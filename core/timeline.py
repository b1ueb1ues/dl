


__g_now = 0
#__g_active_timeline = 0

def now():
    global __g_now
    return __g_now
def set_time(time):
    global __g_now
    __g_now = time
    return 1


__g_event_listeners = {}

def add_event_listener(eventname,listener): #listener should be a function
    global __g_event_listeners

    if eventname in __g_event_listeners:
        __g_event_listeners[eventname].append(listener)
    else:
        __g_event_listeners[eventname] = [listener]

def get_event_trigger(eventname, trigger = []): 
    global __g_event_listeners
    if eventname in __g_event_listeners:
        return __g_event_listeners[eventname]
    else:
        __g_event_listeners[eventname] = []
        return __g_event_listeners[eventname]

def clean_event_listener(): 
    global __g_event_listeners
    __g_event_listeners = {}



class Event(object):

    def __init__(this, name, proc=None, timing=None, timeline=None):
        this.name = name

        if proc:
            this.process = proc
        else:
            this.process = this._process

        if timeline:
            this.timeline = timeline
        else:
            this.timeline = Timeline()

        if timing :
            this.timing = timing
        else:
            this.timing = now()

        if name :
            this._trigger = get_event_trigger(name)
        else:
            this._trigger = []

        this.online = 0
        #this.on()

    def __str__(this):
        return "%f: %s"%(this.timing,this.name)

    def __repr__(this):
        return "%f: %s"%(this.timing,this.name)
    


    def disable(this):
        if this.online:
            this.online = 0
            this.timeline.rm(this)
        return this
    #alias
    off = disable

    def status(this):
        return this.online

    def enable(this, timing = None):
        if timing:
            this.timing = timing
        if this.online == 0:
            this.online = 1
            this.timeline.add(this)
        return this
    #alias
    on = enable


    def callback(this):
        this.process(this)
        this.trigger()
        if this.timing <= now():
            if this.online:
                this.online = 0
                this.timeline.rm(this)

    def listener(this, cb,  eventname = None):
        if eventname:
            add_event_listener(eventname, cb)
        else:
            add_event_listener(this.name, cb)


    def trigger(this, triggername = None):
        if triggername:
            trigger = get_event_trigger(triggername)
        else:
            trigger = this._trigger
        for i in trigger:
            i(this)


    @staticmethod
    def _process(e):
        # sample plain _process
        print '-- plain event ',e.name ,'@', e.timing
        return 1


class Repeat_event(Event):
    def __init__(this, name, proc=None, interval=10, timing=None):
        super(Repeat_event,this).__init__(name, proc, timing)
        this.interval = interval

    def callback(this):
        this.process(this)
        if this.timing == now():
            this.timing += this.interval



class Timeline(object):
    _active = [0]
    _now = 0
    _listenerlist = []
    _eventlist = []

    @classmethod
    def setup(cls):
        cls.activeContext[0] = object.__new__(cls)


    @classmethod
    def reset(cls):
        cls._active = [0]
        set_time(0)
        clean_event_listener()
        return Timeline()

    def __init__(this):
        if this._active[0]:
            return
        this._listenerlist = []
        this._eventlist = []

    def __new__(cls):
        if not cls._active[0] :
            cls._active[0] = object.__new__(cls)
        return cls._active[0]


    def __str__(this):
        return "Timeline Eventlist: %s"%(str(this._eventlist))


    def add(this, event):
        this._eventlist.append(event)


    def addlistener(this, listener):
        this._listenerlist.append(listener)


    def rm(this, event):
        i = this._eventlist.index(event)
        return this._eventlist.pop(i)


    def process_head(this):
        global __g_now
        eventcount = len(this._eventlist)
        if eventcount == 0:
            return -1

        if eventcount == 1:
            headtiming = this._eventlist[0].timing  
            headindex = 0                          
        else: #if eventcount >= 2: 
            headtiming = this._eventlist[0].timing  
            headindex = 0                          
            for i in range(1,eventcount):
                timing = this._eventlist[i].timing
                if timing < headtiming:
                    headtiming = timing
                    headindex = i

        if headtiming >= now():
            set_time(headtiming)
            headevent = this._eventlist[headindex]
            headevent.callback()
            for i in this._listenerlist:
                i(headevent)
        else:
            print "timeline time err"
            exit()
        return 0
    
    @classmethod
    def run(cls, last = 100):
        last += now()
        while 1:
            if now() > last:
                return
            r = cls.process_head(cls._active[0])
            if r == -1:
                return


def main():

    def a1(e):
        print '-1',e.name, e.timing
        e.trigger('e3')
    def a2(e):
        print '-2',e.name, e.timing

    def lis():
        print "listener1"
    def lis2():
        print "listener2"
    def lis3():
        print "listener3"

    e1 = Event("e1",a1,1)

    add_event_listener("e3",lis3)


    add_event_listener("e2",lis)
    add_event_listener("e2",lis2)

    e2 = Event("e2",a2,2)

    Timeline().run()




if __name__ == '__main__' :
    main()
