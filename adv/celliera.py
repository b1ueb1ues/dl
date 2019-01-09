import adv_test
import adv


def module():
    return Celliera

class Celliera(adv.Adv):
    conf = {
        "mod_a": ('att' , 'passive', 0.08) ,
        "mod_d":[('att' , 'passive', 0.45) ,
                 ('crit', 'chance' , 0.20)],
        'condition':'hp70'
        } 


if __name__ == '__main__':
    conf = {}
    acl12 = """
        `s1
        `s2
        `s3
        """
    acl21 = """
        `s2
        `s1
        `s3
        """ 
    # test that 21 is better than 12
    if 0:
        conf['acl'] = acl12
        adv_test.test(module(), conf, verbose=0)
        exit()

    conf['acl'] = acl21
    adv_test.test(module(), conf, verbose=1)


