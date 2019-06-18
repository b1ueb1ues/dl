import adv_test
from adv import *
import linyou


from slot import *
class axe(WeaponBase):
    ele = ['wind']
    wt = 'axe'
    att = 357 
    a = [('k',0.3), ('prep','50%')]

def module():
    return Linyou


class Linyou(linyou.Linyou):
    conf = {}
    conf['slot.w'] = axe()
    conf['slot.a'] = slot.a.KFM() + slot.a.Evening_of_Luxury()

if __name__ == '__main__':
    conf = {
        }

    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440
        `s1
        `s2, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

