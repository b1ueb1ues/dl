import adv_test
import linyou

def module():
    return Linyou_best

class Linyou_best(linyou.Linyou):
    adv_name = 'Linyou'
    comment = 'Kunfu & LongLong'
    conf = {
        "mod_a2"  : ('sp' , 'passive'  , 0.08) ,
        "mod_d" :[
            ('att','passive',0.45),
            ('crit','dmg',0.55),
            ],
        }


if __name__ == '__main__':
    conf = {}
    # a better acl, but hit threshold of lose one s3.
    module().comment += '& cover 2 s1 in one s2'
    conf['acl'] = """                 
        `s2, s1.charged>=s1.sp-440
        `s1
        `s3, not this.s2ssbuff.get()
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

