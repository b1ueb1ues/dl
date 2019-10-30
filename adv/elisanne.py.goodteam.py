if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = '10000 team dps; no s2'
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.a'] = BB() + HG()
    conf['slots.d'] = H_Maritimus()
    conf['acl'] = """
         `s1
         `fs, seq=5
         """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
