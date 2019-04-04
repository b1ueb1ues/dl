import adv_test
import adv

def module():
    return Marty

class Marty(adv.Adv):
    conf = {
        'mod_a1':('sp','passive',0.05),
    }
    comment = 'reach 100 resist with Saintly Delivery'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

