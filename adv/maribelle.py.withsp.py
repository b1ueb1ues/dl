import adv_test
from adv import *
import adv.maribelle

from slot.a import *

def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    name = 'maribelle'
    conf = {}
    conf['slots.a'] = Heralds_of_Hinomoto() + CE()
    


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        # from core.log import *
        # log('debug',dname)
        `s1, seq=5 and cancel
        `s1, sp and dname == 'fs'
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        `fs, seq=5 and s1.charged>1600
        `s3, s
        """
    adv_test.test(module(), conf, verbose=0)

