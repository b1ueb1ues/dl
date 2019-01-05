from core.timeline import *
from core.log import *
import core.acl
import sys
import conf as globalconf
import random


class Modifier(object):
    _static = Static()
    _static.all_modifiers = []
    mod_name = "<nop>"
    mod_type = "_nop" or "att" or "x" or "fs" or "s" #....
    mod_order = "_nop" or "passive" or "ex" or "buff" # chance dmg for crit 
    mod_value = 0
    def __init__(this, name, mtype, order, value):
        this.mod_name = name
        this.mod_type = mtype
        this.mod_order = order
        this.mod_value = value
        this._static['all_modifiers'].append(this)
    def get(this):
        return this.mod_value
    def __repr__(this):
        return "<%s %s %s %s>"%(this.mod_name, this.mod_type, this.mod_order, this.mod_value)

class Dot(object):
    #_static = Static()
    #_static.all_dots = []
    def __init__(this, name, dmg, duration, iv):
        this.__name = name
        this.active = 0
        this.dmg = dmg
        this.iv = iv
        this.duration = duration
        this.dmg_event = Event("dmg")
        this.tick_event = Event("dot_tick", this.tick_proc)
        this.dotend_event = Event("dot_end",this.dot_end_proc)
        #this._static.all_dots.append(this)

    def dot_end_proc(this, e):
        this.active = 0

    def tick_proc(this, e):
        if this.active == 0:
            return
        this.tick_event.timing += this.iv
        this.dmg_event.dmg = this.dmg
        this.dmg_event.name = this.__name
        this.dmg_event.trigger()
        

    def on(this):
        this.active = 1
        this.tick_event.on(now()+this.iv)
        this.dotend_event.on(now()+this.duration)



class Buff(object):
    _static = Static()
    _static.all_buffs = []
    def __init__(this, name='<buff_noname>', value=0, duration=0, mtype=None, morder=None):  
        this.__name = name   
        this._value = value
        this.duration = duration
        this.mod_type = mtype or "<null>" or "att" or "x" or "fs" or "s" #....
        if morder ==None:
            if this.mod_type == 'crit':
                this.mod_order = 'chance'
            else:
                this.mod_order = 'buff'
        else:
            this.mod_order = morder or "<null>" or "passive" or "ex" or "buff" or "punisher" #...

        this.__active = 0
        this.buff_end_event = Event("buff",this.buff_end_proc)
        this._static.all_buffs.append(this)
        this.modifier = Modifier("mod_"+this.__name, this.mod_type, this.mod_order, 0)
        this.modifier.get = this.get

    def reset(this):
        this._static.all_buffs = []
        return this

    def value(this):
        if this.__active:
            return this._value
        else:
            return 0

    def get(this):
        if this.__active:
            return this._value
        else:
            return 0

    def set(this, v):
        this._value = v
        return this

    def buff_end_proc(this, e):
        log("buff", this.__name, this.value(), this.__name+" buff end <timeout>")
        this.__active = 0
        stack = 0
        for i in this._static.all_buffs:
            if i.__name == this.__name:
                if i.__active != 0:
                    stack += 1
        if stack > 0:
            log("buff", this.__name, this.value(), this.__name+" buff stack <%d>"%stack)


    def on(this, duration=None):
        if duration == None:
            d = this.duration
        else:
            d = duration
        if this.__active == 0:
            this.__active = 1
            this.buff_end_event.on(now()+d)
            log("buff", this.__name, this.value(), this.__name+" buff start <%ds>"%d)
        else:
            this.buff_end_event.timing = now() + d
            log("buff", this.__name, this.value(), this.__name+" buff refresh <%ds>"%d)

        stack = 0
        for i in this._static.all_buffs:
            if i.__name == this.__name:
                if i.__active != 0:
                    stack += 1
        if stack > 1:
            log("buff", this.__name, this.value(), this.__name+" buff stack <%d>"%stack)


        return this


    def off(this):
        log("buff", this.__name, this.value(), this.__name+" buff end <turn off>")
        this.__active = 0
        this.buff_end_event.off()
        return this


class Skill(object):
    _static = Static()
    _static.s_prev = "<nop>"
    _static.first_x_after_s = 0
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
        this.se = Event("silence_end")
        this.trigger_silence_end = this.se.trigger
        this.init()

    def __call__(this):
        return this.cast()


    def init(this):
        pass


    def charge(this,sp):
        this.charged += sp   
        #if this.charged > this.sp:  # should be 
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

    def cast(this):
        if not this.check():
            return 0
        else:
            if not this.ac() :
                return 0
            this.charged = 0
            this._static.s_prev = this.name
            duration = this.silence_duration
            # Even if animation is shorter than 1.9, you can't cast next skill before 1.9
            this.silence_end.on(now()+duration)
            this.silence[0] = 1
            if loglevel >= 2:
                log("silence","start")
            return 1

    def ac(this):
        this.trigger_this()
        return 1


