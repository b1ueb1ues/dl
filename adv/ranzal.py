import adv_test
import adv
from slot.d import *

def module():
    return Ranzal

class Ranzal(adv.Adv):
    comment = 'do not use fs'
    import slot.a
    conf = {}
    conf['slot.a'] = slot.a.KFM()+slot.a.CE()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

