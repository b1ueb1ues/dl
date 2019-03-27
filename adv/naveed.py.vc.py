import adv_test
import naveed
import adv

def module():
    return Naveed

class Naveed(naveed.Naveed):
    def s2_proc(this, e):
        this.s1level += 1
        if this.s1level > 5:
            this.s1level = 5
        adv.Selfbuff("crown_double_buff",0.08,15).on()
    


if __name__ == '__main__':
    conf = {}
    Naveed.comment = 'Valiant Crown'
    conf['acl'] = """
        `s1, sp
        `s2, sp
        `s3, sp
        `fs, seq=3 and cancel
        """
    conf['mod_wp'] = ('s', 'passive' , 0.25)
    adv_test.test(module(), conf, verbose=0)



