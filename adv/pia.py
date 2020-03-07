import adv.adv_test
from core.advbase import *

def module():
    return Pia

class Pia(Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3, seq=5
        `fs, seq=5
        """

    def s2_proc(self, e):
        self.energy.add(1, team=True)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


