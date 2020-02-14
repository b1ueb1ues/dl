import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
import laranoa

def module():
    return Laranoa

class Laranoa(laranoa.Laranoa):
    comment = 'doesn\'t count spbuff for teammates; roll fs'

    conf = {}
    conf['slot.d'] = Siren()

    def d_acl(this):
        this.conf['acl'] = """
            `s3,s1.charged>=s1.sp
            `s1,fsc
            `s2,fsc
            `dodge, fsc
            `fs
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)


