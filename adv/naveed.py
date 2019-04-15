import adv_test
import adv

def module():
    return Naveed

class Naveed(adv.Adv):
    def init(this):
        this.s1level = 0
        this.charge_p('prep','100%')
        pass

    def s1_proc(this, e):
        this.dmg_make("s1_missile",3*this.s1level*0.28)


    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level >= 5:
            this.s2.sp = 0
            this.s1level = 5
        


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, sp 
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

