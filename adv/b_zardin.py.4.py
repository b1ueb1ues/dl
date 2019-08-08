if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from adv import *
from module import energy
import b_zardin
from slot.a import *
import slot.w

def module():
    return B_Zardin

class B_Zardin(b_zardin.B_Zardin):
    pass



if __name__ == '__main__':
    conf = {}
    module().comment = 'with s2 & 4t3'
    conf['slots.w'] = slot.w.blade4b2()
    conf['slots.a'] = RR() + JotS()  
    conf['acl'] = """
        `s3, this.energy() = 5
        `s1
        `s2, seq=5 and this.energy() < 4
        """

    adv_test.test(module(), conf, verbose=0)


