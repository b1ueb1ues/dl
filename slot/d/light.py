from slot import *

class Gilgamesh(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.5)]

class Cupid(DragonBase):
    ele = 'light'
    att = 119
    a = [('a', 0.6)]

class Takemikazuchi(DragonBase):
    ele = 'light'
    att = 124
    a = [('od', 0.25), ('a', 0.4)]

class Corsaint_Phoenix(DragonBase):
    ele = 'light'
    att = 124
    a = [('k_paralysis', 0.2), ('a', 0.5)]
C_Phoenix = Corsaint_Phoenix

class Shishimai(DragonBase):
    ele = 'light'
    att = 75
    a = [('cd', 0.7)]

class Daikokuten(DragonBase):
    ele = 'light'
    att = 124
    a = [('a', 0.25), ('a', 0.55)]

class GalaShishimai_450CritDmg(DragonBase):
    ele = 'light'
    att = 124
    aura = [('crit','damage',4.5)]

class Unreleased_LightSkillDamage(DragonBase):
    ele = 'light'
    att = 128
    a = [('s', 0.9), ('a', 0.2)]

class Unreleased_LightSkillHaste(DragonBase):
    ele = 'light'
    att = 120
    a = [('sp', 0.35)]

class Unreleased_LightCritDamage(DragonBase):
    ele = 'light'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Unreleased_LightPrimedStr(DragonBase):
    ele = 'light'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]