import copy
from core import Conf
from ability import Ability, ability_dict
from itertools import islice

class Slot(object):
    att = 0
    ele = 'none'
    wt = 'none'
    stype = 'slot'
    onele = 0

    a = None
    mod = None
    conf = None
    def __init__(self):
        if not self.mod:
            self.mod = []
        if not self.conf:
            self.conf = Conf()
        if not self.a:
            self.a = []
        self.name = type(self).__name__

    def setup(self, c):
        if c.ele == self.ele :
            self.onele = 1
        if self.wt != 'none' and c.wt != self.wt:
            raise ValueError('Wrong weapon type, expected {} but got {}'.format(self.wt, c.wt))

    def oninit(self, adv):
        adv.conf(self.conf)

        i = self.stype
        j = self.mod
        if type(j) == tuple:
            adv.Modifier(i,*j)
        elif type(j) == list:
            idx = 0
            for k in j:
                adv.Modifier(i+'_%d'%idx,*k)
                idx += 1
        elif type(j) == dict:
            idx = 0
            for k in j:
                adv.Modifier(i+k+'_%d'%idx,*j[k])
                idx += 1


class CharacterBase(Slot):
    name = 'null'
    stars = 5
    max_coab = 4

    def __init__(self):
        super().__init__()
        self.coabs = {}

    def setup(self):
        return

    def oninit(self, adv):
        Slot.oninit(self, adv)
        count = 0
        ex_set = set()
        coabs = list(islice(self.coabs.items(), self.max_coab))
        self.coabs = {}
        for key, coab in coabs:
            self.coabs[key] = coab
            chain, ex = coab
            if ex:
                ex_set.add(('ex', ex))
            if chain:
                self.a.append(tuple(chain))
            count += 1
        self.a.extend(ex_set)

    def has_ex(self, ex):
        for _, coab in self.coabs.items():
            if ex == coab[1]:
                return True
        return False

class WeaponBase(Slot):
    stype = 'w'
    wt = 'none'
    s3 = Conf()
    ele = [] # or ''

    def setup(self, c, adv):
        super(WeaponBase, self).setup(c)
        if type(self.ele) == list:
            for i in self.ele:
                if c.ele == i :
                    self.onele = 1
                    break

        if self.onele:
            self.att *= 1.5
            if adv is not None and adv.s3.owner is None:
                self.conf.s3 = Conf(self.s3)
        elif 'all' in self.ele:
            if adv is not None and adv.s3.owner is None:
                self.conf.s3 = Conf(self.s3)

        if self.wt == 'axe':
            self.mod.append(('crit','chance',0.04))
        else :
            self.mod.append(('crit','chance',0.02))

    def s3_proc(self, adv, e):
        pass

class DragonBase(Slot):
    stype = 'd'
    a = [('a', 0.60)]
    default_dragonform = {
        'duration': 600 / 60, # 10s dragon time
        'dracolith': 0.40, # base dragon damage
        'exhilaration': 0, # psiren aura
        'skill_use': 1, # number of skill usage
        'gauge_iv': 15, # gauge interval
        'gauge_val': 10, # gauge regen value
        'latency': 0, # amount of delay for cancel
        'act': 'end',

        'dshift.startup': 96 / 60, # shift 102 -> 96 + 6
        'dshift.recovery': 0 / 60, # assumed cancel
        'dshift.dmg': 2.00,
        'dshift.hit': 1,

        'dx1.recovery': 0,
        'dx2.recovery': 0,
        'dx3.recovery': 0,
        'dx4.recovery': 0,
        'dx5.recovery': 0,
        'ds.startup': 0,

        'dodge.startup': 40 / 60, # dodge frames
        'dodge.recovery': 0,
        'dodge.hit': 0,

        'end.startup': 0, # amount of time needed to kys, 0 default
        'end.recovery': 0
    }
    dragonform = {}

    def setup(self, c):
        Slot.setup(self, c)
        if self.onele:
            self.att *= 1.5
        else:
            self.a = []

    def ds_proc(self):
        try:
            return self.adv.dmg_make('ds',self.adv.dragonform.conf.ds.dmg,'s')
        except:
            return 0

    def oninit(self, adv):
        super().oninit(adv)
        gauge_iv = min(int(adv.duration/12), 15)
        from core.dragonform import DragonForm
        self.adv = adv
        if 'dragonform' in adv.conf:
            name = type(adv).__name__
            dconf = Conf(self.default_dragonform)
            dconf += adv.conf.dragonform
            dconf.gauge_iv = gauge_iv
            self.adv.dragonform = DragonForm(name, dconf, adv, adv.ds_proc)
        else:
            name = type(self).__name__
            dconf = Conf({**self.default_dragonform, **self.dragonform})
            dconf.gauge_iv = gauge_iv
            self.adv.dragonform = DragonForm(name, dconf, adv, self.ds_proc)

