import adv_test
import adv

def module():
    return Melody

class Melody(adv.Adv):
    def condition(this):
        this.conf['mod_a'] = ('crit' , 'passive', 0.08)
        return 'hp100'



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

