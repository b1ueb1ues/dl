if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv
from slot.a import *
import louise

def module():
    return Louise

class Louise(louise.Louise):

    def init(this):
        this.conf.mod = {'ex':('sp','passive',0.15)}
        this.conf['slot.a'] = FB()+SS()
        if this.condition('rollfs'):
            this.conf['acl'] = """
                `s1,fsc
                `s2,fsc
                `s3,fsc
                `dodge, fsc
                `fs
                """
        else:
            this.conf['acl'] = """
                `s1
                `s2
                `s3
                """


if __name__ == '__main__':
    conf = {}
    from slot.d import *
    conf['slot.d'] = Pazuzu()
    adv_test.test(module(), conf, verbose=0)
