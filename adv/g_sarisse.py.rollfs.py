from slot.a import *
from slot.d import *
import adv.g_sarisse

def module():
    return Gala_Sarisse

class Gala_Sarisse(adv.g_sarisse.Gala_Sarisse):
    comment = 'roll fs'
    conf = {}
    conf['slots.d'] = Dreadking_Rathalos()
    conf['acl'] = """
        `s3, fsc and not self.s3_buff
        `s1, fsc
        `s2, fsc
        `dodge, fsc
        `fs
    """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Gala_Sarisse, *sys.argv)
