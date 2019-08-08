if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test

import adv

def module():
    return Nicolas

class Nicolas(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

