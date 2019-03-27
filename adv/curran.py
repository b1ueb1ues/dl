import adv_test
import adv

def module():
    return Curran

class Curran(adv.Adv):
    comment = "do not use weapon skill and fs"
    conf = {
        "mod_a": ('att', 'killer', 0.13*0.45),
        } 

    def init(this):
        if this.condition('last_offense'):
            adv.Selfbuff('last_offense',0.5,15).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        """
    adv_test.test(module(), conf, verbose=0)

