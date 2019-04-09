from timeline import *
from log import *
import acl
import sys
import conf as globalconf
import random
import condition 
m_condition = condition


class Modifier(object):
    _static = Static({
        'all_modifiers': [],
        })
    mod_name = '<nop>'
    mod_type = '_nop' or 'att' or 'x' or 'fs' or 's' #....
    mod_order = '_nop' or 'passive' or 'ex' or 'buff' # chance dmg for crit 
    mod_value = 0
    def __init__(this, name, mtype, order, value, condition=None):
        this.mod_name = name
        this.mod_type = mtype
        this.mod_order = order
        this.mod_value = value
        this.mod_condition = condition
        this.__active = 0
        this.on()
        #this._static.all_modifiers.append(this)
        #this.__active = 1

    @classmethod
    def mod(cls, mtype, all_modifiers=None):
        if not all_modifiers:
            all_modifiers = cls._static.all_modifiers
        m = {}
        for i in all_modifiers:
            if mtype == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    m[i.mod_order] = 1 + i.get()
        ret = 1.0
        for i in m:
            ret *= m[i]
        return ret

    def get(this):
        return this.mod_value


    def on(this, modifier=None):
        if this.__active == 1:
            return this
        if modifier == None:
            modifier = this
        if modifier.mod_condition :
            if not m_condition.on(modifier.mod_condition):
                return this

        this._static.all_modifiers.append(modifier)
        this.__active = 1
        return this


    def off(this, modifier=None):
        if this.__active == 0:
            return this
        this.__active = 0
        if modifier==None:
            modifier = this
        idx = len(this._static.all_modifiers)
        while 1:
            idx -= 1
            if idx < 0:
                break
            if this._static.all_modifiers[idx] == modifier:
                this._static.all_modifiers.pop(idx)
                break
        return this


    def __repr__(this):
        return '<%s %s %s %s>'%(this.mod_name, this.mod_type, this.mod_order, this.mod_value)


class Dot(object):
    def __init__(this, name, dmg, duration, iv):
        this.name = name
        this.active = 0
        this.dmg = dmg
        this.iv = iv
        this.duration = duration
        this.dmg_event = Event('dmg')
        this.tick_timer = Timer(this.tick_proc)
        this.dotend_timer = Timer(this.dot_end_proc)

    def dot_end_proc(this, e):
        this.active = 0

    def tick_proc(this, e):
        if this.active == 0:
            return
        this.tick_event.timing += this.iv
        this.dmg_event.dmg = this.dmg
        this.dmg_event.dname = this.name
        this.dmg_event.trigger()
        

    def on(this):
        this.active = 1
        this.tick_timer.on(this.iv)
        this.dotend_timer.on(this.duration)



