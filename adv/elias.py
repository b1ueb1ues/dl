if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from module import energy

def module():
    return Elias

class Elias(adv.Adv):
    a3 = ('lo',0.4)
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def c_prerun(this):
        energy.Energy(this,{'s2':1},{'s2':1})
        if this.condition('c4+fs & no s2'):
            this.conf['acl'] = """
                `s1, fsc
                `s3, fsc
                `fs, seq=4
                """

    def prerun(this):
        energy.Energy(this,{},{})

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
