if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import linyou
import slot.d.wind 

def module():
    return Linyou_best

class Linyou_best(linyou.Linyou):
    name = 'Linyou'
    comment = '2in1 ; Zephyr'

    def init(this):
        pass

                              


if __name__ == '__main__':
    conf = {}
    # a better acl, but hit threshold of lose one s3.
    conf['acl'] = """
        `s2, s1.charged>=s1.sp-440
        `s1
        `s2, seq=4
        `s3, seq=5
        """

    adv_test.test(module(), conf, verbose=0, mass=0)

