import adv_test
from adv import *
from slot.a import *

def module():
    return Fjorm

class Fjorm(Adv):
    comment = 'do not calc damage counter'
    a3 = ('prep', 100)

    def init(this):
        Teambuff('last bravery',0.3,15).on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)


