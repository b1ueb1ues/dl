import adv_test
import adv

def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {
        "mod_a"  : ('s'   , 'passive' , 0.4) ,
        'condition':'hp100'
        } 

    def init(this):
        this.charge("prep", "100%")
        this.s1buff = adv.Buff('armorbreak',(1.0/0.95-1)/2,10)

    def s1_proc(this, e):
        this.s1buff.on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

