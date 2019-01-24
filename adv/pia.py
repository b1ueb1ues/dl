import adv_test
from adv import *
from module import energy

def module():
    return Pia

class Pia(Adv):
    comment = 'no fs'
    def init(this):
        energy.Energy(this,{'s2':1},{'s2':1})

    def condition(this):
        this.conf['acl'] = """
            `s1, seq=5 and cancel
            `s3, seq=5 and cancel
            """
        return 'no s2'


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)


