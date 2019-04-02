import adv_test
import adv

def module():
    return Jurota

class Jurota(adv.Adv):
    conf = {}
    conf['mod_a1'] = ('att','bp',0.2*0.45)
    comment = 'reach 100 resist with Saintly Delivery'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42




if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

