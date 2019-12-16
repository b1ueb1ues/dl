import adv_test
import adv
import slot

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'no s2'
    a1 = ('cc',0.08,'hp100')

    conf = {}
    conf['slots.a'] = slot.a.HG()+slot.a.FWHC()
    conf['slots.d'] = slot.d.Zephyr()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)

