import adv_test
import adv

def module():
    return Althemia

class Althemia(adv.Adv):
    a1 = ('s',0.3,'hp100')

    import slot
    conf = {}
    conf['slot.d'] = slot.d.Shinobi()


if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        `s1
        `s2
        `s3
        """
    adv_test.test(module(), conf)

