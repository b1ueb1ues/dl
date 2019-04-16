import adv_test
import adv

def module():
    return Maribelle

class Maribelle(adv.Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('prep','100%')

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

    adv_test.test(module(), conf, verbose=0)

