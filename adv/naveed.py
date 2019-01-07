import adv_test
import adv

def module():
    return Naveed

class Naveed(adv.Adv):
    comment = 'with crown doublebuff'
    conf = {
        "mod_wp"  : ('s'   , 'passive' , 0.25) ,
        } 

    def init(this):
        this.s1level = 0
        this.charge('prep','100%')
        pass

    def s1_proc(this, e):
        this.dmg_make("s1_missile",3*this.s1level*0.28)


    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level > 5:
            this.s1level = 5
        adv.Buff("crown_double_buff",0.08,15,wide='self').on()
    


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2, sp
        `s1, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

