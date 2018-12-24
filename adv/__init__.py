from core.timeline import *
from core.log import *
import core.acl


class Buff(object):
    def __init__(this, name=None, value=None, duration=None):
        this._value = 0
        this.duration = 0
        this.name = "buff_noname"
        if name != None:
            this.name = name
        if value != None:
            this._value = value
        if duration != None:
            this.duration = duration
        this.active = 0
        this.buff_end_event = Event("buff",this.buff_end_proc)

    def value(this):
        if this.active:
            return this._value
        else:
            return 1
    def get(this):
        if this.active:
            return this._value
        else:
            return 1

    def set(this, v):
        this._value = v
        return this

    def buff_end_proc(this, e):
        log("buff", this.name, this.value(), this.name+" buff end <timeout>")
        this.active = 0


    def on(this, duration=None):
        if duration == None:
            d = this.duration
        else:
            d = duration
        this.active = 1
        this.buff_end_event.on(now()+d)
        log("buff", this.name, this.value(), this.name+" buff start <%ds>"%d)
        return this


    def off(this):
        log("buff", this.name, this.value(), this.name+" buff end <turn off>")
        this.active = 0
        this.buff_end_event.off()
        return this


class Skill(object):
    charged = 0
    sp = 0
    duration = 1.9
    silence = [0]
    def __init__(this, name=None, sp=None, duration=None, ac=None):
        this.charged = 0
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
        if duration :
            this.duration = duration
        this.silence[0] = 0
        this.silence_end = Event("silence",this.restore)
        this.init()

    def __call__(this):
        return this.cast()


    def init(this):
        pass


    def charge(this,sp):
        this.charged += sp
        #if this.charged > this.sp:
            #this.charged = this.sp

    def restore(this, e):
        this.silence[0] = 0
        Event("silence_end").trigger()


    def check(this):
        if this.sp == 0:
            return 0
        elif this.silence[0] == 1:
            return 0
        elif this.charged >= this.sp:
            return 1
        else:
            return 0

    def cast(this, duration=None):
        if not this.check():
            return 0
        else:
            this.charged = 0
            if duration == None:
                duration = this.duration
            # Even if animation is shorter than 1.9, you can't cast next skill before 1.9
            if duration > 1.9:
                duration = 1.9
            this.silence_end.on(now()+this.duration)
            this.silence[0] = 1
            this.ac()
            return 1

    def ac(this):
        Event(this.name).trigger()

