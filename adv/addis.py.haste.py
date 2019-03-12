import adv_test
import addis
from module.bleed import Bleed

def module():
    return Addis

class Addis(addis.Addis):
    pass

if __name__ == '__main__':
    ## too hard to do that (still possible)
    #module().comment = 'with 20% skill haste'
    #conf = {
    #        'mod_wp':[('s','passive',0.25),
    #                  ('sp','passive',0.05)],
    #        'mod_ex':('sp','passive',0.15)
    #        }
    #conf['acl'] = """
    #    `s2, s1.charged>=2537 and seq=5
    #    `s1, s2.charged<4877 
    #    `s3, this.s2buff.get()==0
    #    """
    #adv_test.test(module(), conf,verbose=0, mass=1)

# just a little down to acl before
    conf = {
            'mod_wp':[('s','passive',0.25),
                      ('sp','passive',0.05)],
            'mod_ex':('sp','passive',0.15)
            }
    module().comment = 'with 20% skill haste'
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-260 and seq=5
        `s1, s2.charged<s2.sp
        `s3, not this.s2buff.get()
        `fs, this.s2buff.get() and seq=5
        """
    adv_test.test(module(), conf,verbose=0, mass=1)


