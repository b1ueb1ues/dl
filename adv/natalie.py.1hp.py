import adv.adv_test
from core.advbase import *
import adv.natalie
from slot.a import HoH, Primal_Crisis

def module():
    return Natalie

class Natalie(adv.natalie.Natalie):
    comment = ''

    conf = adv.natalie.Natalie.conf.copy()
    conf['slot.a'] = HoH()+Primal_Crisis()
    conf['acl'] = """
        `s2
        `s1
        `s3, seq=5
        `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
    """

    def prerun(this):
        super().prerun()
        this.hp = 0
        this.a3atk.on()
        this.a3spd.on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)