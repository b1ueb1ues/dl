from slot import *

class Leviathan(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.6)]

class Siren(DragonBase):
    ele = 'water'
    att = 125
    a = [('s', 0.9), ('a', 0.2)]

class Dragonyule_Jeanne(DragonBase):
    ele = 'water'
    att = 125
    a = [('a', 0.30), ('cc', 0.15)]
DJ = Dragonyule_Jeanne

class Simurgh(DragonBase):
    ele = 'water'
    att = 113
    a = [('od', 0.6)]

class Halloween_Maritimus(DragonBase):
    ele = 'water'
    att = 119
    a = [('sp', 0.35)]
H_Maritimus = Halloween_Maritimus

class Kamuy(DragonBase):
    ele = 'water'
    att = 125
    a = [('primed_att', 0.15), ('a', 0.45)]

class Unreleased_WaterCritDamage(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Unreleased_Water80Str(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.8, 'some wacky condition')]

class Unreleased_DKR_What_is_love(DragonBase):
    ele = 'water'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]