if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
import slot

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'no s2'
    a1 = ('cc',0.08,'hp100')
<<<<<<< HEAD
    conf['acl'] = """
        `s1
        `s3
    """
    conf['slots.a'] = slot.a.HG()+slot.a.RR()
    # conf['slots.d'] = slot.d.Hastur()
=======

    conf = {}
    conf['slots.a'] = slot.a.HG()+slot.a.FWHC()
    conf['slots.d'] = slot.d.Zephyr()
>>>>>>> 68c8187458e8944fa9781dcd1b9375d898f912c6


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

