import adv_test
import adv

def module():
    return Ranzal

class Ranzal(adv.Adv):
    comment = 'do not use fs'
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

