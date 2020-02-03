import adv.adv_test
import adv.veronica
import slot
from slot import *


def module():
    return Veronica

class Veronica(adv.veronica.Veronica):
    def d_acl(this): 
        this.conf['acl'] = """
            `s1
            `s3, seq=5 and cancel
            `fs, seq=5 and s1.charged >= 2500
        """

    def prerun(this):
        super().prerun()
        this.hp = 0


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

