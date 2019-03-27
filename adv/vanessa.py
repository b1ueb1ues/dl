import adv_test
import adv

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = ''
    conf = {
        "mod_a": ('fs', 'passive', 0.40),
        } 
    def pre(this):
        if this.condition('last offense'):
            this.init = this.c_init

    def c_init(this):
        adv.Selfbuff('last_offense',0.3,15).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3, seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