class Adv(object):
    x_status = (0,0)
    conf = {}

    conf_default = { 
            "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05},

            "s1_dmg"  : 0   ,
            "s1_sp"   : 0   ,
            "s1_time" : 1.9 ,

            "s2_dmg"  : 0   ,
            "s2_sp"   : 0   ,
            "s2_time" : 1.9 ,

            "s3_dmg"  : 0   ,
            "s3_sp"   : 0   ,
            "s3_time" : 1.9 ,
            }

    conf_default['acl'] = """
        `s1
        `s2
        `s3
    """

    acl_prepare_default = """
        #pin=e.pin
        #x=0
        #s=0
        #sx=0
        #sp=0
        #cancel=0
        #if pin == 'x': \n    x=1\n    cancel=1\n    x_cancel=1
        #if pin == 'fs':\n    fs=1\n    cancel=1\n    fs_cancel=1
        #if pin == 's': s=this.s_prev
        #if pin == 's-x': sx=this.s_prev
        #if pin == 'sp': sp=1
        #s1=this.s1.cast
        #s2=this.s2.cast
        #s3=this.s3.cast
        #fs=this.fs
        #seq = this.x_status[0]
    """
    def __init__(this,conf):
        this.log = []
        loginit(this.log)
        tmpconf = {}
        tmpconf.update(this.conf_default)
        tmpconf.update(this.conf)
        tmpconf.update(conf)
        this.conf = tmpconf
        this.s1 = Skill("s1",this.conf["s1_sp"])
        this.s2 = Skill("s2",this.conf["s2_sp"])
        this.s3 = Skill("s3",this.conf["s3_sp"])
        this.doing = "idle"
        this.done = "idle"

        if this.conf['x_type']== "ranged":
            this.x = this.range_x
            this.fs_success = this.range_fs_sucess
        elif this.conf['x_type']== "melee":
            this.x = this.melee_x
            this.fs_success = this.melee_fs_success
        #this.fs_success = this.melee_fs_success


    def dmg_mod(this, name):
        if name[0] == 's':
            return this.dmg_mod_s(name)
        elif name[0:2] == 'fs':
            return this.dmg_mod_fs(name)
        elif name[0] == 'x':
            return this.dmg_mod_x(name)
        else:
            return 1

    def dmg_mod_s(this, name):
        return 1
    def dmg_mod_fs(this, name):
        return 1
    def dmg_mod_x(this, name):
        return 1
    def att_mod(this):
        return 1
    def speed(this):
        return 1
    def arm_mod(this):
        return 1
    def sp_mod(this, name):
        return 1
    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass
    def fs_proc(this, e):
        pass
    def dmg_proc(this, name, amount):
        pass
    def init(this): 
        pass






    def run(this, d = 300):
        Timeline().reset()
        this.x_next = Event("x", this.ac).on()
        this.x_prev = 0
        this.s_prev = 0
        this.fs_hold = Event("fs_success", this.fs_success)
        this.first_x_after_s = 0
        this.x_status = (0,0)
        Event("s1").listener(this.s)
        Event("s2").listener(this.s)
        Event("s3").listener(this.s)
        Event("silence_end").listener(this.think_after_s)

        this.think = this.think3

        this.init()

        this.__acl, this.__acl_str = core.acl.acl_func_str(this.acl_prepare_default+this.conf['acl'])

        Timeline().run(d)


    def think_pin(this, pin):
        if pin in this.conf['think_latency'] :
            latency = this.conf['think_latency'][pin]
        else:
            latency = this.conf['think_latency']['default']
        e = Event('think', this.think).on(now() + latency).pin = pin

    def think_after_s(this, e):
        if this.s1.silence[0] == 1:
            this.think_pin("s")
            this.first_x_after_s = 1
        else :
            this.think_pin("s-x")
            this.think_pin("s")


    def think(this, e):
        pass

    def think3(this, e):
        this.__acl(this, e)


    def charge(this, name, sp): #, percent=None):
        if type(sp) == str and sp[-1] == '%':
            percent = int(sp[:-1])
            this.s1.charge(this.conf['s1_sp']*percent/100)
            this.s2.charge(this.conf['s2_sp']*percent/100)
            this.s3.charge(this.conf['s3_sp']*percent/100)
            log("sp", name, "%d%%   "%percent,"%d/%d, %d/%d, %d/%d"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )
            this.think_pin("prep")
            return
        sp = sp * this.sp_mod(name)
        this.s1.charge(sp)
        this.s2.charge(sp)
        this.s3.charge(sp)
        this.think_pin("sp")
        log("sp", name, sp,"%d/%d, %d/%d, %d/%d"%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )


    def dmg_formula(this, name, dmg_p):
        att = 1.0 * this.att_mod()
        arm = 10.0 * this.arm_mod()
        #return 5.0/3 * dmg_p * this.dmg_mod(name) * att/arm   # true formula 
        return att * dmg_p * this.dmg_mod(name) /10



    def dmg_make(this, name, dmg_p):
        count = this.dmg_formula(name, dmg_p)
        
        if name[0] == "x":
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (+%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        elif name[:2] == "fs":
            spgain = this.conf['fs'+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (+%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        else:
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (-%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        this.dmg_proc(name, count)


    def missile(this,e):
        this.dmg_make(e.name, e.amount)
        this.charge(e.name, e.samount)


    def ac(this, e):
        this.x()


    def range_x(this):
        if this.x_status[1] == 0 :
            time = float(this.conf["x1_startup"]) / this.speed()
            this.x_next.timing += time
            if this.x_status[0] == 0:
                this.think_pin('s')
            this.x_status = (0, 1)
            return

        seq = this.x_status[1]
        dmg = this.conf["x%d_dmg"%seq] 
        sp = this.conf["x%d_sp"%seq] 
        e = Event("x%d_missile"%seq, this.missile, \
                now() + this.conf['missile_iv'][seq] )
        e.amount = dmg
        e.samount = sp
        e.on()

        if seq == 5:
            log("x", "x%d"%seq, 0,"-------------------------------------c5")
        else:
            log("x", "x%d"%seq, 0)

        this.think_pin("x")
        if this.first_x_after_s:
            this.think_pin("s-x")
            this.first_x_after_s = 0

        if seq == 5:
            this.doing = "x5_recover"
            this.x_status = (5, 0)
            time = float(this.conf["x5_recovery"]) / this.speed()
        else:
            this.doing = "x%d"%(seq+1)
            this.x_status = (seq, seq+1)
            time = float(this.conf["x%d_startup"%(seq+1)]) / this.speed()
        this.done = "x%d"%seq
        this.x_prev = now()
        this.x_next.timing += time


    def melee_x(this):
        if this.x_status[1] == 0 :
            time = float(this.conf["x1_startup"]) / this.speed()
            this.x_next.timing += time
            if this.x_status[0] == 0:
                this.think_pin('s')
            this.x_status = (0, 1)
            return

        seq = this.x_status[1]
        dmg_p = this.conf["x%d_dmg"%seq]
        sp = this.conf["x%d_sp"%seq] 
        if seq == 5:
            log("x", "x%d"%seq, 0,"-------------------------------------c5")
        else:
            log("x", "x%d"%seq, 0)

        this.dmg_make("x%d"%seq, dmg_p)
        this.charge("x%d"%seq, sp)

        this.think_pin("x")
        if this.first_x_after_s:
            this.think_pin("s-x")
            this.first_x_after_s = 0

        if seq == 5:
            this.doing = "x5_recover"
            this.x_status = (5, 0)
            time = float(this.conf["x5_recovery"]) / this.speed()
        else:
            this.doing = "x%d"%(seq+1)
            this.x_status = (seq, seq+1)
            time = float(this.conf["x%d_startup"%(seq+1)]) / this.speed()
        this.done = "x%d"%seq
        this.x_prev = now()
        this.x_next.timing += time



    def melee_fs_success(this, e):
        log("fs","succ",0)
        dmg_p = this.conf["fs_dmg"]
        this.dmg_make("fs", dmg_p)
        this.charge("fs",this.conf["fs_sp"])
        this.fs_proc(e)
        this.x_status = (-1, 0)
        this.think_pin("fs")
        this.done = "fs"
        this.doing = "fs_recover"


    def range_fs_sucess(this, e):
        log("fs","succ",0)
        dmg_p = this.conf["fs_dmg"]
        sp_gain = this.conf["fs_sp"]
        missile_event = Event("fs_missile", this.missile, 
                now() + this.conf['missile_iv'][0] )
        missile_event.amount = dmg_p
        missile_event.samount = sp_gain
        missile_event.on()
        this.fs_proc(e)
        this.x_status = (-1, 0)
        this.think_pin("fs")
        this.done = "fs"
        this.doing = "fs_recover"

    def fs(this):
        seq = this.x_status[0]
        if seq != 0:
            time = now() - this.x_prev
            log("cancel", "x%d"%seq , time)

        if seq != 0:
            log("fs", 'hold', 0,"                               (hold fs after c%s)"%( seq ) )
        else:
            log("fs", 'hold', 0,"                               (hold fs)" )

        this.x_next.timing = now() + (this.conf["fs_startup"] + this.conf["fs_recovery"]) / this.speed()
        this.fs_hold.on(now()+this.conf['fs_startup'])

        this.x_status = (-1, 0)
        this.doing = "fs_hold"
        return 1



    def s(this, e):
        seq = this.x_status[0]
        if seq == -1:
            time = this.conf['fs_recovery'] - (this.x_next.timing - now())
            log("cancel", "fs" , time)
        elif seq != 0:
            time = now() - this.x_prev
            log("cancel", "x%d"%seq , time)

        if seq == -1:
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after fs)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name) )
        elif seq != 0:
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after c%s)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, seq ) )
        else:
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after s%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, this.s_prev ) )

        this.x_next.timing = now() + this.conf[e.name+"_time"] / this.speed()
        dmg_p = this.conf[e.name+"_dmg"]
        if dmg_p :
            this.dmg_make(e.name , dmg_p)

        func = e.name + '_proc'
        getattr(this, func)(e)

        this.s_prev = int(e.name[1])
        this.x_status = (0, 0)
        this.done = e.name
        this.doing = e.name + "_recover"



if __name__ == "__main__":
    print "to use adv_test"

