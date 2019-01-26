import adv_test
import adv
from module import energy

def module():
    return Elias

class Elias(adv.Adv):
    def condition(this):
        this.conf['acl'] = """
            `s1, fsc
            `s3, fsc
            `fs, seq=4
            """
        this.init = this.c_init
        return 'last offense & c4+fs & no s2'

    def c_init(this):
        adv.Buff('last_offense',0.4,15,wide='self').on()
        energy.Energy(this,{'s2':1},{'s2':1})

   # def init(this):
   #     energy.Energy(this,{'s2':1},{'s2':1})

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
