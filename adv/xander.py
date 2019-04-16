import adv_test
import adv
from slot.a import *
import slot.a

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c2+fs & stella show + RR'

    a3 = ('fs',0.50)

    conf = {}
    a = 3
    if a==1:
        conf['slots.a'] = RR()+FP()
    elif a == 2:
        conf['slots.a'] = RR()+The_Prince_of_Dragonyule()
    elif a == 3:
        conf['slots.a'] = RR()+slot.a.Stellar_Show()
    elif a == 4:
        conf['slots.a'] = The_Prince_of_Dragonyule()+slot.a.Stellar_Show()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `fs, seq=2 and cancel
        """
    #conf['slots.a'] = Stellar_Show() + VC() 
    adv_test.test(module(), conf, verbose=0, mass=0)
    exit()

    ams = slot.a.amulets
    amlen = len(ams)
    for m in range(amlen):
        for n in range(m+1,amlen):
            i = ams[m]
            j = ams[n]
            conf['slots.a'] = i() + j()
            module().comment = '(',type(i()).__name__, type(j()).__name__,')'
            adv_test.test(module(), conf, verbose=-1, mass=0)
