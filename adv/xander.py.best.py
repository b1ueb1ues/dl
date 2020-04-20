import adv.xander
from slot.a import *
from slot.d import *

def module():
    return Xander

class Wily_Warriors_Metal_and_Quick(Amulet):
    att = 55
    a = [('sts',0.06),
         ('cd',0.22,'hp70')]


class Xander(adv.xander.Xander):
    comment = '10 stacks striker\'s strength'
    a1 = ('sts',0.06)
    conf = {}
    conf['slots.a'] = Wily_Warriors_Metal_and_Quick() + RR()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s2, fsc
        `s3, fsc
        `fs, x=2 and cancel
        """

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Xander, *sys.argv)