class Buff(object):
    _static = Static({
        'all_buffs': [],
        'time_func':0,
        })
    def __init__(this, name='<buff_noname>', value=0, duration=0, mtype=None, morder=None):  
        this.name = name   
        this.__value = value
        this.duration = duration
        this.mod_type = mtype or 'att' or 'x' or 'fs' or 's' #....
        this.bufftype = ''
        if morder ==None:
            if this.mod_type == 'crit':
                this.mod_order = 'chance'
            else:
                this.mod_order = 'buff'
        else:
            this.mod_order = morder or '<null>' or 'passive' or 'ex' or 'buff' or 'punisher' #...

        if this.mod_order != 'buff':
            this.bufftime = this.nobufftime
        if not this._static.time_func:
            this._static.time_func = this.nobufftime

        this.buff_end_timer = Timer(this.buff_end_proc)
        this.modifier = Modifier('mod_'+this.name, this.mod_type, this.mod_order, 0)
        this.modifier.get = this.get
        this.dmg_test_event = Event('dmg_formula')
        this.dmg_test_event.dmg_coef = 1
        this.dmg_test_event.dname = 'test'

        this.__stored = 0
        this.__active = 0
        #this.on()

    def nobufftime(this):
        return 1
    
    def bufftime(this):
        return this._static.time_func()


    def value(this, newvalue=None):
        if newvalue:
            return this.set(newvalue)
        else:
            return this.get()

    def get(this):
        if this.__active:
            return this.__value
        else:
            return 0

    def set(this, v, d=None):
        this.__value = v
        if d != None:
            this.duration = d
        return this

    def buff_end_proc(this, e):
        log('buff', this.name, '%s: %.2f'%(this.mod_type, this.value()), this.name+' buff end <timeout>')
        this.__active = 0

        if this.__stored:
            idx = len(this._static.all_buffs)
            while 1:
                idx -= 1
                if idx < 0:
                    break
                if this == this._static.all_buffs[idx]:
                    this._static.all_buffs.pop(idx)
                    break
            this.__stored = 0
        stack = 0
        for i in this._static.all_buffs:
            if i.name == this.name:
                if i.__active != 0:
                    stack += 1
        if stack > 0:
            log('buff', this.name, '%s: %.2f'%(this.mod_type, this.__value*stack), this.name+' buff stack <%d>'%stack)
        this.modifier.off()


    def on(this, duration=None):
        if duration == None:
            d = this.duration * this.bufftime()
        else:
            d = duration * this.bufftime()
        if this.__active == 0:
            this.__active = 1
            if this.__stored == 0:
                this._static.all_buffs.append(this)
                this.__stored = 1
            if d >= 0:
                this.buff_end_timer.on(d)
            log('buff', this.name, '%s: %.2f'%(this.mod_type, this.value()), this.name+' buff start <%ds>'%d)
        else:
            if d >= 0:
                this.buff_end_timer.on(d)
            log('buff', this.name, '%s: %.2f'%(this.mod_type, this.value()), this.name+' buff refresh <%ds>'%d)

        stack = 0
        for i in this._static.all_buffs:
            if i.name == this.name:
                if i.__active != 0:
                    stack += 1
        if stack > 1:
            log('buff', this.name, '%s: %.2f'%(this.mod_type, this.value()*stack), this.name+' buff stack <%d>'%stack)

        this.modifier.on()
        return this


    def off(this):
        if this.__active == 0:
            return 
        log('buff', this.name, '%s: %.2f'%(this.mod_type, this.value()), this.name+' buff end <turn off>')
        this.__active = 0
        this.modifier.off()
        this.buff_end_timer.off()
        return this


class Selfbuff(Buff):
    def __init__(this, name='<buff_noname>', value=0, duration=0, mtype=None, morder=None):  
        Buff.__init__(this, name,value,duration,mtype,morder)
        this.bufftype = 'self'
        this.bufftime = this._bufftime
    
    def _bufftime(this):
        return this._static.time_func()
    
    def buffcount(this):
        bc = 0
        for i in this._static.all_buffs:
            if i.get() and i.bufftype=='self' or i.bufftype=='team':
                bc+=1
        return bc

class Teambuff(Buff):
    def __init__(this, name='<buff_noname>', value=0, duration=0, mtype=None, morder=None):  
        Buff.__init__(this, name,value,duration,mtype,morder)
        this.bufftype = 'team'
        this.bufftime = this._bufftime

    def _bufftime(this):
        return this._static.time_func()

    def on(this, duration=None):
        Buff.on(this, duration)
        this.count_team_buff()
        return this

    def off(this):
        Buff.off(this)
        this.count_team_buff()
        return this

    def buff_end_proc(this,e):
        Buff.buff_end_proc(this,e)
        this.count_team_buff()

    def count_team_buff(this):
        this.dmg_test_event.modifiers = []
        this.dmg_test_event()
        no_team_buff_dmg = this.dmg_test_event.dmg
        modifiers = []
        for i in this._static.all_buffs:
            if i.bufftype=='team' or i.bufftype=='debuff':
                modifiers.append(i.modifier)
        this.dmg_test_event.modifiers = modifiers
        this.dmg_test_event()
        team_buff_dmg = this.dmg_test_event.dmg
        log('buff','team', team_buff_dmg/no_team_buff_dmg-1)

