import adv.adv_test
from slot.d import *
import adv.chelsea

def module():
    return Chelsea

class Chelsea(adv.chelsea.Chelsea):

    def d_slots(this):
        this.slots.d = Dreadking_Rathalos()

    def d_acl(this):
        this.conf['acl'] = """
            `s3,not this.s3_buff_on
            `s1,fsc
            `s2,fsc
            `dodge, fsc
            `fs
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)