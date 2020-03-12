import adv.adv_test
import adv.lathna
from slot.a import *
import sys

def module():
    return Lathna

class Lathna(adv.lathna.Lathna):
    comment = ''
    conf = adv.lathna.Lathna.conf.copy()
    conf['sim_afflict.time'] = 180
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `s3, not self.s3_buff
        `dragon
        `s1a
        `s2, x=5
        """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)