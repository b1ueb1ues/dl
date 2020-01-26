import adv_test
import adv
import natalie
from slot.a import HoH, FoG

def module():
    return Natalie

class Natalie(natalie.Natalie):
    comment = '1hp;'

    def d_slots(this):
        this.slots.a = HoH() + FoG()

    def d_acl(this):
        this.conf['acl'] = """
        `s2
        `s1
        `s3, seq=5
        `fs, seq=5 and s1.sp-212<=s1.charged and s1.charged<=s1.sp
    """
    
    def init(this):
        super().init()
        this.hp = 0

    def s2_proc(this, e):
        if this.hp <= 30:
            adv.Selfbuff('s2', 0.15, 10).on()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2, mass=1)