import adv_test
from xander import *
from slot.a import *

def module():
    return Xander_best

class Together_We_Stand(Amulet):
    att = 52
    a = [('sts',0.05),
         ('s',0.20)]


class Xander_best(Xander):
    comment = '10 stacks striker\'s strength'
    name = 'Xander'
    a1 = ('sts',0.06)
    conf = {}
    conf['slots.a'] = Together_We_Stand() + RR()


    def s1_proc(this,e):
        this.dmg_make('s1_boost',this.conf['s1.dmg']*0.5)




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

    
    def foo(e):
        return
    module().a1 = None
    module().s1_proc = foo
    module().comment = 'only 2+1'
    conf['slots.a'] = Stellar_Show()+LC()
    conf['acl'] = """
        `fs, seq=2 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

