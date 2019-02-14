import copy

_g_statics         = None

_ctx_list = ['_g_now','_g_timeline','_g_event_listeners']
_g_now             = None
_g_timeline        = None
_g_event_listeners = None
gnow = 1

class Static(object):
    def __init__(this, default={}):
        global _g_statics
        this.__default = default
        for i in this.__default:
            this.__setattr__(i,this.__default[i])
        _g_statics.append(this)

    @classmethod
    def reset(cls, this):
        for i in this.__default:
            this.__setattr__(i,this.__default[i])

    @classmethod
    def save(cls, this):
        save = {}
        for i in this.__dict__:
            save[i] = copy.deepcopy(this.__dict__[i])
        return save

    @classmethod
    def load(cls, this, save):
        for i in save:
            this.__setattr__(i, save[i])
        return this.__dict__

_g_statics = []
a = Static({
    "a":1,
    "b":2,
    })

b = Static({
    "aa":11,
    "bb":22,
    'reset':1,
    })


def _static_off():
    global _g_statics
    _statics = {}
    for i in _g_statics:
        _statics[i]=Static.save(i)

def _static_on(save):
    global _g_statics

print a.a
print b.bb
        


def static(default):
    pass



class Ctx(object):
    _active = [None]


    def __init__(this):
        this._now = 0
        this._timeline = Timeline()
        this._event_listeners = {}


    def on(this):
        global _g_now
        global _g_timeline
        global _g_event_listeners

        if this._active[0] != None:
            this._active[0]._now             = _g_now
            this._active[0]._timeline        = _g_timeline
            this._active[0]._event_listeners = _g_event_listeners
        _g_now             = this._now
        _g_timeline        = this._timeline
        _g_event_listeners = this._event_listeners

        this._active[0] = this

        return this


    def save(this):
        global _g_now
        global _g_timeline
        global _g_event_listeners
        this._now             = _g_now
        this._timeline        = _g_timeline
        this._event_listeners = _g_event_listeners
        return this


    def off(this):
        if this._active[0] != this:
            print 'try to turn off inactive ctx'
            exit()

        global _g_now
        global _g_timeline
        global _g_event_listeners
        this.save()
        _g_now             = None
        _g_timeline        = None
        _g_event_listeners = None
        this._active[0] = None


    def now(this, newtime = None):
        if newtime:
            this._now = newtime
        return this._now


    def set_time(this,t):
        this._now = t

#}class Ctx


def now():
    return _g_now


def set_time(time):
    global _g_now
    _g_now = time


def add_event_listener(eventname, listener): #listener should be a function
    global _g_event_listeners

    if eventname in _g_event_listeners:
        _g_event_listeners[eventname].append(listener)
    else:
        _g_event_listeners[eventname] = [listener]


def get_event_trigger(eventname, trigger = []): 
    global _g_event_listeners
    if eventname in _g_event_listeners:
        return _g_event_listeners[eventname]
    else:
        _g_event_listeners[eventname] = []
        return _g_event_listeners[eventname]


class Event(object):
    def __init__(this, name=None):
        if name :
            this.name = name
            this._trigger = get_event_trigger(name)
        else:
            this._trigger = []


    def listener(this, cb, eventname = None):
        if eventname:
            if type(eventname) == list or type(eventname) == tuple:
                for i in eventname:
                    add_event_listener(i, cb)
            else:
                add_event_listener(eventname, cb)
        else:
            add_event_listener(this.name, cb)


    def on(this, e):
        for i in this._trigger:
            i(this)

    def __call__(this, expand=None):
        this.on(this)

    #__call__ = on

#} class Event


class Timer(object):
    def __init__(this, proc=None, timeout=None, repeat=0, timeline=None):
        if proc:
            this.process = proc
        else:
            this.process = this._process

        if timeout :
            this.timeout = timeout
        else:
            this.timeout = 0

        if repeat :
            this.callback = this.callback_repeat
        else:
            this.callback = this.callback_once

        if timeline:
            this.timeline = timeline
        else:
            this.timeline = _g_timeline

        this.timing = 0
        this.online = 0
        #this.on()


    def on(this, timeout = None):
        if timeout:
            this.timing = _g_now + timeout
        else:
            this.timing = _g_now + this.timeout

        if this.online == 0:
            this.online = 1
            this.timeline.add(this)
        return this


    def off(this):
        if this.online:
            this.online = 0
            this.timeline.rm(this)
        return this


    #alias
    disable = off
    enable = on
    __call__ = on


    def status(this):
        return this.online

    def callback_repeat(this):
        this.process(this)
        if this.timing == _g_now :
            this.timing += this.timeout

    def callback_once(this):
        this.process(this)
        if this.timing <= _g_now:
            if this.online:
                this.online = 0
                this.timeline.rm(this)

    def callback(this):
        pass


    def __str__(this):
        return "%f: Timer:%s"%(this.timing,this.process)

    def __repr__(this):
        return "%f: Timer:%s"%(this.timing,this.process)

    def _process(this):
        # sample plain _process
        print '-- plain timer ','@', t.timing
        return 1



class Timeline(object):
    def __init__(this):
        this._tlist = []


    def add(this, t):
        this._tlist.append(t)


    def rm(this, t):
        i = this._tlist.index(t)
        return this._tlist.pop(i)


    def process_head(this):
        global _g_now
        tcount = len(this._tlist)
        if tcount == 0:
            return -1

        if tcount == 1:
            headtiming = this._tlist[0].timing  
            headindex = 0                          
        else: #if tcount >= 2: 
            headtiming = this._tlist[0].timing  
            headindex = 0                          
            for i in range(1,tcount):
                timing = this._tlist[i].timing
                if timing < headtiming:
                    headtiming = timing
                    headindex = i

        if headtiming >= _g_now:
            _g_now = headtiming
            headt = this._tlist[headindex]
            headt.callback()
        else:
            print "timeline time err"
            exit()
        return 0
    

    def run(this, last = 100):
        last += _g_now
        while 1:
            if _g_now > last:
                return

            r = this.process_head()
            if r == -1:
                return


    def __str__(this):
        return "Timeline tlist: %s"%(str(this._tlist))

#} class Timeline



Ctx().on()


def main():
    class A():
        name = 'b'
        def a3(this):
            print '-3',this.name
    a = A()

    def a1():
        print '-1', now()
    def a2():
        e = Event('e3')
        e.test = 1
        e()
        print '-2', now()
 
    def lis(e):
        print "listener1"
    def lis2(e):
        print "listener2"
    def lis3(e):
        print "listener3"

    e1 = Timer(a1,1).on()

    Event('e3').listener(lis3)
    Event('e2').listener(lis)
    Event('e2').listener(lis2)

    e2 = Timer(a2,2).on()
    e3 = Timer(a.a3,3).on()

    _g_timeline.run()




if __name__ == '__main__' :
    main()
