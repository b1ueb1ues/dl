import adv_test
from core.advbase import *
from slot.a import *
import naveed

def module():
    return Naveed

class Naveed(naveed.Naveed):
    def prerun(this):
        this.s1level = 5

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

