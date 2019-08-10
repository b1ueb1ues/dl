if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.d import *

def module():
    return Berserker

class Berserker(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=3 and cancel
        """
    conf['slot.d'] = Marishiten()
    a3 = ('lo',0.3)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

