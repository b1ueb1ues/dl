import adv_test
import adv

def module():
    return Marty

class Marty(adv.Adv):
    comment = 'do not use weapon skill'
    conf = {
            'mod_a':('sp','passive',0.05),
            }


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

