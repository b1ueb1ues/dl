from core.timeline import *
from core.log import *
import core.acl
import sys

loglevel = 0
if len(sys.argv) >= 2:
    loglevel = int(sys.argv[1])

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
        if this.active == 0:
            this.active = 1
            this.buff_end_event.on(now()+d)
            log("buff", this.name, this.value(), this.name+" buff start <%ds>"%d)
        else:
            this.buff_end_event.timing = now() + d
            log("buff", this.name, this.value(), this.name+" buff refresh <%ds>"%d)

        return this


    def off(this):
        log("buff", this.name, this.value(), this.name+" buff end <turn off>")
        this.active = 0
        this.buff_end_event.off()
        return this


class Skill(object):
    charged = 0
    sp = 0
    silence_duration = 1.9
    silence = [0]
    name = "_Skill"
    def __init__(this, name=None, sp=None, ac=None):
        this.charged = 0
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
        this.silence[0] = 0
        this.silence_end = Event("silence",this.restore)
        this.trigger_this = Event(this.name+"_cast").trigger
        this.trigger_silence_end = Event("silence_end").trigger
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
        if loglevel >= 2:
            log("silence","end")
        this.silence[0] = 0
        this.trigger_silence_end()


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
            this.ac()
            if duration == None:
                duration = this.silence_duration
            # Even if animation is shorter than 1.9, you can't cast next skill before 1.9
            if duration > 1.9:
                duration = 1.9
            this.silence_end.on(now()+duration)
            this.silence[0] = 1
            if loglevel >= 2:
                log("silence","start")
            return 1

    def ac(this):
        this.trigger_this()


class Action(object):   
    prev = [0]
    doing = [0] # idle
    spd_func = [0]
    name = "_Action"
    index = 0
    recover_start = 0
    startup_start = 0
    _startup = 0
    _recovery = 0
    status = -2 # -2nop -1startup 0doing 1recovery

    def __init__(this, name=None, conf=None, act=None):  ## can't change name after this
        if name != None:
            if type(name) == tuple:
                this.name = name[0]
                this.index = name[1]
            else:
                this.name = name
                this.index = 0
        if conf != None:
            this._startup = conf[this.name+"_startup"]
            this._recovery = conf[this.name+"_recovery"]
            
        if act != None:
            this.act = act

        if this.spd_func[0] == 0:
            this.spd_func[0] = this.nospeed

        this.cancel_by = []
        this.interrupt_by = []

        this.startup_event = Event("acting", this._cb_acting)
        this.recovery_event = Event("action_end", this._cb_act_end)
        this.e_idle = Event("idle")
        this.e_this = Event(this.name)

    def __call__(this):
        return this.tap()
    
    def getdoing(this):
        return this.doing[0]
    def _setdoing(this):
        this.doing[0] = this
    def getprev(this):
        return this.prev[0]
    def _setprev(this):
        this.prev[0] = this.doing[0]

    def getrecovery(this):
        return this._recovery / this.speed()

    def getstartup(this):
        return this._startup / this.speed()

    def nospeed(this):
        return 1

    def speed(this):
        return this.spd_func[0]()

    def _cb_acting(this, e):
        if this.getdoing() == this:
            this.status = 0
            this.act()
            this.status = 1
            this.recover_start = now() 
            this.recovery_event.on(now()+ this.getrecovery())


    def _cb_act_end(this, e):
        if this.getdoing() == this:
            if loglevel >= 2:
                log("ac_end",this.name)
            this.status = -2
            this._setprev() # turn this from doing to prev
            this.doing[0] = 0
            this.e_idle.trigger()


    def act(this):
        if loglevel >= 2:
            log("ac",this.name)
        this.e_this.trigger()


    def tap(this):
        doing = this.getdoing()

        if doing == 0:
            if loglevel >= 2:
                log("tap",this.name, None, 'idle')
        else:
            if loglevel >= 2:
                log("tap",this.name, None, 'doing '+doing.name)

        if doing == this : # self is doing
            return 0

        #if doing == 0: # idle
        #    pass
        if doing != 0 : # doing != this
            if doing.status == -1: # try to interrupt an action
                if this.name in doing.interrupt_by : # can interrupt action
                    log("interrupt", doing.name , "by "+this.name+"\t", "after %.2fs"%(now()-doing.startup_start) )
                else:
                    return 0
            elif doing.status == 1: # try to cancel an action
                if this.name in doing.cancel_by : # can interrupt action
                    log("cancel", doing.name , "by "+this.name+"\t", "after %.2fs"%(now()-doing.recover_start) )
                else:
                    return 0
            elif doing.status == 0:
                print "err in action tap()"
                exit()
            this._setprev()
        this.status = -1
        this.startup_start = now()
        this.startup_event.on(now()+this.getstartup())
        this._setdoing()
        #this.act()
        return 1



