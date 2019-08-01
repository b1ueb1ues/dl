import adv_test
import adv
import louise

def module():
    return Louise

class Louise(louise.Louise):

    def prerun(this):
        super(Louise, this).prerun()
        this.conf.rotation = """
fs d 
fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d -------- s2 fs d -------- s1 fs d 
fs d 
fs d -------- s3 fs d 
fs d -------- s1 fs d 
fs d 
fs d -------- s2 fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s3 fs d -------- s2 fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d -------- s3 fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d -------- s3 fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d -------- s3 fs d 
fs d 
fs d -------- s1 fs d 
fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s3 fs d 
fs d 
fs d 
fs d -------- s1 fs d -------- s2 fs d
        """






if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `rotation
        """
    from slot.a import *
    conf['slots.a'] = Stellar_Show() + Forest_Bonds()
    adv_test.test(module(), conf, verbose=0)




['fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 's2', 's1', 'fs', 'fs', 'fs', 'fs', 's3', 'fs', 'fs', 's1', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's3', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs']


['fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 's2', 's1', 'fs', 'fs', 'fs', 'fs', 's3', 'fs', 'fs', 's1', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's3', 'fs', 'fs', 's2', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's3', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2', 's3', 'fs', 'fs', 'fs', 'fs', 's1', 'fs', 'fs', 'fs', 'fs', 'fs', 'fs', 's1', 's2']