class Debuff(Teambuff):
    def __init__(this, name='<buff_noname>', value=0, duration=0, chance='1', mtype='def', morder=None):  
        value = 0-value
        chance = float(chance)
        if chance!= 1:
            bd = 1.0/(1.0+value)
            bd = (bd-1)*chance+1
            value = 1-1.0/bd
            value = 0-value
        Teambuff.__init__(this, name,value,duration,mtype,morder)
        this.bufftype = 'debuff'
        this.bufftime = this.nobufftime

    def chance(c):
        bd = 1.0/(1.0+this.value)
        bd = (bd-1)*c+1
        this.value = 1-1.0/bd
        return this


class Skill(object):
    _static = Static({
        's_prev'          : '<nop>' ,
        'first_x_after_s' : 0       ,
        'silence'         : 0       ,
        })
    charged = 0
    sp = 0
    silence_duration = 1.9
    name = '_Skill'
    def __init__(this, name=None, sp=None, ac=None):
        this.charged = 0
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
        this._static.silence = 0
        this.silence_end_timer = Timer(this.cb_silence_end)
        this.silence_end_event = Event('silence_end')
        this.cast_event = Event(this.name+'_cast')
        this.init()

    def __call__(this):
        return this.cast()


    def init(this):
        pass


    def charge(this,sp):
        this.charged += sp   
        #if this.charged > this.sp:  # should be 
            #this.charged = this.sp

    def cb_silence_end(this, e):
        if loglevel >= 2:
            log('silence','end')
        this._static.silence = 0
        this.silence_end_event()


    def check(this):
        if this.sp == 0:
            return 0
        elif this._static.silence == 1:
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
            # Even if animation is shorter than 1.9, you can't cast next skill before 1.9
            this.silence_end_timer.on(this.silence_duration)
            this._static.silence = 1
            if loglevel >= 2:
                log('silence','start')
            return 1

    def ac(this):
        this.cast_event()
        return 1


class Action(object):   
    _static = Static({
        'prev'     : 0 ,
        'doing'    : 0 ,
        'spd_func' : 0 ,
        })

    name = '_Action'
    index = 0
    recover_start = 0
    startup_start = 0
    _startup = 0
    _recovery = 0
    status = -2 # -2nop -1startup 0doing 1recovery
    idle = 0

    class Nop(object):
        name = '__idle__'
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
            this.conf = conf
            this._startup = conf[this.name+'_startup']
            this._recovery = conf[this.name+'_recovery']
            
        if act != None:
            this.act = act

        if this._static.spd_func == 0:
            this._static.spd_func = this.nospeed
        if this._static.doing == 0:
            this._static.doing = this.nop
        if this._static.prev == 0:
            this._static.prev = this.nop

        this.cancel_by = []
        this.interrupt_by = []

        this.startup_timer = Timer(this._cb_acting)
        this.recovery_timer = Timer(this._cb_act_end)
        this.idle_event = Event('idle')
        this.act_event = Event(this.name)

        this.Event = Event
        this.Buff = Buff
        this.Debuff = Debuff
        this.Selfbuff = Selfbuff
        this.Teambuff = Teambuff
        this.Modifier = Modifier
        this.log = log


    def __call__(this):
        return this.tap()
    
    def getdoing(this):
        return this._static.doing
    def _setdoing(this):
        this._static.doing = this
    def getprev(this):
        return this._static.prev
    def _setprev(this):
        this._static.prev = this._static.doing

    def rt_tap(this):
        if this.rt_name != this.name:
            this.rt_name = this.name
            this._startup = this.conf[this.name+'_startup']
            this._recovery = this.conf[this.name+'_recovery']
            this.act_event = Event(this.name)
        this.o_tap()

    def realtime(this):
        this.rt_name = this.name
        this.tap, this.o_tap = this.rt_tap, this.tap

    def reinit(this, name=None, conf=None, act=None):  
        if name != None:
            if type(name) == tuple:
                this.name = name[0]
                this.index = name[1]
            else:
                this.name = name
                this.index = 0
        if conf != None:
            this.conf = conf
            this._startup = conf[this.name+'_startup']
            this._recovery = conf[this.name+'_recovery']
            
        if act != None:
            this.act = act

        this.act_event = Event(this.name)


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
            this.act(this)
            this.status = 1
            this.recover_start = now() 
            this.recovery_timer.on(this.getrecovery())


    def _cb_act_end(this, e):
        if this.getdoing() == this:
            if loglevel >= 2:
                log('ac_end',this.name)
            this.status = -2
            this._setprev() # turn this from doing to prev
            this._static.doing = this.nop
            this.idle_event()


    def act(this, action):
        if loglevel >= 2:
            log('act',this.name)
        this.act_event()


    def tap(this):
        doing = this._static.doing

        if doing.idle :
            if loglevel >= 2:
                log('tap',this.name, None, 'idle')
        else:
            if loglevel >= 2:
                log('tap',this.name, None, 'doing '+doing.name)

        if doing == this : # self is doing
            return 0

        #if doing.idle # idle
        #    pass
        if not doing.idle : # doing != this
            if doing.status == -1: # try to interrupt an action
                if this.name in doing.interrupt_by : # can interrupt action
                    log('interrupt', doing.name , 'by '+this.name+'\t', 'after %.2fs'%(now()-doing.startup_start) )
                else:
                    return 0
            elif doing.status == 1: # try to cancel an action
                if this.name in doing.cancel_by : # can interrupt action
                    log('cancel', doing.name , 'by '+this.name+'\t', 'after %.2fs'%(now()-doing.recover_start) )
                else:
                    return 0
            elif doing.status == 0:
                print 'err in action tap()'
                exit()
            this._setprev()
        this.status = -1
        this.startup_start = now()
        this.startup_timer.on(this.getstartup())
        this._setdoing()
        return 1



