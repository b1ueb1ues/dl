import adv_test
from adv import *
from slot.a import *
from slot.d import *
import g_luca

def module():
    return G_Luca

class G_Luca(g_luca.G_Luca):
    comment = '7 buff icons from team (buff value not considered); use VC/FitF if HP<70'

    def d_slots(this):
        this.slots.a = The_Wyrmclan_Duo()+Primal_Crisis()

    def buff_icon_count(this):
        return 7

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2, mass=0)

