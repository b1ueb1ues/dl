if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Fjorm

class Fjorm(Adv):
    comment = 'do not calc damage counter'
    a3 = ('prep', 100)
    conf = {}
    conf['slot.a'] = Dragon_and_Tamer()+LC()
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=5
        """

    def prerun(this):
        Teambuff('last bravery',0.3,15).on()
        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

    def s2_proc(this, e):
        this.dmg_make('o_s2reflect', this.s2reflect * 11, fixed=True)

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)