class Adv(object):
    # vvvvvvvvv rewrite this to provide advanced tweak vvvvvvvvvv
    adv_name = None
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
    def pre(this):
        pass
    def init(this): 
        pass
    #def condition(this):
    #    return ''
    # ^^^^^^^^^ rewrite this to provide advanced tweak ^^^^^^^^^^

    comment = ''
    #x_status = (0,0)
    conf = {}

    conf_default = { 
        'latency' : {'x':0.05, 'sp':0.05, 'default':0.05, 'idle':0},
        'latency' : {'x':0.00, 'sp':0.00, 'default':0.00, 'idle':0},

        's1_dmg'      : 0   ,
        's1_sp'       : 0   ,
        's1_startup'  : 0.1 ,
        's1_recovery' : 1.9 ,

        's2_dmg'      : 0   ,
        's2_sp'       : 0   ,
        's2_startup'  : 0.1 ,
        's2_recovery' : 1.9 ,

        's3_dmg'      : 0   ,
        's3_sp'       : 0   ,
        's3_startup'  : 0.1 ,
        's3_recovery' : 1.9 ,

        'dodge_startup'  : 0  ,
        'dodge_recovery' : 43 / 60.0  ,

        'fsf_startup'  : 0          ,
        'fsf_recovery' : 41 / 60.0  ,

        }

    conf_default['acl'] = '''
        `s1
        `s2
        `s3
    '''

    acl_prepare_default = '''
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
        #fsf=this.fsf
        #dodge=this.dodge
    '''
        #if pin[-2:] == '-x':\n    s=pidx\n    sx=pidx\n    print sx\n    print pin\n    exit()

    def preconfig(this,conf={}):
        tmpconf = {}
        tmpconf.update(this.conf_default)
        tmpconf.update(globalconf.get(this.adv_name))
        tmpconf.update(this.conf)
        tmpconf.update(conf)
        if 'adv_name' in tmpconf :
            if this.adv_name != tmpconf['adv_name']:
                if this.adv_name == this.__class__.__name__:
                    this.adv_name = tmpconf['adv_name']
                    this.setconf(conf)
                    return

        this.conf = tmpconf
        this.conf['base_str'] = this.calc_str(this.conf)
        #this.base_str = this.conf['base_str']
        this.base_str = this.calc_str(this.conf) 

    def setconfig(this,conf={}):
        this.preconfig(conf)

        # set buff
        this.action = Action()
        this.action._static.spd_func = this.speed
        # set buff
        this.buff = Buff()
        this.all_buffs = []
        this.buff._static.all_buffs = this.all_buffs
        this.buff._static.time_func = this.bufftime
        # set modifier
        this.modifier = Modifier(0,0,0,0)
        this.all_modifiers = []
        this.modifier._static.all_modifiers = this.all_modifiers

        # init actions
        this.a_s1 = Action(('s1',1),this.conf)
        this.a_s2 = Action(('s2',2),this.conf)
        this.a_s3 = Action(('s3',3),this.conf)
        this.a_x1 = Action(('x1',1),this.conf)
        this.a_x2 = Action(('x2',2),this.conf)
        this.a_x3 = Action(('x3',3),this.conf)
        this.a_x4 = Action(('x4',4),this.conf)
        this.a_x5 = Action(('x5',5),this.conf)

        this.a_dodge = Action('dodge', this.conf)
        this.a_fsf = Action('fsf', this.conf)


        fsconf = {}
        xnfsconf = {}
        xn = {}
        for i in this.conf:
            if i[:3] == 'fs_':
                fsconf[i] = this.conf[i]
            if i[2:5] == 'fs_':
                xnfsconf[i] = this.conf[i]
                xn[i[:4]] = 1
        this.a_fs = Action('fs',fsconf)

        for i in ['x1fs','x2fs','x3fs','x4fs','x5fs']:
            tmpconf = {}
            for j in xnfsconf:
                if j[:4] == i:
                    tmpconf[j[2:]] = xnfsconf[j]
            if tmpconf == {}:
                setattr(this, 'a_'+i,  this.a_fs )
            else:
                for j in fsconf:
                    if j not in tmpconf:
                        tmpconf[j] = fsconf[j]
                setattr(this, 'a_'+i,  Action('fs' ,tmpconf) )

        this.a_x1.cancel_by = ['dodge','fs','fsf','s1','s2','s3']
        this.a_x2.cancel_by = ['dodge','fs','fsf','s1','s2','s3']
        this.a_x3.cancel_by = ['dodge','fs','fsf','s1','s2','s3']
        this.a_x4.cancel_by = ['dodge','fs','fsf','s1','s2','s3']
        this.a_x5.cancel_by = ['dodge','fs','fsf','s1','s2','s3']
        this.a_fs.cancel_by = ['dodge','s1','fsf','s2','s3']
        this.a_x1fs.cancel_by = ['dodge','s1','s2','s3']
        this.a_x2fs.cancel_by = ['dodge','s1','s2','s3']
        this.a_x3fs.cancel_by = ['dodge','s1','s2','s3']
        this.a_x4fs.cancel_by = ['dodge','s1','s2','s3']
        this.a_x5fs.cancel_by = ['dodge','s1','s2','s3']

        this.a_x1.interrupt_by = ['dodge', 'fs','fsf','s1','s2','s3']
        this.a_x2.interrupt_by = ['dodge', 'fs','fsf','s1','s2','s3']
        this.a_x3.interrupt_by = ['dodge', 'fs','fsf','s1','s2','s3']
        this.a_x4.interrupt_by = ['dodge', 'fs','fsf','s1','s2','s3']
        this.a_x5.interrupt_by = ['dodge', 'fs','fsf','s1','s2','s3']
        this.a_fs.interrupt_by = ['s1','s2','s3']
        this.a_x1fs.interrupt_by = ['s1','s2','s3']
        this.a_x2fs.interrupt_by = ['s1','s2','s3']
        this.a_x3fs.interrupt_by = ['s1','s2','s3']
        this.a_x4fs.interrupt_by = ['s1','s2','s3']
        this.a_x5fs.interrupt_by = ['s1','s2','s3']

        this.s1 = Skill('s1',this.conf['s1_sp'],this.a_s1.tap)
        this.s2 = Skill('s2',this.conf['s2_sp'],this.a_s2.tap)
        this.s3 = Skill('s3',this.conf['s3_sp'],this.a_s3.tap)

        if this.conf['x_type']== 'ranged':
            this.l_x = this.l_range_x
            this.l_fs = this.l_range_fs
            #this.fs_success = this.range_fs_sucess
        elif this.conf['x_type']== 'melee':
            this.l_x = this.l_melee_x
            this.l_fs = this.l_melee_fs
            #this.fs_success = this.melee_fs_success

        # set cmd
        this.x1 = this.a_x1
        this.x2 = this.a_x2
        this.x3 = this.a_x3
        this.x4 = this.a_x4
        this.x5 = this.a_x5
        #this.fs = this.a_fs
        this.fsf = this.a_fsf
        this.dodge = this.a_dodge


        for i in this.conf:
            if i[:3] == 'mod':
                j = this.conf[i]
                if type(j) == tuple:
                    Modifier(i,*j)
                elif type(j) == list:
                    idx = 0
                    for k in j:
                        Modifier(i+'_%d'%idx,*k)
                        idx += 1

    def calc_str(this, conf):
        base_str = conf['str_wp']+conf['str_w']
        tmp_str = 0
        if conf['element'] == 'flame':
            tmp_str = conf['str_adv'] * (1+0.15+0.23+0.04)
        elif conf['element'] == 'water':
            tmp_str = conf['str_adv'] * (1+0.15+0.23+0.07+0.07)
        elif conf['element'] == 'wind':
            tmp_str = conf['str_adv'] * (1+0.15+0.23+0.07)
        elif conf['element'] == 'light':
            tmp_str = conf['str_adv'] * (1+0.15+0.23+0.07+0.07)
        elif conf['element'] == 'shadow':
            tmp_str = conf['str_adv'] * (1+0.15+0.23+0.07)

        base_str += tmp_str

        tmp_str = 0
        tmp_str = conf['str_d']

        base_str += tmp_str

        #conf['base_str'] = int(base_str)
        return int(base_str)




    def __init__(this,conf={},cond=0):
        this.conf_init = conf
        this.ctx = Ctx().on()
        this.condition = m_condition.on
        this.m_condition = m_condition
        this.m_condition.set(cond)
        this._log = []
        loginit(this._log)
        

        if not this.adv_name:
            this.adv_name = this.__class__.__name__

        this.preconfig(conf)

        if 1:
            this.crit_mod = this.solid_crit_mod
        else:
            this.crit_mod = this.rand_crit_mod

        this.skill = Skill()
        this._acl = None

        #this.ctx.off()


    def dmg_mod(this, name):
        if name[:2] == 'o_':
            name = name[2:]
        #if name.find('o_') != -1:
        #    name = name.replace('o_','')
            
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
        for i in this.all_modifiers:
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
        m = {'chance':0, 'dmg':0, 'damage':0, 'passive':0, 'rate':0,}
        for i in this.all_modifiers:
            if 'crit' == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    print 'err in crit_mod'
                    exit()
        chance = m['chance']+m['passive']+m['rate']
        if chance > 1:
            chance = 1
        cdmg = m['dmg'] + m['damage'] + 1.7
        average = chance * (cdmg-1) + 1
        return average
    
    def rand_crit_mod(this):
        m = {'chance':0, 'dmg':0, 'damage':0, 'passive':0}
        for i in this.all_modifiers:
            if 'crit' == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    print 'err in crit_mod'
                    exit()
        chance = m['chance']+m['passive']
        if chance > 1:
            chance = 1
        cdmg = m['dmg'] + m['damage'] + 1.7
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

    def bufftime(this):
        return this.mod('buff')

    def l_idle(this, e):
        this.think_pin('idle')
        prev = this.action.getprev()
        if prev.name[0] == 's':
            this.think_pin(prev.name)
        if this.skill._static.first_x_after_s :
            this.skill._static.first_x_after_s = 0
            s_prev = this.skill._static.s_prev
            this.think_pin('%s-x'%s_prev)
        this.x()


    def getxseq(this):
        doing = this.action.getdoing()
        if doing.name[0] == 'x':
            return doing.index, doing.status
        else:
            return doing.name, doing.index


    def getprev(this):
        prev = this.action.getprev()
        return prev.name, prev.index, prev.status


    def fs(this):
        doing = this.action.getdoing()
        if doing.name[0] == 'x':
            a = getattr(this, 'a_'+doing.name+'fs')
            return a()
        else:
            return this.a_fs()

    def x(this):
        prev = this.action.getprev() 
        x_next = 1
        if prev.name[0] == 'x':
            if prev.index != 5:
                x_next = prev.index + 1

        a = getattr(this, 'x%d'%x_next)()
        return 1
    

    def l_range_x(this, e):
        xseq = e.name
        dmg_coef = this.conf['%s_dmg'%xseq]
        sp_gain = this.conf['%s_sp'%xseq] 
        if xseq == 'x5':
            log('x', '%s'%xseq, 0,'-------------------------------------c5')
        else:
            log('x', '%s'%xseq, 0)

        missile_timer = Timer(this.cb_missile, this.conf['missile_iv'][xseq] )
        missile_timer.dname = '%s_missile'%xseq
        missile_timer.amount = dmg_coef
        missile_timer.samount = sp_gain
        missile_timer()

        this.think_pin('x')

    def cb_missile(this, t):
        this.dmg_make(t.dname, t.amount)
        this.charge(t.dname, t.samount)

    
    def l_melee_x(this, e):
        xseq = e.name
        dmg_coef = this.conf['%s_dmg'%xseq]
        sp = this.conf['%s_sp'%xseq] 
        if xseq == 'x5':
            log('x', '%s'%xseq, 0,'-------------------------------------c5')
        else:
            log('x', '%s'%xseq, 0)
        this.dmg_make('%s'%xseq, dmg_coef)
        this.think_pin('x')
        this.charge('%s'%xseq, sp)


    def run(this, d = 300):
        this.pre()
        this.ctx.on()

        this.setconfig()

        this.l_idle        = Listener('idle',this.l_idle)
        this.l_x           = Listener(['x1','x2','x3','x4','x5'],this.l_x)
        this.l_fs          = Listener(['fs','x1fs','x2fs','x3fs','x4fs','x5fs'],this.l_fs)
        this.l_s           = Listener(['s1','s2','s3'],this.l_s)
        this.l_silence_end = Listener('silence_end' , this.l_silence_end  )
        this.l_dmg_make    = Listener('dmg_make'    , this.l_dmg_make     )
        this.l_true_dmg    = Listener('true_dmg'    , this.l_true_dmg     )
        this.l_dmg_formula = Listener('dmg_formula' , this.l_dmg_formula  )

        #e = Event()
        #e.listener(this.l_idle        , 'idle')
        #e.listener(this.l_x  , ['x1', 'x2' ,'x3', 'x4', 'x5'] )
        #e.listener(this.l_fs , ['fs', 'x1fs', 'x2fs', 'x3fs', 'x4fs', 'x5fs'] )
        #e.listener(this.l_s  , ['s1', 's2', 's3'] )
        #e.listener(this.l_silence_end , 'silence_end')
        #e.listener(this.l_dmg_make    , 'dmg_make')
        #e.listener(this.l_true_dmg    , 'true_dmg')
        #e.listener(this.l_dmg_formula , 'dmg_formula')

        this.init()

        this.ctx.on()

        Event('idle')()

        if not this._acl:
            this._acl, this._acl_str = acl.acl_func_str(
                    this.acl_prepare_default+this.conf['acl'] 
                    )

        Timeline.run(d)


    def think_pin(this, pin):
        def cb_think(t):
            if loglevel >= 2:
                log('think', t.pin, t.dname)
            this._acl(this, t)

        if pin in this.conf['latency'] :
            latency = this.conf['latency'][pin]
        else:
            latency = this.conf['latency']['default']

        t = Timer(cb_think).on(latency)
        doing = this.action.getdoing()
        t.pin = pin
        t.dname = doing.name
        t.dstat = doing.status
        t.didx = doing.index


    def l_silence_end(this, e):
        doing = this.action.getdoing()
        sname = this.skill._static.s_prev
        if doing.name[0] == 'x':
            this.skill._static.first_x_after_s = 1
        else:
            this.think_pin(sname+'-x')  # best choice
        this.think_pin(sname)
        #if doing.name[0] == 's': 
        #   no_deed_to_do_anythin

    def charge_p(this, name, sp):
        if type(sp) == str and sp[-1] == '%':
            percent = int(sp[:-1])
            this.s1.charge(this.conf['s1_sp']*percent/100)
            this.s2.charge(this.conf['s2_sp']*percent/100)
            this.s3.charge(this.conf['s3_sp']*percent/100)
            log('sp', name, '%d%%   '%percent,'%d/%d, %d/%d, %d/%d'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )
            this.think_pin('prep')
            return


    def charge(this, name, sp): 
        sp = sp * this.sp_mod(name)
        this.s1.charge(sp)
        this.s2.charge(sp)
        this.s3.charge(sp)
        this.think_pin('sp')
        log('sp', name, sp,'%d/%d, %d/%d, %d/%d'%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )

    def l_dmg_formula(this, e):
        name = e.dname
        dmg_coef = e.dmg_coef
        if hasattr(e, 'dtype'):
            name = e.dtype
        if 'modifiers' in e.__dict__ :
            if e.modifiers!=None and e.modifiers != 0:
                this.all_modifiers = e.modifiers
        e.dmg = this.dmg_formula(name, dmg_coef)
        this.all_modifiers = this.modifier._static.all_modifiers
        e.ret = e.dmg
        return

    def dmg_formula(this, name, dmg_coef):
        att = 1.0 * this.att_mod() * this.base_str
        armor = 10.0 * this.def_mod()
        return 5.0/3 * dmg_coef * this.dmg_mod(name) * att/armor   # true formula 
        #return att/armor * dmg_coef * this.dmg_mod(name)

    def l_true_dmg(this, e):
        log('dmg', e.dname, e.count, e.comment)

    def l_dmg_make(this, e):
        dmg_make(e.dname, e.dmg_coef)

    def dmg_make(this, name, dmg_coef, dtype=None):
        if dtype == None:
            dtype = name
        count = this.dmg_formula(dtype, dmg_coef)
        log('dmg', name, count)
        this.dmg_proc(name, count)

    def dmg_make_withspshow(this, name, dmg_coef, dtype=None):
        if dtype == None:
            dtype = name

        count = this.dmg_formula(dtype, dmg_coef)
        
        if name[0] == 'x':
            spgain = this.conf[name[:2]+'_sp']
            log('dmg', name, count, '%d/%d, %d/%d, %d/%d (+%d)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        elif name[:2] == 'fs':
            spgain = this.conf['fs'+'_sp']
            log('dmg', name, count, '%d/%d, %d/%d, %d/%d (+%d)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        else:
            spgain = 0
            if name[:2]+'_sp' in this.conf:
                spgain = this.conf[name[:2]+'_sp']
            log('dmg', name, count, '%d/%d, %d/%d, %d/%d (-%d)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )

        this.dmg_proc(name, count)


    def l_melee_fs(this, e):
        log('fs','succ')
        dmg_coef = this.conf['fs_dmg']
        this.dmg_make('fs', dmg_coef)
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge('fs',this.conf['fs_sp'])

    def l_range_fs(this, e):
        log('fs','succ')
        dmg_coef = this.conf['fs_dmg']
        sp_gain = this.conf['fs_sp']
        missile_timer = Timer(this.cb_missile, this.conf['missile_iv']['fs'] )
        missile_timer.dname = 'fs_missile'
        missile_timer.amount = dmg_coef
        missile_timer.samount = sp_gain
        missile_timer()
        this.fs_proc(e)
        this.think_pin('fs')


    def l_s(this, e):
        prev, index, stat = this.getprev()
        if prev == 'fs':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after fs)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name) )
        elif prev[0] == 'x':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after c%s)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, index ) )
        else:
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after %s)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, prev ) )

        dmg_coef = this.conf[e.name+'_dmg']
        if dmg_coef :
            this.dmg_make(e.name , dmg_coef)

        if e.name+'_buff' in this.conf:
            buffarg = this.conf[e.name+'_buff']
            wide = buffarg[0]
            buffarg = buffarg[1:]
            if wide == 'team':
                Teambuff(e.name, *buffarg).on()
            elif wide == 'self':
                Selfbuff(e.name, *buffarg).on()
            elif wide == 'debuff':
                Debuff(e.name, *buffarg).on()
            else:
                Buff(e.name, *buffarg).on()


        func = e.name + '_proc'
        getattr(this, func)(e)



if __name__ == '__main__':
    print 'to use adv_test'

