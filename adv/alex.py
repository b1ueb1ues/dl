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
    conf['slot.d'] = Shinobi()

    def prerun(this):
        if this.condition('0 resist'):
            this.afflics.poison.resist=0
        else:
            this.afflics.poison.resist=100

    def s1_proc(this, e):
        this.afflics.poison('s1',100,0.396)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    import sys
    from slot.a import *
    if len(sys.argv) >= 3:
        sim_duration = int(sys.argv[2])
    else:
        sim_duration = 180

    if sim_duration == 120:
        conf['acl'] = """
            `rotation
        """
        conf['rotation'] = """
            C4FS C5- S1 C4FS C5- S1 C1- S2 C4FS C5- S1 C5- S3 C5- S1
            C5- S2 C5- S1 C4FS C5- S1 C4FS C2- S2 C2- S3 C3- S1
        """

    adv_test.test(module(), conf, verbose=0)


