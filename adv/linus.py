import adv_test
import adv

def module():
    return Linus

class Linus(adv.Adv):
    comment = 'do not use weapon skill'
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

