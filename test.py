from adv import *
from adv.mikoto import *
import slot 

s = slot.Slots('elisanne')
s.d = slot.d.water.Leviathan()
s.w = slot.WeaponBase()
s.w.wt = 'lance'
s.a = slot.a.VC()+slot.a.Witchs_Kitchen()
s.a = slot.a.RR()+slot.a.Bellathorna()


conf = Conf()
conf.acl = Conf()
conf.acl = """
    `s1,seq=5 and cancel
    `s2,seq=5 and cancel
    `s3,seq=5 and cancel
    """

Mikoto(conf).run()
#logcat()
sum_dmg()


print(s.att())
print(s.tmp.a.a)
print(s.att())
print(s.tmp.a.a)

