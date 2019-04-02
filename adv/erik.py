import adv_test
import adv

def module():
    return Erik

class Erik(adv.Adv):
    comment ='do not use weapon skill'
    conf = {
        "mod_a1": ('fs', 'passive', 0.30),
        } 
    comment += '& reach 100 resist with Silke Lends a Hand'
    conf['mod_wp2'] = ('s','passive',0.1)
    conf['str_wp2'] = 42



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,fsc
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

