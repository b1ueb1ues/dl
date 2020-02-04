import adv.adv_test
from slot.d import *
from slot.a import *
import adv.chelsea

def module():
    return Chelsea

class Chelsea(adv.chelsea.Chelsea):

    def d_slots(this):
        this.slots.d = Dreadking_Rathalos()
        this.slots.a = The_Lurker_in_the_Woods()+Dear_Diary()

    def d_acl(this):
        this.conf['acl'] = """
            `s3,not this.s3_buff_on
            `s2,fsc
            `dodge, fsc
            `fs
        """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)