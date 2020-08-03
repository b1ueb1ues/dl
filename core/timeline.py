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
    def __init__(self, name=None):
        if name :
            self.name = name
            self.__name = name
            self._trigger = get_event_trigger(name)
        else:
            self._trigger = []


    def listener(self, cb, eventname = None):
        if eventname:
            if type(eventname) == list or type(eventname) == tuple:
                for i in eventname:
                    add_event_listener(i, cb)
            else:
                add_event_listener(eventname, cb)
        else:
            add_event_listener(self.__name, cb)


    def on(self, e=None):
        for i in self._trigger:
            i(self)

    def __call__(self, expand=None):
        self.on(self)

    # def __str__(self):
    #     return self.__name


    #__call__ = on

#} class Event

class Listener(object):
    def __init__(self, eventname, cb):
        self.__cb = cb
        self.__eventname = eventname
        self.__online = 0
        self.on()

    def __call__(self, e):
        self.__cb(e)

    def on(self, cb=None):
        if self.__online :
            return 
        if cb :
            self.__cb = cb
        if type(self.__eventname) == list or type(self.__eventname) == tuple:
            for i in self.__eventname:
                add_event_listener(i, self.__cb)
        else:
            add_event_listener(self.__eventname, self.__cb)
        self.__online = 1
        return self

    def pop(self):
        self.off()
        return self.__cb


    def off(self):
        if not self.__online:
            return 
        if type(self.__eventname) == list or type(self.__eventname) == tuple:
            for i in self.__eventname:
                els = get_event_trigger(i)
                idx = els.index(self.__cb)
                els.pop(idx)
        else:
            els = get_event_trigger(self.__eventname)
            idx = els.index(self.__cb)
            els.pop(idx)
        self.__online = 0
        return self

#} class Listener


class Timer(object):
    def __init__(self, proc=None, timeout=None, repeat=0, timeline=None):
        if proc:
            self.process = proc
        else:
            self.process = self._process

        if timeout :
            self.timeout = timeout
        else:
            self.timeout = 0

        if repeat :
            self.callback = self.callback_repeat
        else:
            self.callback = self.callback_once

        if timeline:
            self.timeline = timeline
        else:
            self.timeline = _g_timeline

        self.timing = 0
        self.online = 0
        self.pause_diff = 0
        #self.on()


    def on(self, timeout = None):
        if timeout:
            self.timeout = timeout
            self.timing = _g_now + timeout
        else:
            self.timing = _g_now + self.timeout

        if self.online == 0:
            self.online = 1
            self.timeline.add(self)
        return self


    def off(self):
        if self.online:
            self.online = 0
            self.timeline.rm(self)
        return self

    def add(self, time=0):
        self.timeout += time
        self.timing += time
        if self.timing + time < now():
            self.off()

    #alias
    disable = off
    enable = on
    __call__ = on


    def status(self):
        return self.online

    def callback_repeat(self):
        self.process(self)
        if self.timing == _g_now :
            self.timing += self.timeout

    def callback_once(self):
        self.process(self)
        if self.timing <= _g_now:
            if self.online:
                self.online = 0
                self.timeline.rm(self)

    def callback(self):
        pass


    def __str__(self):
        return '%f: Timer:%s'%(self.timing,self.process)

    def __repr__(self):
        return '%f: Timer:%s'%(self.timing,self.process)

    def _process(self):
        # sample plain _process
        print('-- plain timer ','@', t.timing)
        return 1


class Timeline(object):
    def __init__(self):
        self._tlist = []


    def add(self, t):
        self._tlist.append(t)


    def rm(self, t):
        i = self._tlist.index(t)
        return self._tlist.pop(i)


    def process_head(self):
        global _g_now
        tcount = len(self._tlist)
        if tcount == 0:
            return -1

        if tcount == 1:
            headtiming = self._tlist[0].timing  
            headindex = 0                          
        else: #if tcount >= 2: 
            headtiming = self._tlist[0].timing  
            headindex = 0                          
            for i in range(1,tcount):
                timing = self._tlist[i].timing
                if timing < headtiming:
                    headtiming = timing
                    headindex = i

        if headtiming >= _g_now:
            _g_now = headtiming
            headt = self._tlist[headindex]
            headt.callback()
        else:
            print('timeline time err', headtiming, _g_now)
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

    def _stop(self):
        global _g_stop
        _g_stop = 1


    def _run(self, last = 100):
        last += _g_now
        while 1:
            if _g_now > last:
                return _g_now

            r = self.process_head()
            if r == -1:
                return _g_now
            
            if _g_stop :
                return _g_now


    def __str__(self):
        return 'Timeline tlist: %s'%(str(self._tlist))

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
        def a3(self):
            print('-3',self.name)
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