class Amuletempty(object):
    stype = 'a2'
    def oninit(self,adv):
        return
    def setup(self, c, adv):
        return


class AmuletBase(Slot):
    ae = Amuletempty()
    stype = 'a'
    a2 = None

    def __add__(self, another):
        if type(self) is type(another):
            raise ValueError('Cannot equip two of the same wyrmprint')
        self.a2 = another
        self.a2.stype = 'a2'
        return self

    def oninit(self, adv):
        Slot.oninit(self, adv)
        if self.a2:
            self.a2.a2 = None
            self.a2.oninit(adv)



class Slots(object):
    #w = None
    #d = None
    #a = None
    #a2 = None
    #w = WeaponBase()
    #d = DragonBase()
    #a = AmuletBase()+AmuletBase()
    #c = CharacterBase()
    #a2 = AmuletBase()
    def __str__(self):
        r = str(self.c) + '\n'
        r += str(self.d) + '\n'
        r += str(self.w) + '\n'
        r += str(self.a) + '\n'
        r += str(self.a.a2) + '\n'
        return r


    def __init__(self):
        self.c = CharacterBase()
        #self.w = WeaponBase()
        #self.d = DragonBase()
        #self.a = AmuletBase()+AmuletBase()
        self.w = None
        self.d = None
        self.a = None

    def __setup(self, adv):
        self.c.setup()
        self.w.setup(self.c, adv)
        self.d.setup(self.c)
        self.a.setup(self.c)


    def oninit(self, adv):
        tmp = copy.deepcopy(self)
        self.tmp = tmp
        tmp.__setup(adv)
        tmp.c.oninit(adv)
        tmp.w.oninit(adv)
        tmp.d.oninit(adv)
        tmp.a.oninit(adv)
        self.abilities = {'c':{}, 'w':{}, 'd':{}, 'a':{}}
        for afrom, alist in [('c', tmp.c.a), ('w', tmp.w.a), ('d', tmp.d.a), ('a', tmp.a.a)]:
            for ab in alist:
                name = ab[0]
                if '_' in name:
                    acat = name.split('_')[0]
                else:
                    acat = name
                self.abilities[afrom][name] = ability_dict[acat](*ab)
                self.abilities[afrom][name].oninit(adv, afrom)

    def att(self, forte=None):
        tmp = copy.deepcopy(self)
        self.tmp = tmp
        tmp.__setup(None)
        if not forte:
            return tmp.c.att + tmp.d.att + tmp.w.att + tmp.a.att
        # return tmp.c.att*forte.c(tmp.c.ele,tmp.c.wt) + tmp.d.att*forte.d(tmp.d.ele) + tmp.w.att + tmp.a.att
        return (tmp.c.att+100)*forte.c(tmp.c.ele,tmp.c.wt) + tmp.d.att*forte.d(tmp.d.ele) + tmp.w.att + (tmp.a.att+200)

import slot.d as d
import slot.w as w
import slot.a as a
