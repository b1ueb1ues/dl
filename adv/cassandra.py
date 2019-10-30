if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Cassandra

class Flash_of_Genius(Amulet):
    att = 57

class Cassandra(Adv):
    # comment = 'no counter damage'
    a1 = ('prep','100%')
    conf = {}
    conf['slots.a'] = CC()+Flash_of_Genius()
    conf['acl'] = """
        `s1
        `s2, seq=5
    """

    def prerun(this):
        this.comment = 's2 drops combo'
        this.hits = 0
        this.flurry_str = Selfbuff('flurry_str',0.2,-1,'att','passive')
        
        timing = adv_test.sim_duration/3
        this.ro(0)
        Timer(this.ro).on(timing)
        Timer(this.ro).on(timing*2)
        if this.condition('reflect 500 damage on every s2'):
            this.s2reflect = 500
        else:
            this.s2reflect = 0

    def dmg_proc(this, name, amount):
        if name == 'x1':
            this.hits += 1
        elif name == 'x2':
            this.hits += 2
        elif name == 'x3':
            this.hits += 3
        elif name == 'x4':
            this.hits += 2
        elif name == 'x5':
            this.hits += 5
        elif name == 'fs':
            this.hits += 2
        elif name == 's1':
            this.hits += 2
        elif name == 's2':
            this.hits += 5

        if this.hits >= 15:
            this.flurry_str.on()

    def ro(this, t):
        Selfbuff('a3',0.10,-1).on()

    def s2_proc(this, e):
        this.dmg_make('o_s2_reflect', this.s2reflect * 11, fixed=True)
        this.flurry_str.off()


if __name__ == '__main__':
    adv_test.test(module(), conf, verbose=0)

