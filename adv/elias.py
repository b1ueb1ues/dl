import adv_test
import adv
from module import energy

def module():
    return Elias

class Elias(adv.Adv):
    def init(this):
        energy.Energy(this,{'s2':1},{'s2':1})

if __name__ == '__main__':
    conf = {}

    if 0:
        conf['acl'] = """
            `s1, seq=5 or fsc
            `s2, seq=5 or fsc
            `s3, seq=5 or fsc
            """
        adv_test.test(module(), conf, verbose=0)

    module().comment = 'spawn c1+fs; don not use s2'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)

    module().comment = 'spawn c1+fs;'
    conf['acl'] = """
        `s1, seq=5 or fsc
        `s2, seq=5 or fsc
        `s3, seq=5 or fsc
        `fs, seq=1
        """
    adv_test.test(module(), conf, verbose=0)
