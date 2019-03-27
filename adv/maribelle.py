import adv_test
import adv

def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {}
    conf['mod_a1'] = ('s', 'passive', 0.4, 'hp100')

    def init(this):
        this.charge_p("prep", "100%")



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

