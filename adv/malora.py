import adv_test
import adv

def module():
    return Malora

class Malora(adv.Adv):
    conf = {
            'mod_a':('att','bp',0.2*0.15),
            }
    def s2_proc(this, e):
        adv.Buff('armorbreak',-0.04,10,'def').on()  

    def condition(this):
        this.conf['acl'] = """
            `s1,fsc
            `s2,fsc
            `s3,fsc
            `fs,seq=1
            """
        return 'spawn c1+fs'




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        """
    adv_test.test(module(), conf, verbose=0)
