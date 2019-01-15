import adv_test
import adv

def module():
    return Marty

class Marty(adv.Adv):
    conf = {
            'mod_a':('sp','passive',0.05),
            }


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

