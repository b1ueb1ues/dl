import adv_test
import adv

def module():
    return Julietta

class Julietta(adv.Adv):
    comment = 'do not use weapon skill and fs'
    conf = {
        'mod_wp': [
            ('s','passive',0.15),
            ('crit','rate',0.12),
        ],
    }
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        """
    adv_test.test(module(), conf, verbose=0)

