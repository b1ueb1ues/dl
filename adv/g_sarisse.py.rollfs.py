import adv_test
import adv
from adv import *
import slot
from slot.a import *
from slot.d import *
import g_sarisse
def module():
    return G_Sarisse

class G_Sarisse(g_sarisse.G_Sarisse):
    def d_acl(this):
        this.conf['acl'] = """
            `s3, not this.s3_buff_on
            `s1,fsc
            `s2,fsc
            `dodge, fsc
            `fs
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

