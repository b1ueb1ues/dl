import adv.adv_test
from core.advbase import *

def module():
    return Vida

class Vida(Adv):
#    comment = 'unsuitable resist'
    a1 = ('fs',0.30)
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    def prerun(self):
        self.s2charge = 0

    def s2_proc(self, e):
        self.s2charge = 3

    def fs_proc(self, e):
        if self.s2charge > 0:
            self.s2charge -= 1
            self.dmg_make("o_fs_boost",0.21*3)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

