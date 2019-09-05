
class Hits(object):
    def __init__(this, host, hitattr):
        this.host = host
        this.hitattr = hitattr
        this.timer = []
        idx = 0
        for i in hitattr :
            idx += 1
            t = Timer(this.cb, i)
            t.idx = idx
            this.timer.append(t)


    def on(this):
        for i in this.timer :
            i.on()


    def off(this):
        for i in this.timer :
            i.off()

    
    def cb(this, t):
        this.host._act(t.idx)


class characterbase(object):
    base_atk = 2000
    base_def = 10
    hp = 0
    od = 0
    bk = 0
