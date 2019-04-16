import adv_test
import adv

def module():
    return Curran

class Curran(adv.Adv):
    comment = "do not use weapon skill and fs"
    a1 = ('od',0.13)
    a3 = ('lo',0.5)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        """
    adv_test.test(module(), conf, verbose=0)