class Action(object):   
    _static = Static()
    _static.prev = 0
    _static.doing = 0
    _static.spd_func = 0

    #prev = [0]
    #doing = [0] # idle
    #spd_func = [0]
    name = "_Action"
    index = 0
    recover_start = 0
    startup_start = 0
    _startup = 0
    _recovery = 0
    status = -2 # -2nop -1startup 0doing 1recovery
    idle = 0

    class Nop(object):
        name = "__idle__"
        index = 0
        status = -2
        idle = 1

    nop = Nop()

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

        if this._static["spd_func"] == 0:
            this._static["spd_func"] = this.nospeed
        if this._static["doing"] == 0:
            this._static["doing"] = this.nop
        if this._static["prev"] == 0:
            this._static["prev"] = this.nop

        this.cancel_by = []
        this.interrupt_by = []

        this.startup_event = Event("acting", this._cb_acting)
        this.recovery_event = Event("action_end", this._cb_act_end)
        this.e_idle = Event("idle")
        this.e_this = Event(this.name)

    def reset(this):
        this._static.prev = 0
        this._static.doing = 0
        this._static.spd_func = 0

    def __call__(this):
        return this.tap()
    
    def getdoing(this):
        return this._static['doing']
    def _setdoing(this):
        this._static["doing"] = this
    def getprev(this):
        return this._static['prev']
    def _setprev(this):
        this._static['prev'] = this._static['doing']

    def getrecovery(this):
        return this._recovery / this.speed()

    def getstartup(this):
        return this._startup / this.speed()

    def nospeed(this):
        return 1

    def speed(this):
        return this._static.spd_func()

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
            this._static['doing'] = this.nop
            this.e_idle.trigger()


    def act(this):
        if loglevel >= 2:
            log("act",this.name)
        this.e_this.trigger()


    def tap(this):
        doing = this.getdoing()

        if doing.idle :
            if loglevel >= 2:
                log("tap",this.name, None, 'idle')
        else:
            if loglevel >= 2:
                log("tap",this.name, None, 'doing '+doing.name)

        if doing == this : # self is doing
            return 0

        #if doing.idle # idle
        #    pass
        if not doing.idle : # doing != this
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
        return 1



