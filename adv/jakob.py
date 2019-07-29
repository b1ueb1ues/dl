import adv_test
import adv

def module():
    return Jakob

class Jakob(adv.Adv):

    def prerun(this):
        if this.condition('60 bog resist'):
            this.afflics.resist['bog'] = 60
        this.charge_p('prep','50%')
        this.bogbuff = adv.Debuff('s1_bog',-0.5,8,1,'att','bog')


    def s1_proc(this, e):
        if this.afflics.add('s1','bog',90,8):
            this.bogbuff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

