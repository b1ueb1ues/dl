from functools import partial
from itertools import combinations

from core.advbase import *

class Bleed(Dot):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0

    def __init__(this, name, dmg_coef):
        Dot.__init__(this, name, dmg_coef, 30, 4.99)
        this.quickshot_event = Event("dmg_formula")
        this.quickshot_event.dmg_coef = dmg_coef
        this.quickshot_event.dname = 's_bleed'
        this.dot_end_timer = Timer(this.dot_end_proc)
        this.true_dmg_event = Event("true_dmg")
        this.true_dmg_event.dname = 'o_bleed'
        this.true_dmg_event.dtype = 's'

    def reset(this):
        this._static['all_bleeds'] = []
        this._static['stacks'] = 0
        return this

    def tick_proc(this, e):
        dmg_sum = 0
        stacks = this._static['stacks']
        for i in this._static['all_bleeds']:
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
        this.true_dmg_event.comment = "%d stacks"%stacks
        this.true_dmg_event.count = dmg
        this.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += this.iv

    def dot_end_proc(this, e):
        idx = this._static['all_bleeds'].index(this)
        this._static['all_bleeds'].pop(idx)
        this._static['stacks'] -= 1
        log('debuff','bleed','stack_end',"stack <%d>"%this._static['stacks'])
        if this._static['stacks'] < 0:
            print('err in bleed dot_end_proc')
            exit()
        if this._static['stacks'] == 0:
            this._static['tick_event'].off()


    def on(this):
        if this._static['stacks'] == 3:
            log('resist','bleed')
            return
        elif this._static['stacks'] > 3:
            print("err in bleed on")
            exit()

        log('debuff','bleed')
        this.quickshot_event()
        this._static['all_bleeds'].append(this)
        this.dot_end_timer.on(this.duration)

        if this._static['stacks'] == 0:
            this._static['tick_event'] = Timer(this.tick_proc).on(this.iv)
        elif this._static['stacks'] < 3:
            pass
        this._static['stacks'] += 1


class mBleed(Bleed):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0
    _static['cache'] = []

    def __init__(this, name, dmg_coef, chance=0.8):
        super(mBleed, this).__init__(name, dmg_coef)
        this.end_index = None
        this.chance = chance

    def sum_bleeds(this, bleeds, active=None, probability=1.0, index=0):
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
            The probability that this particular situation happens
        index : optional
            The index in the list of bleeds we're current at
            If equal to the length, it instead adds up damage and also caches for the next tick
        """
        if active is None:
            active = []

        # remove bleeds that expire at this index
        for bleed in active:
            if bleed.end_index is not None and index > bleed.end_index:
                active.remove(bleed)

        # we're past the last bleed; time to add up
        if index == len(bleeds):
            total = 0.0
            stacks = len(active)
            cache = this._static['cache']

            # find if a currently cached call has the same set of active bleed stacks
            # if so just add to its probability instead of adding more cached called
            equivalents = list(filter(lambda p: p.keywords['active'] == active, cache))
            if equivalents:
                equivalents[0].keywords['probability'] += probability
            else:
                this._static['cache'].append(partial(this.sum_bleeds, active=active, probability=probability, index=index))

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
            return this.sum_bleeds(bleeds, active + [current], probability * current.chance, index + 1) + \
                   this.sum_bleeds(bleeds, active, probability * (1.0 - current.chance), index + 1)
        else:
            # stacks saturated, guaranteed whiff
            return this.sum_bleeds(bleeds, active, probability, index + 1)


    def tick_proc(this, e):
        stacks = this._static['stacks']
        cache = this._static['cache']
        this._static['cache'] = []
        bleeds = this._static['all_bleeds']

        dmg = 0
        if cache:
            for cached in cache:
                dmg += cached(bleeds)
        else:
            dmg = this.sum_bleeds(bleeds)

        this.true_dmg_event.comment = "%d lifetime stacks"%stacks
        this.true_dmg_event.count = dmg
        this.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += this.iv

    def on(this):
        log('debuff','bleed')
        this.quickshot_event()
        this._static['all_bleeds'].append(this)
        this.dot_end_timer.on(this.duration)

        if this._static['stacks'] == 0:
            this._static['tick_event'] = Timer(this.tick_proc).on(this.iv)

        this._static['stacks'] += 1

    def dot_end_proc(this, e):
        # can't remove this in order to build a more accurate picture
        length = len(this._static['all_bleeds'])

        # the index of the last element of the bleed list when this expires
        # any future bleeds (ones with index strictly greater than this)
        # will not be directly blocked by this bleed
        this.end_index = length-1
        this._static['stacks'] -= 1
        log('debuff', 'bleed', 'stack_end', "stack <%d>" % this._static['stacks'])
        if this._static['stacks'] < 0:
            print('err in bleed dot_end_proc')
            exit()

    def reset(this):
        this._static['all_bleeds'] = []
        this._static['stacks'] = 0
        this._static['cache'] = []
        return this
