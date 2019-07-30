import adv_test
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
        `rotation
        """
    conf['rotation'] = """
        c5c5c5c5c4s1c5c4c5s1end
    """
    adv_test.test(module(), conf, verbose=0)

