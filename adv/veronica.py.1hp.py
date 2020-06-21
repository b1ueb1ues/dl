import adv.veronica
import slot
from slot import *


def module():
    return Veronica

class Veronica(adv.veronica.Veronica):

    conf = adv.veronica.Veronica.conf.copy()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
    """

    def prerun(self):
        super().prerun()
        self.set_hp(0)

    def a1_buff_on(self, e):
        super().a1_buff_on(e)
        self.set_hp(0)

if __name__ == '__main__':
    import sys
    from core.simulate import test_with_argv
    test_with_argv(Veronica, *sys.argv)