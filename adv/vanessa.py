import adv.adv_test
import adv

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = ''
    a1 = ('fs',0.4)
    a3 = ('lo',0.3)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3, seq=4
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

