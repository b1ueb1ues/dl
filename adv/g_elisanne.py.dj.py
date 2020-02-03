import adv_test
from adv import *
from slot.d import *
from slot.a import *
import g_elisanne

def module():
    return G_Elisanne

class G_Elisanne(g_elisanne.G_Elisanne):

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
    adv.adv_test.test(module(), conf, verbose=-2)

