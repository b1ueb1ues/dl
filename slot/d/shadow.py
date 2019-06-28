from slot import *

class Marishiten(DragonBase):
    ele = 'shadow'
    att = 121


class Nyarlathotep(DragonBase):
    ele = 'shadow'
    att = 128
    aura = ('att','passive',0.50,'hp30')


class Shinobi(DragonBase):
    ele = 'shadow'
    att = 128
    aura = [('att','passive',0.2),
            ('s','passive',0.7)]



