if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *

def module():
    return Ezelith

class Ezelith(Adv):
    comment = ''
    a3 = ('bk',0.3)
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """


    def prerun(this):
        random.seed()
        this.s2buff = Selfbuff("s2",0.15, 15)
        this.s2chance = 0.15
        if this.condition('hp70'):
            this.s2chance += 0.2

    def s2_proc(this, e):
        this.s2buff.on()

    def dmg_proc(this, name, amount):
        if name[0] != 'x':
            return
        if this.s2buff.get():
            r = random.random()
            if r < this.s2chance:
                Debuff("s2_ab",0.05,5,1).on()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, mass=1, verbose=-2)

