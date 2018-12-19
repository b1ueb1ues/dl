from core.timeline import *
from core.log import *



class Skill(object):
    charged = 0
    sp = 0
    def __init__(this, name=None, sp=None, ac=None):
        this.charged = 0
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
        this.init()


    def init(this):
        pass


    def charge(this,sp):
        this.charged += sp
        #if this.charged > this.sp:
            #this.charged = this.sp

    def check(this):
        if this.charged >= this.sp:
            return 1
        else:
            return 0

    def cast(this):
        if not this.check():
            return 0
        else:
            this.charged = 0
            this.ac()
            return 1

    def ac(this):
        Event(this.name).trigger()

class Adv(object):
    x_status = (0,0)
    conf = {}

    conf_default = { 
            "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05}
            }

    conf_default['al'] = {
        'sp': [],
        'x5': [],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        's': [],
        }

    def __init__(this,conf):
        this.log = []
        loginit(this.log)
        tmpconf = {}
        tmpconf.update(this.conf)
        tmpconf.update(this.conf_default)
        tmpconf.update(conf)
        this.conf = tmpconf
        this.s1 = Skill("s1",this.conf["s1_sp"])
        this.s2 = Skill("s2",this.conf["s2_sp"])
        this.s3 = Skill("s3",this.conf["s3_sp"])

        if this.conf['x_type']== "ranged":
            this.x = this.range_x
        elif this.conf['x_type']== "melee":
            this.x = this.melee_x

    def init(this): #virtual
        pass

    def x(this): #virtual
        pass

    def ac(this, e):
        this.x()

    def run(this, d = 300):

        Timeline().reset()
        this.idle = Event("idle", this.ac).on()
        this.x_status = (0,0)
        Event("s1").listener(this.s)
        Event("s2").listener(this.s)
        Event("s3").listener(this.s)

        this.init()
        Timeline().run(d)

    def think_pin(this, pin):
        if pin in this.conf['think_latency'] :
            latency = this.conf['think_latency'][pin]
        else:
            latency = this.conf['think_latency']['default']
        e = Event('think', this.think).on(now() + latency).pin = pin

    def think(this, e):
        if e.pin == 'sp' and 'sp' in this.conf['al']:
            for i in this.conf['al']['sp']:
                if getattr(this,i).cast():
                    break

        if e.pin == 'x_cancel':
            if 'x5' in this.conf['al'] and this.x_status == (5, 0):
                for i in this.conf['al']['x5']:
                    if getattr(this,i).check():
                        log("cancel",'x%s'%this.x_status[0],0)
                        getattr(this,i).cast()
                        break

            elif 'x4' in this.conf['al'] and this.x_status == (4, 5):
                for i in this.conf['al']['x4']:
                    if getattr(this,i).check():
                        log("cancel",'x%s'%this.x_status[0],0)
                        getattr(this,i).cast()
                        break
            elif 'x3' in this.conf['al'] and this.x_status == (3, 4):
                for i in this.conf['al']['x3']:
                    if getattr(this,i).check():
                        log("cancel",'x%s'%this.x_status[0],0)
                        getattr(this,i).cast()
                        break
            elif 'x2' in this.conf['al'] and this.x_status == (2, 3):
                for i in this.conf['al']['x2']:
                    if getattr(this,i).check():
                        log("cancel",'x%s'%this.x_status[0],0)
                        getattr(this,i).cast()
                        break
            elif 'x1' in this.conf['al'] and this.x_status == (1, 2):
                for i in this.conf['al']['x1']:
                    if getattr(this,i).check():
                        log("cancel",'x%s'%this.x_status[0],0)
                        getattr(this,i).cast()
                        break
            else:
                return
            #elif this.x_status == (0, 1) and this.conf['al']['x1']:
                #for i in this.conf['al']['x0'] :
                    #getattr(this, i).cast()
        if e.pin == 's' and 's' in this.conf['al']:
            for i in this.conf['al']['s'] :
                if getattr(this, i).cast():
                    break

    def charge(this, name, sp): #, percent=None):
        if type(sp) == str and sp[-1] == '%':
            percent = int(sp[:-1])
            this.s1.charge(this.conf['s1_sp']*percent/100)
            this.s2.charge(this.conf['s2_sp']*percent/100)
            this.s3.charge(this.conf['s3_sp']*percent/100)
            log("sp", name, "%d%%"%percent,"%d/%d, %d/%d, %d/%d"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )
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

    def dmg_mod_fs(this):
        return 1

    def att_mod(this):
        return 1
    

    def speed(this):
        return 1


    def arm_mod(this):
        return 1


    def sp_mod(this, name):
        return 1


    def dmg_make(this, name, dmg_p):
        count = this.dmg_formula(name, dmg_p)
        
        if name[0] == "x":
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (+%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        else:
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (-%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )


    def missile(this,e):
        this.dmg_make(e.name, e.amount)
        this.charge(e.name, e.samount)


    def range_x(this):
        if this.x_status[1] == 0 :
            time = float(this.conf["x1_startup"]) / this.speed()
            this.idle.timing += time
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
        this.think_pin("x_cancel")

        if seq == 5:
            this.x_status = (5, 0)
            time = float(this.conf["x5_recovery"]) / this.speed()
        else:
            this.x_status = (seq, seq+1)
            time = float(this.conf["x%d_startup"%(seq+1)]) / this.speed()
        this.idle.timing += time

    def melee_x(this):
        if this.x_status[1] == 0 :
            time = float(this.conf["x1_startup"]) / this.speed()
            this.idle.timing += time
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

        this.think_pin("x_cancel")

        if seq == 5:
            this.x_status = (5, 0)
            time = float(this.conf["x5_recovery"]) / this.speed()
        else:
            this.x_status = (seq, seq+1)
            time = float(this.conf["x%d_startup"%(seq+1)]) / this.speed()
        this.idle.timing += time



    def s(this, e):
        #if e.name == "s1":
            #this.s1_proc(e)

        seq = this.x_status[0]
        log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after c%s)"%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, seq ) )

        this.idle.timing = now() + this.conf[e.name+"_time"] / this.speed()
        dmg = this.conf[e.name+"_dmg"]
        if dmg :
            this.dmg_make(e.name , this.conf[e.name+"_dmg"])

        func = e.name + '_proc'
        getattr(this, func)(e)

        this.x_status = (0, 0)
        #this.think_pin("s")

    def s1_proc(this, e):
        pass

    def s2_proc(this, e):
        pass

    def s3_proc(this, e):
        pass


