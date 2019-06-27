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
    conf['slots.a'] = RR() + JotS()
    


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        # import core.log
        # log = core.log.log
        # log('debug',dname)
        `s1, cancel
        `s2, cancel
        `s1, pin == 'prep'
        `fs, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)

