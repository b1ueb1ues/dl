import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Julietta

class Julietta(Adv):
    comment = 'no fs & no s2'

    def s2_proc(self, e):
       adv.Event('defchain')()

    conf = {}
    conf['slot.a'] = KFM()+FitF()
    conf['acl'] = """
        `s1
        `s3,seq=5
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)