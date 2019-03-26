import adv_test
import adv

def module():
    return Karl

class Karl(adv.Adv):
    def pre(this):
        if this.condition('hp70'):
            this.conf['mod_a'] = ('att' , 'passive', 0.08)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

