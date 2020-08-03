from core.advbase import *
from slot.a import The_Wyrmclan_Duo, Primal_Crisis
import adv.gala_luca

def module():
    return Gala_Luca

class Gala_Luca(adv.gala_luca.Gala_Luca):
    comment = '7 buff icons from team (buff value not considered); use VC/FitF if HP<70'
    conf = adv.gala_luca.Gala_Luca.conf.copy()
    conf['slots.a'] = The_Wyrmclan_Duo()+Primal_Crisis()

    def buff_icon_count(self):
        return 7


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Gala_Luca, *sys.argv)