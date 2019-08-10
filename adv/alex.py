if __name__ == '__main__':
    import adv_test
    from adv_test import sim_duration
else:
    import adv.adv_test
    from adv.adv_test import sim_duration
import adv
from slot.d import *

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)

    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    def d_slots(this):
        if sim_duration == 120:
            conf['acl'] = """
                `rotation
            """
            conf['rotation'] = """
                C4FS C5- S1 C4FS C5- S1 C1- S2 C4FS C5- S1 C5- S3 C5- S1
                C5- S2 C5- S1 C4FS C5- S1 C4FS C2- S2 C2- S3 C3- S1
            """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)


