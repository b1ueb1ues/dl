from slot import *

class Cerberus(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.6)]

class Arctos(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.45), ('cd', 0.55)]

class Prometheus(DragonBase):
    ele = 'flame'
    att = 121
    a = [('a', 0.5)]

class Sakuya(DragonBase):
    ele = 'flame'
    att = 121
    a = [('s', 0.9), ('a', 0.2)]

class Apollo(DragonBase):
    ele = 'flame'
    att = 127
    a = [('k_burn', 0.2), ('a', 0.5)]

class Kagutsuchi(DragonBase):
    ele = 'flame'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]

class Dreadking_Rathalos(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]

class Unreleased_FlameSkillHaste(DragonBase):
    ele = 'flame'
    att = 120
    a = [('sp', 0.35)]

class Unreleased_Flame80Str(DragonBase):
    ele = 'flame'
    att = 127
    a = [('a', 0.8, 'some wacky condition')]