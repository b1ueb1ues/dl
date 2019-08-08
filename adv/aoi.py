if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.d import *

def module():
    return Aoi

class Aoi(adv.Adv):
    a1 = ('od',0.08)


if __name__ == '__main__':
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

