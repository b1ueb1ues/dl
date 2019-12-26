from core import Conf

conf = Conf()

conf.xtype       = 'melee'

conf.x1.dmg      = 97     / 100.0
conf.x1.sp       = 130
conf.x1.startup  = 10     / 60.0
conf.x1.recovery = 23     / 60.0

conf.x2.dmg      = 97     / 100.0
conf.x2.sp       = 130
conf.x2.startup  = 0
conf.x2.recovery = 41     / 60.0

conf.x3.dmg      = 63*2   / 100.0
conf.x3.sp       = 220
conf.x3.startup  = 6      / 60.0
conf.x3.recovery = 37     / 60.0

conf.x4.dmg      = 129    / 100.0
conf.x4.sp       = 360
conf.x4.startup  = 0
conf.x4.recovery = 65     / 60.0

conf.x5.dmg      = 194    / 100.0
conf.x5.sp       = 660
conf.x5.startup  = 0
conf.x5.recovery = 33     / 60.0

conf.fsf.startup  = 0
conf.fsf.recovery = 33     / 60.0

conf.fs.dmg       = 92     / 100.0
conf.fs.sp        = 200
conf.fs.startup   = 30     / 60.0
conf.fs.recovery  = 41     / 60.0

conf.dodge.recovery = 43     / 60.0

lv2 = {
    'x1.dmg': 106.7 / 100,
    'x2.dmg': 106.7 / 100,
    'x3.dmg': 69.3*2/ 100,
    'x4.dmg': 141.9 / 100,
    'x5.dmg': 213.4 / 100
}
