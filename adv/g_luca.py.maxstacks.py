import adv.adv_test
from slot.a import The_Wyrmclan_Duo, Primal_Crisis
import adv.g_luca

def module():
    return G_Luca

class G_Luca(adv.g_luca.G_Luca):
    comment = '7 buff icons from team (buff value not considered); use VC/FitF if HP<70'
    conf = adv.g_luca.G_Luca.conf
    conf['slot.a'] = The_Wyrmclan_Duo()+Primal_Crisis()

    def buff_icon_count(this):
        return 7

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)