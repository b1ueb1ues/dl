import adv_test
import adv

def module():
    return Eleonora

class Eleonora(adv.Adv):
    a3 = ('prep','50%')

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100
        if this.condition('fullhp=poison'):
            this.fullhp = 1
        else:
            this.fullhp = 0

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s1_proc(this, e):
        this.afflics.poison('s1',110+50*this.fullhp,0.53)

    def s2_proc(this, e):
        this.afflics.poison('s2',100+50*this.fullhp,0.396)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
