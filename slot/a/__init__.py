from slot import *
from ability import Ability
from collections import defaultdict


class Amulet(AmuletBase):
    a = []
    def __init__(self):
        self.mod = []
        self.conf = Conf()
        self.mmax = {
                'a'      : 0.20,   # attack
                's'      : 0.40,   # skill damage
                'cc'     : 0.15,   # crit chance
                'cd'     : 0.25,   # crit damage
                'fs'     : 0.50,   # force strike
                'bt'     : 0.30,   # buff time

                'sp'     : 0.15,   # skill haste

                'bk'     : 0.30,   # break killer
                'od'     : 0.15,   # od killer

                'lo'     : 0.60,   # lastoffence
                'bc'     : 0.15,   # buffchain
                'sts'    : 0.06,   # striker strength
                'sls'    : 0.06,   # slayer stength
                'dc'     : 3,      # dragon's claw
                'ds'     : 3,      # dragon's skill
                'prep'   : 100,    # skill prep
                'resist' : 10000,  # resist
                'da'    : 0.18,   # dragon damage
                'dt'    : 0.20,   # dragon time

                'eprep'  : 5, # energy prep
            }
        from core.afflic import AFFLICT_LIST
        for afflic in AFFLICT_LIST:
            self.mmax['k_'+afflic] = 0.25
        self.mmax['k_burn'] = 0.30
        self.base_a = self.a

    def setup(self, c):
        abilities = self.base_a
        if self.a2:
            abilities += self.a2.base_a
            self.att += self.a2.att
        sorted_abilities = defaultdict(lambda: [])
        for ab in abilities:
            name = ab[0]
            sorted_abilities[name].append(ab)
        self.a = []
        for name, ab_list in sorted_abilities.items():
            if name in self.mmax:
                max_value = self.mmax[name]
                for ab in sorted(ab_list, key=lambda x: '' if len(x) < 3 or x[2] in ('flame', 'water', 'wind', 'light', 'shadow') else x[2]):
                    if len(ab) > 2:
                        new_ab = (ab[0], min(ab[1], max_value), *ab[2:])
                    else:
                        new_ab = (ab[0], min(ab[1], max_value))
                    self.a.append(new_ab)
                    max_value -= ab[1]
                    if max_value <= 0:
                        break
            else:
                self.a.extend(ab_list)

 #   def oninit(self, adv):
 #       super(Amulet, self).oninit(adv)
 #       for i in self.a:
 #           i.oninit(adv)


    # def merge(self, a, b):
    #     k = b[0]
    #     if k not in a:
    #         a[k] = b
    #     else:
    #         a[k] = (b[0],a[k][1]+b[1])

    # def merge_cond(self, a, b):
    #     k = b[0]+b[2]
    #     if k not in a:
    #         a[k] = b
    #     else:
    #         a[k] = (b[0],a[k][1]+b[1],b[2])

    # def setup(self, c):
    #     super(Amulet,self).setup(c)
    #     if self.a2:
    #         self.on(c)
    #         self.a2.on(c)
    #         self.att += self.a2.att
    #         self.tmp = self.a + self.a2.a
    #         self.a = {}
    #     else:
    #         self.on(c)
    #         self.tmp = self.a
    #         self.a = {}

    #     for i in self.tmp:
    #         if len(i)==2 or (len(i)==3 and not isinstance(i[2], str)):
    #             k = i[0]
    #             if k not in self.mmax:
    #                 self.merge(self.a, i)
    #             elif self.mmax[k] > 0:
    #                 if self.mmax[k] > i[1]:
    #                     self.merge(self.a, i)
    #                     self.mmax[k] -= i[1]
    #                 else :
    #                     i = (i[0],self.mmax[k])
    #                     self.merge(self.a, i)
    #                     self.mmax[k] = 0
    #     for i in self.tmp:
    #         if len(i)==3 and isinstance(i[2], str):
    #             k = i[0]
    #             if k not in self.mmax:
    #                 self.merge_cond(self.a, i)
    #             elif self.mmax[k] > 0:
    #                 if self.mmax[k] > i[1]:
    #                     self.merge_cond(self.a, i)
    #                     self.mmax[k] -= i[1]
    #                 else:
    #                     i = (i[0],self.mmax[k],i[2])
    #                     self.merge_cond(self.a, i)
    #                     self.mmax[k] = 0

    #     tmp = []
    #     for k,i in self.a.items():
    #         tmp.append(i)
    #     self.a = tmp


    # def on(self, c):
    #     return

from slot.a.all import *
