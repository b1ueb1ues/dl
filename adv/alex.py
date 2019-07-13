import adv_test
import adv
from slot.d import *

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)


    #rotation = [1,1,2,3,1]
    #def act_get(this):



    #conf = {}
    #conf['slot.d'] = Shinobi()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    if 0:
        conf['acl'] = """
            #if this.s2.check(): this.tmp = 1
            #if s3.sp == 0: this.tmp = 0
            `s1, fsc
            `s2, seq=3 
            `s3, seq=1 and this.tmp==1
            `fs, seq=4
            """

    if 0:
        conf['acl'] = """
            `s1, seq=5 and cancel or fsc
            `s2, fsc
            `s3, seq=4 and cancel or fsc
            `fs, seq=4 and s1.charged - s1.sp < 288
            """

    adv_test.test(module(), conf, verbose=0)