class Adv(object):
    # vvvvvvvvv rewrite this to provide advanced tweak vvvvvvvvvv
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
    def speed(this):
        return 1
    def init(this): 
        pass
    # ^^^^^^^^^ rewrite this to provide advanced tweak ^^^^^^^^^^

    x_status = (0,0)
    conf = {}

    conf_default = { 
        "latency" : {'x':0.05, 'sp':0.05, 'default':0.05, 'idle':0},
        "latency" : {'x':0.00, 'sp':0.00, 'default':0.00, 'idle':0},

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
        #prev = this.action.getprev()
        #pname=prev.name
        #pidx=prev.index
        #pstat=prev.status

        #xseq = -1
        #if dname[0] == 'x': xseq = didx
        #if dstat == -2: xseq = 0
        #seq = xseq

        #cancel=0
        #x=0
        #fsc=0
        #if pin == 'x': \n    x=1\n    cancel=1\n    x_cancel=1
        #if pin == 'fs':\n    fsc=1\n    cancel=1

        #s=0
        #sx=0
        #if pin[0] == 's' and pin[1] != 'p':\n    s=int(pin[1])
        #if pin[-2:] == '-x':\n    s=int(pin[1])\n    sx=s\n

        #sp=0
        #if pin == 'sp': sp=dname

        #s1=this.s1
        #s2=this.s2
        #s3=this.s3
        #fs=this.fs
    """
        #if pin[-2:] == '-x':\n    s=pidx\n    sx=pidx\n    print sx\n    print pin\n    exit()


    def __init__(this,conf):
        random.seed()
        this.timeline = Timeline().reset()
        this.log = []
        loginit(this.log)
        tmpconf = {}

        this.adv_name = this.__class__.__name__

        tmpconf.update(this.conf_default)
        tmpconf.update(this.conf)
        tmpconf.update(conf)
        this.conf = tmpconf

        this.base_str = this.conf['base_str']
        if 1:
            this.crit_mod = this.solid_crit_mod
        else:
            this.crit_mod = this.rand_crit_mod

        this.skill = Skill()
        this.action = Action()
        this.action.reset()
        this.action._static['spd_func'] = this.speed
        this.buff = Buff()
        this.buff._static['all_buffs'] = []
        # set modifier
        this.modifier = Modifier(0,0,0,0)
        this.modifier._static['all_modifiers'] = []
        for i in this.conf:
            if i[:3] == 'mod':
                j = this.conf[i]
                if type(j) == tuple:
                    Modifier(i,j[0],j[1],j[2])
                elif type(j) == list:
                    idx = 0
                    for k in j:
                        Modifier(i+"_%d"%idx,k[0],k[1],k[2])
                        idx += 1

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
            return this.mod('s')
        elif name[0:2] == 'fs':
            return this.mod('fs')
        elif name[0] == 'x':
            return this.mod('x')
        else:
            return 1

    def mod(this, mtype):
        m = {}
        for i in this.modifier._static.all_modifiers:
            if mtype == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    m[i.mod_order] = 1 + i.get()
        ret = 1.0
        for i in m:
            ret *= m[i]
        return ret

    def crit_mod(this):
        pass

    def solid_crit_mod(this):
        m = {"chance":0, "dmg":0, "damage":0, "passive":0}
        for i in this.modifier._static.all_modifiers:
            if 'crit' == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    print "err in crit_mod"
                    exit()
        chance = m['chance']+m['passive']
        if chance > 1:
            chance = 1
        cdmg = m['dmg'] + m["damage"] + 1.7
        average = chance * (cdmg-1) + 1
        return average
    
    def rand_crit_mod(this):
        m = {"chance":0, "dmg":0, "damage":0, "passive":0}
        for i in this.modifier._static.all_modifiers:
            if 'crit' == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    print "err in crit_mod"
                    exit()
        chance = m['chance']+m['passive']
        if chance > 1:
            chance = 1
        cdmg = m['dmg'] + m["damage"] + 1.7
        r = random.random()
        if r < chance:
            return cdmg
        else: 
            return 1


    def att_mod(this):
        att = this.mod('att')
        cc = this.crit_mod()
        return cc * att

    def def_mod(this):
        m = this.mod('def')
        if m < 0.5:
            return 0.5
        else:
            return m

    def sp_mod(this, name):
        return this.mod('sp')


    def l_idle(this, e):
        this.think_pin("idle")
        prev = this.action.getprev()
        if prev.name[0] == 's':
            this.think_pin(prev.name)
        if this.skill._static.first_x_after_s :
            this.skill._static.first_x_after_s = 0
            s_prev = this.skill._static.s_prev
            this.think_pin("%s-x"%s_prev)
        this.x()


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
        this.timeline.set()
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
        
        Event("dmg_make").listener(this.l_dmg_make)
        Event("true_dmg").listener(this.l_true_dmg)
        Event("dmg_formula").listener(this.l_dmg_formula)

        this.init()

        this._acl, this._acl_str = core.acl.acl_func_str(
                this.acl_prepare_default+this.conf['acl'] 
                )

        Timeline().run(d)


    def think_pin(this, pin):
        if pin in this.conf['latency'] :
            latency = this.conf['latency'][pin]
        else:
            latency = this.conf['latency']['default']
        e = Event('think', this.cb_think).on(now() + latency)
        doing = this.action.getdoing()
        e.pin = pin
        e.dname = doing.name
        e.dstat = doing.status
        e.didx = doing.index


    def think_after_s(this, e):
        doing = this.action.getdoing()
        sname = this.skill._static.s_prev
        if doing.name[0] == 'x':
            this.skill._static.first_x_after_s = 1
        else:
            this.think_pin(sname+'-x')  # best choice
        this.think_pin(sname)
        #if doing.name[0] == 's': 
        #   no_deed_to_do_anythin
            


    def cb_think(this, e):
        if loglevel >= 2:
            log("think", e.pin, e.dname)
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

    def l_dmg_formula(this, e):
        name = e.name
        dmg_p = e.dmg_p
        e.dmg = this.dmg_formula(name, dmg_p)
        e.ret = e.dmg
        return

    def dmg_formula(this, name, dmg_p):
        att = 1.0 * this.att_mod() * this.base_str
        armor = 10.0 * this.def_mod()
        return 5.0/3 * dmg_p * this.dmg_mod(name) * att/armor   # true formula 
        #return att/armor * dmg_p * this.dmg_mod(name)

    def l_true_dmg(this, e):
        name = e.name
        count = e.dmg
        comment = e.comment
        log("dmg", name, count, comment)

    def l_dmg_make(this, e):
        name = e.name
        dmg_p = e.dmg_p
        dmg_make(name, dmg_p)

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
            spgain = 0
            if name[:2]+"_sp" in this.conf:
                spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (-%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        this.dmg_proc(name, count)


    def missile(this,e):
        this.dmg_make(e.name, e.amount)
        this.charge(e.name, e.samount)


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
        if e.name+"_buff" in this.conf:
            buffarg = this.conf[e.name+'_buff']
            Buff(e.name, *buffarg).on()

        func = e.name + '_proc'
        getattr(this, func)(e)



if __name__ == "__main__":
    print "to use adv_test"

