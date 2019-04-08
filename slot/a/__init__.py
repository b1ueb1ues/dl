from slot import *

class Amulet(AmuletBase):
    def setup(this, c):
        super(Amulet,this).setup(c)

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

mmax = {
        'cc'   : 0.15,   # crit chance
        'cd'   : 0.25,   # crit damage
        'fs'   : 0.35,   # force strike
        'sp'   : 0.15,   # skill haste
        'a'    : 0.15,   # attack
        'bk'   : 0.25,   # break killer
        'bt'   : 0.30,   # buff time
        'od'   : 0.15,   # od killer

        'lo'   : 0.50,   # lastoffence
        'sts'  : 0.06,   # striker strength
        'sls'  : 0.05,   # slayer stength
        'db'   : 0.15,   # doublebuff
        'dc'   : 3,      # dragon claw
        'prep' : 100,    # skill prep
        }


class RR(Amulet):
    att = 64
    mod = [('s','p',0.25),
           ('c','c',0.06,'hp70')]


class LC(Amulet):
    att = 64
    mod = [('c','d',0.13),
           ('c','c',0.08,'hp70')]
