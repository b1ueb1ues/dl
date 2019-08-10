if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Ranzal

class Ranzal(adv.Adv):
    comment = 'do not use fs'
    conf = {}
    conf['acl'] = """
        `s1 
        `s3
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

