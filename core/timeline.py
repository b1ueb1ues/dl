from core.ctx import *
import core.log


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


    def on(this, e=None):
        for i in this._trigger:
            i(this)

    def __call__(this, expand=None):
        this.on(this)

    #__call__ = on

#} class Event

class Listener(object):
    def __init__(this, eventname, cb):
        this.__cb = cb
        this.__eventname = eventname
        this.__online = 0
        this.on()

    def __call__(this, e):
        this.__cb(e)

    def on(this, cb=None):
        if this.__online :
            return 
        if cb :
            this.__cb = cb
        if type(this.__eventname) == list or type(this.__eventname) == tuple:
            for i in this.__eventname:
                add_event_listener(i, this.__cb)
        else:
            add_event_listener(this.__eventname, this.__cb)
        this.__online = 1
        return this

    def pop(this):
        this.off()
        return this.__cb


    def off(this):
        if not this.__online:
            return 
        if type(this.__eventname) == list or type(this.__eventname) == tuple:
            for i in this.__eventname:
                els = get_event_trigger(i)
                idx = els.index(this.__cb)
                els.pop(idx)
        else:
            els = get_event_trigger(this.__eventname)
            idx = els.index(this.__cb)
            els.pop(idx)
        this.__online = 0
        return this

#} class Listener


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
            this.timeout = timeout
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
        return '%f: Timer:%s'%(this.timing,this.process)

    def __repr__(this):
        return '%f: Timer:%s'%(this.timing,this.process)

    def _process(this):
        # sample plain _process
        print('-- plain timer ','@', t.timing)
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
            print('timeline time err')
            exit()
        return 0
    
    @classmethod
    def run(cls, last = 100):
        global _g_timeline
        return _g_timeline._run(last)

    @classmethod
    def stop(cls, last = 100):
        global _g_timeline
        return _g_timeline._stop()

    def _stop(this):
        global _g_stop
        _g_stop = 1


    def _run(this, last = 100):
        last += _g_now
        while 1:
            if _g_now > last:
                return _g_now

            r = this.process_head()
            if r == -1:
                return _g_now
            
            if _g_stop :
                return _g_now


    def __str__(this):
        return 'Timeline tlist: %s'%(str(this._tlist))

#} class Timeline


Ctx().on()
Ctx.register(globals(),{
    '_g_now'             : 0 ,
    '_g_stop'            : 0 ,
    '_g_timeline'        : Timeline() ,
    '_g_event_listeners' : {} ,
    })




def main():
    class A():
        name = 'b'
        def a3(this):
            print('-3',this.name)
    a = A()

    def a1():
        print('-1', now())
    def a2():
        e = Event('e3')
        e.test = 1
        e()
        print('-2', now())
 
    def lis(e):
        print('listener1')
    def lis2(e):
        print('listener2')
    def lis3(e):
        print('listener3')

    e1 = Timer(a1,1).on()

    Event('e3').listener(lis3)
    Event('e2').listener(lis)
    Event('e2').listener(lis2)

    e2 = Timer(a2,2).on()
    e3 = Timer(a.a3,3).on()

    _g_timeline.run()




if __name__ == '__main__' :
    main()
