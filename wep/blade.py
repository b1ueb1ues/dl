from core import Conf

conf = Conf()

conf.actions = Conf()

conf.actions.x1 = Conf()
conf.actions.x2 = Conf()
conf.actions.x3 = Conf()
conf.actions.x4 = Conf()
conf.actions.x5 = Conf()
conf.actions.fs = Conf()
conf.actions.fsf = Conf()
conf.actions.dodge = Conf()

conf.xtype       = 'melee'

conf.actions.x1.dmg      = 97     / 100.0
conf.actions.x1.sp       = 130
conf.actions.x1.startup  = 10     / 60.0
conf.actions.x1.recovery = 23     / 60.0

conf.actions.x2.dmg      = 97     / 100.0
conf.actions.x2.sp       = 130
conf.actions.x2.startup  = 0
conf.actions.x2.recovery = 41     / 60.0

conf.actions.x3.dmg      = 63*2   / 100.0
conf.actions.x3.sp       = 220
conf.actions.x3.startup  = 6      / 60.0
conf.actions.x3.recovery = 37     / 60.0

conf.actions.x4.dmg      = 129    / 100.0
conf.actions.x4.sp       = 360
conf.actions.x4.startup  = 0
conf.actions.x4.recovery = 65     / 60.0

conf.actions.x5.dmg      = 194    / 100.0
conf.actions.x5.sp       = 660
conf.actions.x5.startup  = 0
conf.actions.x5.recovery = 33     / 60.0

conf.actions.fsf.startup  = 0
conf.actions.fsf.recovery = 33     / 60.0

conf.actions.fs.dmg       = 92     / 100.0
conf.actions.fs.sp        = 200
conf.actions.fs.startup   = 30     / 60.0
conf.actions.fs.recovery  = 41     / 60.0

conf.actions.dodge.recovery = 43     / 60.0

