import adv_test
import adv

def module():
    return Rodrigo

class Rodrigo(adv.Adv):
    def condition(this):
        this.conf['mod_a'] = ('att' , 'passive', 0.08)
        return 'hp70'


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

