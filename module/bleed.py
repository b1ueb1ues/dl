from functools import partial
from itertools import combinations

from core.advbase import *

class Bleed(Dot):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0

    def __init__(self, name, dmg_coef, duration=30):
        Dot.__init__(self, name, dmg_coef, duration, 4.99)
        self.quickshot_event = Event("dmg_formula")
        self.quickshot_event.dmg_coef = dmg_coef
        self.quickshot_event.dname = 's_bleed'
        self.dot_end_timer = Timer(self.dot_end_proc)
        self.true_dmg_event = Event("true_dmg")
        self.true_dmg_event.dname = 'o_{}_bleed'.format(name)
        self.true_dmg_event.dtype = 's'

    def reset(self):
        self._static['all_bleeds'] = []
        self._static['stacks'] = 0
        return self

    def tick_proc(self, e):
        dmg_sum = 0
        stacks = self._static['stacks']
        for i in self._static['all_bleeds']:
            dmg_sum += i.quickshot_event.dmg
        if stacks == 1:
            dmg = dmg_sum
        elif stacks == 2:
            dmg = dmg_sum * 1.5
        elif stacks == 3:
            dmg = dmg_sum * 2
        else:
            print("err in bleed tick_proc")
            exit()
        self.true_dmg_event.comment = " stack <%d>"%stacks
        self.true_dmg_event.count = dmg
        self.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += self.iv

    def dot_end_proc(self, e):
        idx = self._static['all_bleeds'].index(self)
        self._static['all_bleeds'].pop(idx)
        self._static['stacks'] -= 1
        log('debuff','bleed','stack_end',"stack <%d>"%self._static['stacks'])
        if self._static['stacks'] < 0:
            print('err in bleed dot_end_proc')
            exit()
        if self._static['stacks'] == 0:
            self._static['tick_event'].off()

    def get(self):
        return self._static['stacks']
    
    def on(self):
        if self._static['stacks'] == 3:
            log('resist','bleed')
            return
        elif self._static['stacks'] > 3:
            print("err in bleed on")
            exit()

        log('debuff','bleed')
        self.quickshot_event()
        self._static['all_bleeds'].append(self)
        self.dot_end_timer.on(self.duration)

        if self._static['stacks'] == 0:
            self._static['tick_event'] = Timer(self.tick_proc).on(self.iv)
        elif self._static['stacks'] < 3:
            pass
        self._static['stacks'] += 1


class mBleed(Bleed):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0
    _static['cache'] = []

    def __init__(self, name, dmg_coef, chance=0.8):
        super(mBleed, self).__init__(name, dmg_coef)
        self.end_index = None
        self.chance = chance

    def sum_bleeds(self, bleeds, active=None, probability=1.0, index=0):
        """ Calculates the total damage from bleed during the current tick
        Keeps a running probability of each possible combination of active bleed stacks in cache
        Also able to calculate it from scratch which is slower

        Parameters
        ----------
        bleeds : list
            The list of all current and past bleed instances
        active : list, optional
            The list of currently active bleed instances
        probability : float, optional
            The probability that self particular situation happens
        index : int, optional
            The index in the list of bleeds we're current at
            If equal to the length, it instead adds up damage and also caches for the next tick
        """
        if active is None:
            active = []

        # remove bleeds that expire at self index
        for bleed in active:
            if bleed.end_index is not None and index > bleed.end_index:
                active.remove(bleed)

        # we're past the last bleed; time to add up
        if index == len(bleeds):
            total = 0.0
            stacks = len(active)
            cache = self._static['cache']

            # find if a currently cached call has the same set of active bleed stacks
            # if so just add to its probability instead of adding more cached calls
            equivalents = list(filter(lambda p: p.keywords['active'] == active, cache))
            if equivalents:
                equivalents[0].keywords['probability'] += probability
            else:
                self._static['cache'].append(partial(self.sum_bleeds, active=active, probability=probability, index=index))

            for bleed in active:
                total += bleed.quickshot_event.dmg

            if stacks == 3:
                return total * 2 * probability
            elif stacks == 2:
                return total * 1.5 * probability
            elif stacks == 1:
                return total * probability
            else:
                return 0

        if len(active) < 3:
            # still have room for another stack
            # add the damages from having it whiff and proc
            current = bleeds[index]
            return self.sum_bleeds(bleeds, active + [current], probability * current.chance, index + 1) + \
                   self.sum_bleeds(bleeds, active, probability * (1.0 - current.chance), index + 1)
        else:
            # stacks saturated, guaranteed whiff
            return self.sum_bleeds(bleeds, active, probability, index + 1)


    def tick_proc(self, e):
        stacks = self._static['stacks']
        cache = self._static['cache']
        self._static['cache'] = []
        bleeds = self._static['all_bleeds']

        dmg = 0
        if cache:
            for cached in cache:
                dmg += cached(bleeds)
        else:
            dmg = self.sum_bleeds(bleeds)

        self.true_dmg_event.comment = "%d active stacks"%stacks
        self.true_dmg_event.count = dmg
        self.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += self.iv

    def on(self):
        log('debuff','bleed')
        self.quickshot_event()
        self._static['all_bleeds'].append(self)
        self.dot_end_timer.on(self.duration)

        if self._static['stacks'] == 0:
            self._static['tick_event'] = Timer(self.tick_proc).on(self.iv)

        self._static['stacks'] += 1

    def dot_end_proc(self, e):
        # can't remove self in order to build a more accurate picture
        length = len(self._static['all_bleeds'])

        # the index of the last element of the bleed list when self expires
        # any future bleeds (ones with index strictly greater than self)
        # will not be directly blocked by self bleed
        self.end_index = length-1
        self._static['stacks'] -= 1
        log('debuff', 'bleed', 'stack_end', "stack <%d>" % self._static['stacks'])
        if self._static['stacks'] < 0:
            print('err in bleed dot_end_proc')
            exit()

    def reset(self):
        self._static['all_bleeds'] = []
        self._static['stacks'] = 0
        self._static['cache'] = []
        return self
