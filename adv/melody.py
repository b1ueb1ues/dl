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

    conf = {}
    conf['slots.a'] = slot.a.HG()+slot.a.FWHC()
    conf['slots.d'] = slot.d.Zephyr()


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

