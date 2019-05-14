import adv_test
import adv

def module():
    return Norwin

class Norwin(adv.Adv):

    def init(this):
        this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        adv.Teambuff('a1', 0.10,10*3).on()
        adv.Selfbuff('blind killer', 0.20,8*3,'att','killer').on()




if __name__ == '__main__':
    module().comment = 'blind 3 times & c5+fs'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2)
