import adv_test
import adv

def module():
    return Alex

class Alex(adv.Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel 
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0)


