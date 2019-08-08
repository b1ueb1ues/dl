import adv.adv_test
from adv import *

def module():
    return Norwin

class Norwin(Adv):

    def prerun(this):
        if this.condition('80 resist'):
            this.afflics.blind.resist=80
        else:
            this.afflics.blind.resist=100

        #this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        #this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        #this.dmg_make("o_s2hitblind",(4.035-2.69)*3)
        #adv.Teambuff('a1', 0.10,10*3).on()
        #adv.Selfbuff('blind killer', 0.20,8*3,'att','killer').on()

        this.m = Modifier('pkiller','att','killer',0.2)
        this.m.get = this.getbane

    def getbane(this):
        return this.afflics.blind.get()*0.2


    def s1_proc(this, e):
        this.afflics.blind('s1',100)
        Teambuff('a1',0.15*this.afflics.blind.get(),10).on()


    def s2_before(this, e):
        r = this.afflics.blind.get()
        coef = 3 * 2.45 * (1-r)
        return coef

    def s2_proc(this, e):
        r = this.afflics.blind.get()
        coef = 3 * 2.45 * r
        this.dmg_make('s2',coef)
        coef = 3 * (3.528-2.45) * r
        this.dmg_make('o_s2_boost',coef)





if __name__ == '__main__':
    module().comment = 'blind 3 times & c5+fs'
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
