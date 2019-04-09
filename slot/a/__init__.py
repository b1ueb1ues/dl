from slot import *


mtype = {
    'a'  : 'attack',
    's'  : 'skill',
    'c'  : 'crit',
    'fs' : 'force strike',
    'sp' : 'skill haste',
    'b'  : 'bufftime',
}

morder = {
    'p'    : 'passive',
    'c'    : 'crit chance',
    'd'    : 'crit damage',
    'k'    : 'killer',
    'bk'   : 'break',
    'buff' : 'buff',
}


class Ability(object):
    def __init__(this, name, value, cond=None):
        this.name = name
        this.value = value
        this.cond = cond
        this.mod = []
        if name == 'a':
            this.mod = ('att','passive',value, cond)
        elif name == 's':
            this.mod = ('s','passive',value, cond)
        elif name == 'cc':
            this.mod = ('crit','chance',value, cond)
        elif name == 'cd':
            this.mod = ('crit','damage',value, cond)
        elif name == 'fs':
            this.mod = ('fs','passive',value, cond)
        elif name == 'bt':
            this.mod = ('buff','time',value, cond)

        elif name == 'sp':
            if cond != 'fs':
                this.mod = ('sp','passive',value, cond)

        elif name == 'bk':
            this.mod = ('att','bk',value*0.15, cond)
        elif name == 'od':
            this.mod = ('att','killer',value*0.45, cond)


        
class Amulet(AmuletBase):
    a = []
    def __init__(this):
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

    def oninit(this, adv):
        pass


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
        for i in this.a:
            tmp.append(this.a[i])
        this.a = tmp
        print(this.a)


    def on(this, c):
        return

from slot.a.all import *
