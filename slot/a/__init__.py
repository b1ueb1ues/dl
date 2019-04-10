from slot import *
from ability import Ability



class Amulet(AmuletBase):
    def __init__(this):
        this.mod = []
        this.conf = Conf()
        this.mmax = {
                'a'      : 0.15,   # attack
                's'      : 0.35,   # skill damage
                'cc'     : 0.15,   # crit chance
                'cd'     : 0.25,   # crit damage
                'fs'     : 0.35,   # force strike
                'bt'     : 0.30,   # buff time

                'sp'     : 0.15,   # skill haste

                'bk'     : 0.25,   # break killer
                'od'     : 0.15,   # od killer

                'lo'     : 0.50,   # lastoffence
                'bc'     : 0.15,   # buffchain
                'sts'    : 0.06,   # striker strength
                'sls'    : 0.05,   # slayer stength
                'dc'     : 3,      # dragon claw
                'prep'   : 100,    # skill prep
                'resist' : 10000,  # resist
                }


 #   def oninit(this, adv):
 #       super(Amulet, this).oninit(adv)
 #       for i in this.a:
 #           i.oninit(adv)


    def merge(this, a, b):
        k = b[0]
        if k not in a:
            a[k] = b
        else:
            a[k] = (b[0],a[k][1]+b[1])

    def merge_cond(this, a, b):
        k = b[0]+b[2]
        if k not in a:
            a[k] = b
        else:
            a[k] = (b[0],a[k][1]+b[1],b[2])

    def setup(this, c):
        super(Amulet,this).setup(c)
        if this.a2:
            this.on(c)
            this.a2.on(c)
            this.att += this.a2.att
            this.tmp = this.a + this.a2.a
            this.a = {}

        for i in this.tmp:
            if len(i)==2 or (len(i)==3 and i[2]==None):
                k = i[0]
                if this.mmax[k] > 0:
                    if this.mmax[k] > i[1]:
                        this.merge(this.a, i)
                        this.mmax[k] -= i[1]
                    else :
                        i = (i[0],this.mmax[k])
                        this.merge(this.a, i)
                        this.mmax[k] = 0
        for i in this.tmp:
            if len(i)==3 and i[2]!=None:
                k = i[0]
                if this.mmax[k] > 0:
                    if this.mmax[k] > i[1]:
                        this.merge_cond(this.a, i)
                        this.mmax[k] -= i[1]
                    else:
                        i = (i[0],this.mmax[k],i[2])
                        this.merge_cond(this.a, i)
                        this.mmax[k] = 0

        tmp = []
        for k,i in this.a.items():
            tmp.append(i)
        this.a = tmp


    def on(this, c):
        return

from slot.a.all import *
