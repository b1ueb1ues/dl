from __init__ import *

class Dragon(DragonBase):
    ele = 'water'
    att = 125
    def onele(this, ele):
        this.mod = [('att','passive',0.45),
                    ('crit','chance',0.2)]
        this.att *= 1.5

