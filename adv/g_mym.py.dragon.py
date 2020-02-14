import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *
import adv.g_mym

def module():
    return adv.g_mym.G_Mym

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)