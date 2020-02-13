import adv.adv_test
import adv
from slot.d import *

def module():
    return Waike


class Waike(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['afflict_res.bog'] = 100

    def init(this):
        this.fullhp = 0
        if conf['afflict_res.bog'] < 100:
            if this.condition('hp100'):
                this.fullhp = 1

    def s2_proc(this, e):
        this.afflics.bog.on('s2', 80+this.fullhp*40)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

