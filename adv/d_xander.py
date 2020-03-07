import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Dragonyule_Xander

class Dragonyule_Xander(Adv):
    a3 = ('sp',0.05)
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel or s
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    conf['acl'] = acl12

    def prerun(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def s2_proc(self, e):
        self.energy.add(1, team=self.condition('buff all team'))
        self.buff_class('s2', 0.15, 10)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)


