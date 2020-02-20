import adv_test
from core.advbase import *
from slot.d import *
from slot.a import *
import g_elisanne

def module():
    return Gala_Elisanne

class Gala_Elisanne(g_elisanne.Gala_Elisanne):

    conf = {}
    
    def d_slots(this):
        this.slots.a = BB()+KFM()
        this.slots.d = Leviathan()

    def d_acl(this):
        this.conf['acl'] = """
            `s1
            `s2, seq=4
            `fs, seq=5
            """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

