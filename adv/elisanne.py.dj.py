import adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = 'Dragonyule Jeanne; no s2 or s3'
    a1 = ('bt',0.25)

    conf = {}
    conf['slots.a'] = BB() + JotS()
    conf['slots.d'] = DJ()
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf['acl'] = """
                        `s1
                        """
        else:
            self.conf['acl'] = """
                        `s1
                        `fs, seq=5
                        """


if __name__ == '__main__':
    adv.adv_test.test(module(), conf)
