import adv_test
import adv

def module():
    return Althemia

class Althemia(adv.Adv):
    a1 = ('s',0.3,'hp100')

   # import slot
   # conf = {}
   # conf['slot.d'] = slot.d.Shinobi()


if __name__ == '__main__':
    conf = {}

    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s3
        `s2, s=1
        """
    adv_test.test(module(), conf)

