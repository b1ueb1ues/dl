if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
import adv.maribelle
from slot import *



class wand(WeaponBase):
    ele = ['wind']
    wt = 'wand'
    att = 372 
    a = [('k',0.3), ('prep','50%')]

def module():
    return Maribelle_s3

class Maribelle_s3(adv.maribelle.Maribelle):
    name = 'maribelle'
    conf = {}
    conf['slot.w'] = wand()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """
        
    adv_test.test(module(), conf, verbose=0)

