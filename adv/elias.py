import adv.adv_test
from core.advbase import *

def module():
    return Elias

class Elias(Adv):
    a3 = ('lo',0.4)
    conf = {}
    conf['acl'] = """
    `s1, fsc
    `s3, fsc
    `fs, seq=4
    """

    def s2_proc(self, e):
        self.energy.add(1, team=True)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
