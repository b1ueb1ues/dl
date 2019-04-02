import adv_test
import adv

def module():
    return Xania

class Xania(adv.Adv):
    comment = 'reach 100 resist with Saintly Delivery'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42

    conf = {
        "mod_a1": ("s", 'passive', 0.20) ,
    } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

