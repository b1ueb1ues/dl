import adv_test
import adv

def module():
    return Luca

class Luca(adv.Adv):
    def init(this):
        this.dmg_make("o_s1_paralysis",2.65)
        this.dmg_make("o_s1_paralysis",2.65)
        this.dmg_make("o_s1_paralysis",2.65)

    def condition(this):
        this.conf['mod_a'] = ('att' , 'passive' , 0.13) 
        this.conf['acl'] = """
            `s1, fsc
            `s2, fsc
            `s3, fsc
            `fs, seq=4
            """
        return 'hp100 & c4+fs'



if __name__ == '__main__':
    module().comment = 'paralysis 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
