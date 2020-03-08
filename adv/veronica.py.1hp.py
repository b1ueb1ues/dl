import adv.adv_test
import adv.veronica
import slot
from slot import *


def module():
    return Veronica

class Veronica(adv.veronica.Veronica):

    conf = adv.veronica.Veronica.conf.copy()
    conf['acl'] = """
        `s1
        `s3, seq=5 and cancel
        `fs, seq=5 and s1.charged >= 2500
    """

    def prerun(self):
        super().prerun()
        self.hp = 0


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

