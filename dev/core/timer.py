

_g_now = 0
_g_timeline = 0


def now():
    return _g_now


def set_time(time):
    global _g_now
    _g_now = time


class Timeline(object):
    def __init__(this):
        this._tlist = []
        this._stop = 0


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
    

    def stop(this):
        this._stop = 1


    def run(this, last = 100):
        global _g_now
        last += _g_now
        while 1:
            if _g_now > last:
                this.now = _g_now
                return _g_now

            r = this.process_head()
            if r == -1:
                this.now = _g_now
                return _g_now
            
            if this._stop :
                this.now = _g_now
                return _g_now


    def __str__(this):
        return 'Timeline tlist: %s'%(str(this._tlist))

#} class Timeline


class Timer(object):
    @classmethod
    def init(cls, tl=None):
        global _g_now
        global _g_timeline
        if not tl:
            tl = {}
            tl['timeline'] = Timeline()
            tl['now'] = 0
        _g_timeline = tl['timeline']
        _g_now = tl['now']
        return tl
            
    def __init__(this, proc=None, timeout=None):
        if proc:
            this.process = proc
        else:
            this.process = this._process

        if timeout :
            this.timeout = timeout
        else:
            this.timeout = 0

        this.timeline = _g_timeline

        this.timing = 0
        this.__online = 0


    def on(this, timeout = None):
        global _g_now
        if timeout:
            this.timeout = timeout
            this.timing = _g_now + timeout
        else:
            this.timing = _g_now + this.timeout

        if this.timeout:
            if this.__online == 0:
                this.__online = 1
                this.timeline.add(this)
        return this


    def off(this):
        if this.__online:
            this.__online = 0
            this.timeline.rm(this)
        return this


    #alias
    disable = off
    enable = on
    repeat = on
    __call__ = on


    def status(this):
        return this.__online


    def callback(this):
        this.process(this)
        if this.timing <= _g_now:
            if this.__online:
                this.__online = 0
                this.timeline.rm(this)


    @classmethod
    def run(cls, duration=100):
        _g_timeline.run(duration)


    def __str__(this):
        return '%f: Timer:%s'%(this.timing, this.process)


    def __repr__(this):
        return '%f: Timer:%s'%(this.timing, this.process)


    def _process(this):
        # sample plain _process
        print('-- plain timer ','@', t.timing)
        return 1

#} class Timer


if __name__ == '__main__':
    tl = Timer.init()
    def test(t):
        print(t)
        t()
    t = Timer(test)(3)
    Timer.run(120)

