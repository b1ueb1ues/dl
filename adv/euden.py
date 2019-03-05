import adv_test
import adv


def module():
    return Euden

class Euden(adv.Adv):
    def s2_proc(this, e):
        adv.Buff('armorbreak',1/0.955-1, 10, 'att','debuff').on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=3 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

