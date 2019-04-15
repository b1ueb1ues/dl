import adv_test
from adv import *
import copy
from module.fsalt import *
import albert
from slot.a import *


def module():
    return Albert


class Albert(albert.Albert):
    def pre(this):
        super(Albert,this).pre()
        this.conf.slots.a = RR() + The_Chocolatiers()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1, this.s2.charged > 900
        `s3
        `fs, seq=2
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

