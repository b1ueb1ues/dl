if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *
import slot.a
from slot.d import *

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c2+fs'

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+BN()
        else:
            this.conf.slot.a = TSO()+JotS()

    a3 = ('fs',0.50)

    conf = {}
    conf['slots.a'] = TSO()+JotS()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=2 and cancel
        """
    #a = 3
    #if a==1:
    #    conf['slots.a'] = RR()+FP()
    #elif a == 2:
    #    conf['slots.a'] = RR()+The_Prince_of_Dragonyule()
    #elif a == 3:
    #    conf['slots.a'] = RR()+slot.a.Stellar_Show()
    #elif a == 4:
    #    conf['slots.a'] = The_Prince_of_Dragonyule()+slot.a.Stellar_Show()



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

