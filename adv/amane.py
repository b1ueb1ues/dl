import adv_test
import adv
import wep.wand
from core.timeline import *
from core.log import *


def module():
    return Amane

class Amane(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 4.92*2   ,
        "s1_sp"   : 2711     ,
        "s1_time" : 1.8 , #108/60

        "s2_dmg"  : 0        ,
        "s2_sp"   : 11449     ,
        "s2_time" : 1.1 , #65/60

        "s3_dmg"  : 4*2.71   ,
        "s3_sp"   : 8597     ,
        "s3_time" : 1.9        , #117/60
        } )
    conf.update(wep.wand.conf)

    def s2_buff_end(this, e):
        this.buff["s2"] = 1
        log("buff","s2","end   ")


    def init(this):
        #!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!
        this.charge("prep","75%")
        this.s2buff = Event("s2buff",this.s2_buff_end)
        this.buff = {
                "s2":1,     #1.15 for 10s
                }

    def att_mod(this):
        return this.buff["s2"]


    def dmg_mod_s(this, name):
        return 1.11*1.25


    def s1_proc(this, e):
        pass


    def s2_proc(this, e):
        this.buff["s2"] = 1.15
        log("buff","s2","start   ")
        this.s2buff.on(now()+10)


    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        /s2, seq=5 and cancel
        /s1, seq=5 and cancel
        /s3
        """

    adv_test.test(module(), conf, verbose=0)

