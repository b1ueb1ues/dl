import adv_test
import adv


def module():
    return Celliera

class Celliera(adv.Adv):
    comment = 'RR+jewels_of_the_sun'
    a3 = ('a',0.08,'hp70')
    import slot
    conf = {}
    conf['slots.a'] = slot.a.RR() + slot.a.Jewels_of_the_Sun()
    #conf['slots.a'] = slot.a.RR() + slot.a.CE()


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
    adv_test.test(module(), conf, verbose=0)


