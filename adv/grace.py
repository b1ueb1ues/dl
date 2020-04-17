from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Grace

class Grace(Adv):
    a1 = ('fs',0.30)

    conf = {}
    conf['slots.a'] = The_Lurker_in_the_Woods()+Dear_Diary()
    conf['acl'] = """
        `s1
        `s2
        `s3
    """

    def prerun(self):
        conf_fs_alt = {
            'fs.dmg': 0.382,
            'fs.sp': 800,
            'fs.charge': 1.7999999523162842,
            'fs.startup': 0.7333333492279053,
            'fs.recovery': 0.6,
            'fs.hit': -1,
        }
        self.conf += Conf(conf_fs_alt)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)