def sum_dmg():
    l = logget()
    dmg_sum = {'x':0, 's':0}
    for i in l:
        if i[1] == 'dmg':
            dmg_sum[i[2][0]] += i[3]

    total = 0
    for i in dmg_sum:
        total += dmg_sum[i]
    dmg_sum['total'] = total
    print dmg_sum


if __name__ == "__main__":

    conf = {}
    conf.update( {
        "x_type"      : "ranged" ,

        "x1_dmg"      : 0.98     ,
        "x1_sp"       : 130      ,
        "x1_startup"  : 18/60.0  ,

        "x2_dmg"      : 1.06     ,
        "x2_sp"       : 200      ,
        "x2_startup"  : 33/60.0  ,

        "x3_dmg"      : 1.08     ,
        "x3_sp"       : 240      ,
        "x3_startup"  : 31/60.0  ,

        "x4_dmg"      : 1.56     ,
        "x4_sp"       : 430      ,
        "x4_startup"  : 53/60.0  ,

        "x5_dmg"      : 2.06     ,
        "x5_sp"       : 600      ,
        "x5_startup"  : 64/60.0  ,
        "x5_recovery" : 68/60.0  ,

        "fs_dmg"      : 1.8      ,
        "fs_sp"       : 400      ,
        "fs_startup"  : 42/60.0  ,
        "fs_recovery" : 81/60.0  ,

        "dodge_recovery": 43/60.0,

        "missile_iv"  : [0.7/2, 0.7, 0.7, 0.7, 0.7, 0.7], # fs, c1, c2...
        } )

    conf.update( {
        "s1_dmg"  : 1.61*6   ,
        "s1_sp"   : 2648     ,
        "s1_time" : 167/60.0 ,

        "s2_dmg"  : 2.44*4   ,
        "s2_sp"   : 5838     ,
        "s2_time" : 114/60.0 ,

        "s3_dmg"  : 0        ,
        "s3_sp"   : 0        ,
        "s3_time" : 0        ,
        } )

    conf.update( {
        "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05}
        } )
    al = {
        'sp': [],
        'x5': [],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        'x0': [],
        }

    al.update( {
            #'sp': ["s1","s2"],
            'x5': ["s1", "s2"],
            'x4': ["s1", "s2"],
            'x3': ["s1", "s2"],
            'x2': ["s1", "s2"],
            'x1': ["s1", "s2"],
            'x0': ["s1", "s2"],
        } )

    conf['al'] = al

    a = Adv(conf)
    a.run(300)
    logcat(['dmg','x','cast'])
    sum_dmg()


    logreset()
    conf['al'] = {
            'sp': ["s1","s2"],
            'x5': [],
            'x4': [],
            'x3': [],
            'x2': [],
            'x1': [],
            'x0': [],
            }

    a = Adv(conf)
    a.run(300)
    sum_dmg()
            


