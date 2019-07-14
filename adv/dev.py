import adv_test
import adv
from slot.d import *

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)

    conf = {}
    conf['rotation'] = """
        c4fsc4fss1c
            """
    rotation_stat = 0

    def rotation(this):
        if not this.act_next:
            this.act_next = this.get_next_act()
        anext = this.act_next

        if anext[0] == 'c':
            if this.

        doing = this.action.getdoing()
        dname = doing.name
        dstat = doing.status
        didx = doing.index

        r = this.act_next()
        if r:
            this.act_next = 0
        return r


    def get_next_act(this):
        p = rotation_stat
        rt = this.conf.rotation



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
    """
    adv_test.test(module(), conf, verbose=0)


