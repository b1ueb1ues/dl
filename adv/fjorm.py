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
    conf['slot.a'] = Dragon_and_Tamer()+LC()
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)


