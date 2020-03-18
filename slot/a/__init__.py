from slot import *
from ability import Ability



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
                'dc'     : 3,      # dragon claw
                'prep'   : 100,    # skill prep
                'resist' : 10000,  # resist
                'dra'    : 0.18,   # dragon damage
                'drt'    : 0.20,   # dragon time

                'eprep'  : 5, # energy prep
            }
        from core.afflic import AFFLICT_LIST
        for afflic in AFFLICT_LIST:
            self.mmax['k_'+afflic] = 0.25
        self.mmax['k_burn'] = 0.30


 #   def oninit(self, adv):
 #       super(Amulet, self).oninit(adv)
 #       for i in self.a:
 #           i.oninit(adv)


    def merge(self, a, b):
        k = b[0]
        if k not in a:
            a[k] = b
        else:
            a[k] = (b[0],a[k][1]+b[1])

    def merge_cond(self, a, b):
        k = b[0]+b[2]
        if k not in a:
            a[k] = b
        else:
            a[k] = (b[0],a[k][1]+b[1],b[2])

    def setup(self, c):
        super(Amulet,self).setup(c)
        if self.a2:
            self.on(c)
            self.a2.on(c)
            self.att += self.a2.att
            self.tmp = self.a + self.a2.a
            self.a = {}
        else:
            self.on(c)
            self.tmp = self.a
            self.a = {}

        for i in self.tmp:
            if len(i)==2 or (len(i)==3 and not isinstance(i[2], str)):
                k = i[0]
                if k not in self.mmax:
                    self.merge(self.a, i)
                elif self.mmax[k] > 0:
                    if self.mmax[k] > i[1]:
                        self.merge(self.a, i)
                        self.mmax[k] -= i[1]
                    else :
                        i = (i[0],self.mmax[k])
                        self.merge(self.a, i)
                        self.mmax[k] = 0
        for i in self.tmp:
            if len(i)==3 and isinstance(i[2], str):
                k = i[0]
                if k not in self.mmax:
                    self.merge_cond(self.a, i)
                elif self.mmax[k] > 0:
                    if self.mmax[k] > i[1]:
                        self.merge_cond(self.a, i)
                        self.mmax[k] -= i[1]
                    else:
                        i = (i[0],self.mmax[k],i[2])
                        self.merge_cond(self.a, i)
                        self.mmax[k] = 0

        tmp = []
        for k,i in self.a.items():
            tmp.append(i)
        self.a = tmp


    def on(self, c):
        return

from slot.a.all import *
