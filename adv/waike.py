import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Waike


class Waike(Adv):
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['afflict_res.bog'] = 100

    def init(self):
        self.fullhp = 0
        if self.conf['afflict_res.bog'] < 100:
            if self.condition('hp100'):
                self.fullhp = 1

    def s2_proc(self, e):
        self.afflics.bog.on('s2', 80+self.fullhp*40)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

