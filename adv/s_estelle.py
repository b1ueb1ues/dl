import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Summer_Estelle

class Summer_Estelle(Adv):
    a3 = ('bt',0.2)
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    conf['acl'] = acl12

    def init(self):
        if self.condition('buff all team'):
            self.s2_proc = self.c_s2_proc


    def c_s2_proc(self, e):
        Teambuff('s2',0.15,15).on()

    def s2_proc(self, e):
        Selfbuff('s2',0.15,15).on()



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


