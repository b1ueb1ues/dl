import adv_test
import adv

def module():
    return Pietro

class Pietro(adv.Adv):
    comment = 'unsuitable resist'
    conf = {}
    conf['mod_a1'] = ('crit','damage',0.13)

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s3,seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

