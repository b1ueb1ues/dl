import adv_test
import adv

def module():
    return Karl

class Karl(adv.Adv):
    conf = {}
    conf['mod_a3'] = ('att' , 'passive', 0.08, 'hp70')
    #conf['mod_wp2'] = ('buff' , 'time', 0.15)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=-2)

