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
        self.a1_buff.on()

if __name__ == '__main__':
    import sys
    from core.simulate import test_with_argv
    test_with_argv(Veronica, *sys.argv)