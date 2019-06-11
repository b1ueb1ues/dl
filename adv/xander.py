import adv_test
import adv
from slot.a import *
import slot.a

def module():
    return Xander

class Xander(adv.Adv):
    comment = 'c2+fs'

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
    #from module import ra
    #ra.test(module(), conf)
    #exit()
    adv_test.test(module(), conf, verbose=0, mass=0)

