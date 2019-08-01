import adv_test
from adv import *
import fleur

def module():
    return Fleur

class Fleur(fleur.Fleur):
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
        """
    conf['rotation'] = """
        c5fsc5fsc5fs c5fs c5 c5fs s3  c1fs s1 c3 fs end
    """
    adv_test.test(module(), conf, verbose=0)




