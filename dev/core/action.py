from ctx import *

class Action(object):   
    __static = {}
    
    name = '_Action'
    index = 0
    recover_start = 0
    startup_start = 0
    __startup = 0
    __recovery = 0
    status = -2 # -2nop -1startup 0doing 1recovery
    idle = 0

    class Nop(object):
        name = '__idle__'
        index = 0
        status = -2
        idle = 1

    nop = Nop()

    @classmethod
    def init(cls):
        cls.__static['prev'] = cls.nop
        cls.__static['doing'] = cls.nop
        cls.__static['spd'] = cls.nospeed


    def __init__(this, name=None, conf=None):  ## can't change name after this
        # conf : startup, recovery, active, action
        if name != None:
            if type(name) == tuple:
                this.name = name[0]
                this.index = name[1]
            else:
                this.name = name
                this.index = 0


        def sync_config(c):
            this.__startup = c.startup
            this.__recovery = c.recovery
            this.__active = c.active
            if 'action' in c:
                this.act = c.action

        if not conf :
            this.conf = conf
            this.conf.sync_action = this.sync_config
        else:
            this.conf = Conf()
            this.conf.sync_action = this.sync_config
            this.conf.startup = 0.1
            this.conf.recovery = 1.9

        this.cancel_by = []
        this.interrupt_by = []

        this.startup_timer = Timer(this._cb_acting)
        this.recovery_timer = Timer(this._cb_act_end)
        this.e_idle = Event('idle')


    def __call__(this):
        return this.tap()
    
   # def get_doing(this):
   #     return this.__static['doing']
   # def set_doing(this):
   #     this.__static['doing'] = this
   # def get_prev(this):
   #     return this.__static['prev']
   # def set_prev(this):
   #     this.__static['prev'] = this.__static['doing']


    def get_recovery(this):
        return this.__recovery / this.speed()


    def get_startup(this):
        return this.__startup / this.speed()


    def nospeed(this):
        return 1


    def speed(this):
        return this.__static['spd']()


    def _cb_acting(this, e):
        if this.__static['doing'] == this:
            this.status = 0
            this._act(1)
            this.status = 1
            this.recover_start = now() 
            this.recovery_timer(this.get_recovery())


    def _cb_act_end(this, e):
        if this.__static['doing'] == this:
            if loglevel >= 2:
                log('ac_end',this.name)
            this.status = -2
            this.__static['doing'] = this # turn this from doing to prev
            this._static.doing = this.nop
            this.idle_event()


    def _act(this, partidx):
        this.idx = partidx
        if loglevel >= 2:
            log('act',this.name)
        this.act(this)


    def act(this, action):
        this.act_event.name = this.name
        this.act_event.idx = this.idx
        this.act_event()


    def tap(this):
        doing = this._static.doing

        if doing.idle :
            if loglevel >= 2:
                log('tap',this.name, this.atype+'\t', 'idle:%d'%doing.status)
        else:
            if loglevel >= 2:
                log('tap',this.name, this.atype+'\t', 'doing '+doing.name+':%d'%doing.status)

        if doing == this : # self is doing
            return 0

        #if doing.idle # idle
        #    pass
        if not doing.idle : # doing != this
            if doing.status == -1: # try to interrupt an action
                if this.atype in doing.interrupt_by : # can interrupt action
                    doing.startup_timer.off()
                    log('interrupt', doing.name , 'by '+this.name+'\t', 'after %.2fs'%(now()-doing.startup_start) )
                else:
                    return 0
            elif doing.status == 1: # try to cancel an action
                if this.atype in doing.cancel_by : # can interrupt action
                    doing.recovery_timer.off()
                    log('cancel', doing.name , 'by '+this.name+'\t', 'after %.2fs'%(now()-doing.recover_start) )
                else:
                    return 0
            elif doing.status == 0:
                print('err in action tap()')
                errrrrrrrrrrrr()
            this.__static['doing'] = this # turn this from doing to prev
        this.status = -1
        this.startup_start = now()
        this.startup_timer.on(this.getstartup())
        this.__static['doing'] = this # setdoing
        if now() <= 3:
            log('debug','tap,startup', this.getstartup())
        return 1


if __name__ == '__main__' :
    Action()
