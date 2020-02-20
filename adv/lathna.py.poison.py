import adv.adv_test
import adv.lathna
from slot.a import *

def module():
    return Lathna

class Lathna(adv.lathna.Lathna):
    comment = ''
    conf = adv.lathna.Lathna.conf.copy()
    conf['sim_afflict.time'] = 180
    conf['sim_afflict.type'] = 'poison'
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        # s1a = this.s1a
        `dragon
        `s1a
        `s2, seq = 5
        `s3, seq = 5
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)