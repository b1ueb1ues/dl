if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Luca

class Luca(adv.Adv):
    a1 = ('a',0.13,'hp100')
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """

    def s1_proc(this, e):
        this.afflics.paralysis('s1',110,0.883)



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)
