if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    a3 = ('lo',0.3)
    conf = {}
    conf['slot.a'] = RR()+SS()
    conf['slot.d'] = Marishiten()
    conf['acl'] = """
        `s1
        `fs, seq=2 and cancel
        """
    a3 = ('lo',0.3)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

