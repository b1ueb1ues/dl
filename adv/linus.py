if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv

def module():
    return Linus

class Linus(adv.Adv):
    # comment = 'do not use weapon skill'
    conf = {}
    conf['acl'] = """
        `s1 
        `s2
        `s3,seq=4
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

