if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *

def module():
    return Sinoa

class Sinoa(adv.Adv):
    def s1_proc(this, e):
        adv.Teambuff('s1_att',0.25/4,15,'att').on()
        adv.Teambuff('s1_crit',0.25/4,10,'crit').on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=0)