class Adv(object):
    x_status = (0,0)
    conf = {}

    conf_default = { 
        "latency" : {'x':0.05, 'sp':0.05, 'default':0.05, 'idle':0},

        "s1_dmg"      : 0   ,
        "s1_sp"       : 0   ,
        "s1_startup"  : 0.1 ,
        "s1_recovery" : 1.9 ,

        "s2_dmg"      : 0   ,
        "s2_sp"       : 0   ,
        "s2_startup"  : 0.1 ,
        "s2_recovery" : 1.9 ,

        "s3_dmg"      : 0   ,
        "s3_sp"       : 0   ,
        "s3_startup"  : 0.1 ,
        "s3_recovery" : 1.9 ,
        }

    conf_default['acl'] = """
        `s1
        `s2
        `s3
    """

    acl_prepare_default = """
        #pin=e.pin
        #dname=e.dname
        #dstat=e.dstat
        #didx=e.didx
        #xseq = -1
        #x=0
        #s=0
        #sx=0
        #sp=0
        #cancel=0
        #prev = this.action.getprev()
        #pname="00"
        #pidx=0
        #pstat=0
        #if prev != 0:\n    pname = prev.name\n    pidx = prev.index\n    pstat = prev.status

        #if dname[0] == 'x': xseq = didx
        #if dname == 'idle': xseq = 0
        
        #seq = xseq
        #if pin == 'x': \n    x=1\n    cancel=1\n    x_cancel=1
        #if pin == 'fs':\n    fs=1\n    cancel=1
        #if pin == 'idle' and pname[0]=='s': \n    s = int(pname[1])
        #if pin == 's-x': \n    s = this.s_prev\n    sx=this.s_prev\n
        #if pin == 'sp': sp=1
        #s1=this.s1
        #s2=this.s2
        #s3=this.s3
        #fs=this.fs
    """


    def __init__(this,conf):
        this.log = []
        loginit(this.log)
        tmpconf = {}
        tmpconf.update(this.conf_default)
        tmpconf.update(this.conf)
        tmpconf.update(conf)
        this.conf = tmpconf
        this.s_prev = 0

        this.skill = Skill()
        this.action = Action()
        this.action.spd_func[0] = this.speed

        # init actions
        this.a_s1 = Action(("s1",1),this.conf)
        this.a_s2 = Action(("s2",2),this.conf)
        this.a_s3 = Action(("s3",3),this.conf)
        this.a_fs = Action("fs",this.conf)
        this.a_x1 = Action(("x1",1),this.conf)
        this.a_x2 = Action(("x2",2),this.conf)
        this.a_x3 = Action(("x3",3),this.conf)
        this.a_x4 = Action(("x4",4),this.conf)
        this.a_x5 = Action(("x5",5),this.conf)

        this.a_x1.cancel_by = ["dodge","fs","s1","s2","s3"]
        this.a_x2.cancel_by = ["dodge","fs","s1","s2","s3"]
        this.a_x3.cancel_by = ["dodge","fs","s1","s2","s3"]
        this.a_x4.cancel_by = ["dodge","fs","s1","s2","s3"]
        this.a_x5.cancel_by = ["dodge","fs","s1","s2","s3"]
        this.a_fs.cancel_by = ["dodge","s1","s2","s3"]

        this.a_x1.interrupt_by = ["dodge", "fs","s1","s2","s3"]
        this.a_x2.interrupt_by = ["dodge", "fs","s1","s2","s3"]
        this.a_x3.interrupt_by = ["dodge", "fs","s1","s2","s3"]
        this.a_x4.interrupt_by = ["dodge", "fs","s1","s2","s3"]
        this.a_x5.interrupt_by = ["dodge", "fs","s1","s2","s3"]
        this.a_fs.interrupt_by = ["s1","s2","s3"]

        # set cmd
        this.x1 = this.a_x1
        this.x2 = this.a_x2
        this.x3 = this.a_x3
        this.x4 = this.a_x4
        this.x5 = this.a_x5
        this.fs = this.a_fs
        this.s1 = Skill("s1",this.conf["s1_sp"],this.a_s1.tap)
        this.s2 = Skill("s2",this.conf["s2_sp"],this.a_s2.tap)
        this.s3 = Skill("s3",this.conf["s3_sp"],this.a_s3.tap)

        if this.conf['x_type']== "ranged":
            this.l_x = this.l_range_x
            this.l_fs = this.l_range_fs
            #this.fs_success = this.range_fs_sucess
        elif this.conf['x_type']== "melee":
            this.l_x = this.l_melee_x
            this.l_fs = this.l_melee_fs
            #this.fs_success = this.melee_fs_success
        this._el = {}
        save_event_listeners(this._el)


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
    def def_mod(this):
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


    def l_idle(this, e):
        this.think_pin("idle")
        this.x()
        pass

    def getxseq(this):
        doing = this.action.getdoing()
        if doing.name[0] == 'x':
            return doing.index, doing,status
        else:
            return doing.name, doing.index


    def getprev(this):
        prev = this.action.getprev()
        return prev.name, prev.index, prev.status


    def x(this):
        prev = this.action.getprev() 
        x_next = 1
        if prev != 0:
            if prev.name[0] == 'x':
                if prev.index != 5:
                    x_next = prev.index + 1

        a = getattr(this, "x%d"%x_next)()
        return 1


    def l_range_x(this, e):
        xseq = e.name
        dmg_p = this.conf["%s_dmg"%xseq]
        sp_gain = this.conf["%s_sp"%xseq] 
        if xseq == 'x5':
            log("x", "%s"%xseq, 0,"-------------------------------------c5")
        else:
            log("x", "%s"%xseq, 0)

        missile_event = Event("%s_missile"%xseq, this.missile, 
                now() + this.conf['missile_iv'][xseq] )
        missile_event.amount = dmg_p
        missile_event.samount = sp_gain
        missile_event.on()

        this.think_pin("x")
    
    def l_melee_x(this, e):
        xseq = e.name
        dmg_p = this.conf["%s_dmg"%xseq]
        sp = this.conf["%s_sp"%xseq] 
        if xseq == 'x5':
            log("x", "%s"%xseq, 0,"-------------------------------------c5")
        else:
            log("x", "%s"%xseq, 0)
        this.dmg_make("%s"%xseq, dmg_p)
        this.charge("%s"%xseq, sp)
        this.think_pin("x")


    def run(this, d = 300):
        Timeline().reset()
        load_event_listeners(this._el)

        Event("init", this.l_idle).on()
        Event("idle").listener(this.l_idle)

        Event("x1").listener(this.l_x)
        Event("x2").listener(this.l_x)
        Event("x3").listener(this.l_x)
        Event("x4").listener(this.l_x)
        Event("x5").listener(this.l_x)
        Event("fs").listener(this.l_fs)
        Event("s1").listener(this.l_s)
        Event("s2").listener(this.l_s)
        Event("s3").listener(this.l_s)

        Event("silence_end").listener(this.think_after_s)

        this.cb_think = this.think3

        this.init()

        this._acl, this._acl_str = core.acl.acl_func_str(
                this.acl_prepare_default+this.conf['acl'] 
                )
        #this._acl, this._acl_str = core.acl.acl_func_str(
        #       this.acl_prepare_default+this.conf['acl']+'`x')

        Timeline().run(d)


    def think_pin(this, pin):
        if pin in this.conf['latency'] :
            latency = this.conf['latency'][pin]
        else:
            latency = this.conf['latency']['default']
        e = Event('think', this.cb_think).on(now() + latency)
        e.pin = pin
        doing = this.action.getdoing()
        e.dname = 'idle'
        e.didx = -1
        e.dstat = -1
        if doing:
            e.dname = doing.name
            e.dstat = doing.status
            e.didx = doing.index


    def think_after_s(this, e):
        if this.skill.silence[0] == 1:
            print '1'
            exit()
            this.think_pin(e.name)
            this.first_x_after_s = 1
        else :
            this.think_pin(e.name+"-x")
            this.think_pin(e.name)


    def cb_think(this, e):
        pass

    def think3(this, e):
        this._acl(this, e)


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
        armor = 10.0 * this.def_mod()
        #return 5.0/3 * dmg_p * this.dmg_mod(name) * att/arm   # true formula 
        return att/armor * dmg_p * this.dmg_mod(name)



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


    def l_melee_fs(this, e):
        log("fs","succ")
        dmg_p = this.conf["fs_dmg"]
        this.dmg_make("fs", dmg_p)
        this.charge("fs",this.conf["fs_sp"])
        this.fs_proc(e)
        this.think_pin("fs")

    def l_range_fs(this, e):
        log("fs","succ")
        dmg_p = this.conf["fs_dmg"]
        sp_gain = this.conf["fs_sp"]
        missile_event = Event("fs_missile", this.missile, 
                now() + this.conf['missile_iv']['fs'] )
        missile_event.amount = dmg_p
        missile_event.samount = sp_gain
        missile_event.on()
        this.fs_proc(e)
        this.think_pin("fs")


    def fs(this):
        xseq = this.x_status[0]
        if xseq != 0:
            time = now() - this.x_prev
            log("cancel", "x%d"%xseq , time)

        if xseq != 0:
            log("fs", 'hold', 0,"                               (hold fs after c%s)"%( xseq ) )
        else:
            log("fs", 'hold', 0,"                               (hold fs)" )

        this.x_next.timing = now() + (this.conf["fs_startup"] + this.conf["fs_recovery"]) / this.speed()
        this.fs_hold.on(now()+this.conf['fs_startup'])

        this.x_status = (-1, 0)
        this.doing = "fs_hold"
        return 1


    def l_s(this, e):
        prev, index, stat = this.getprev()
        if prev == 'fs':
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after fs)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name) )
        elif prev[0] == 'x':
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after c%s)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, index ) )
        else:
            log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after %s)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, prev ) )

        dmg_p = this.conf[e.name+"_dmg"]
        if dmg_p :
            this.dmg_make(e.name , dmg_p)

        func = e.name + '_proc'
        getattr(this, func)(e)





if __name__ == "__main__":
    print "to use adv_test"

