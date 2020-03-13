import adv.veronica
import slot
from slot import *


def module():
    return Veronica

class Veronica(adv.veronica.Veronica):

    conf = adv.veronica.Veronica.conf.copy()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `fs, (s1.charged>=s1.sp-self.sp_val('fs'))
    """

    def prerun(self):
        super().prerun()
        self.hp = 0

if __name__ == '__main__':
    import sys
    from core.simulate import test_with_argv
    test_with_argv(Veronica, *sys.argv)