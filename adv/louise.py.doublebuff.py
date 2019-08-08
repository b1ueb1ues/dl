import adv.adv_test
import adv
from slot.a import *
import louise

def module():
    return Louise

class Louise(louise.Louise):
    def prerun(this):
        super(Louise, this).prerun()
        adv.Buff('double',(0.13+0.08)*7,30).on()



if __name__ == '__main__':
    module().comment = 'roll fs & g_ranzal+lowen'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `dodge, fsc
        `fs
        """
    conf['slots.a'] = Stellar_Show() + Forest_Bonds()
    from slot.d import *
    conf['slot.d'] = Pazuzu()

    adv_test.test(module(), conf, verbose=0)
