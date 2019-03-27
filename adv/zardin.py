import adv_test
import adv

def module():
    return Zardin

class Zardin(adv.Adv):
    conf = {}
    conf['mod_a1'] = ('att', 'passive', 0.10, 'hp100')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

