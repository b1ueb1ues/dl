import adv_test
import adv

def module():
    return Karl

class Karl(adv.Adv):
    conf = {}
    conf['mod_wp'] = [
            ('s','passive',0.10),
            ('fs','passive',0.20),
            ]
    def condition(this):
        this.conf['mod_a'] = ('att' , 'passive', 0.08)
        return 'hp70'



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

