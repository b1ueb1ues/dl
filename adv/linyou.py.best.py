import adv_test
import linyou
import slot.d.wind 

def module():
    return Linyou_best

class Linyou_best(linyou.Linyou):
    name = 'Linyou'
    comment = 'Kunfu & LongLong'

    def pre(this):
        this.conf['slots.d'] = slot.d.wind.Longlong()

                              


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

