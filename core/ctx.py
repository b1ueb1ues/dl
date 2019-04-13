import copy

class Ctx(object):
    _active = [None]
    _gdict_s = []
    _vdict_s = []

    @classmethod
    def register(cls, gdict, vdict):
        cls._gdict_s.append(gdict)
        cls._vdict_s.append(vdict)
        if cls._active[0] != None:
            for k in vdict:
                gdict[k] = vdict[k]
            cls._active[0].__init__()


    def __init__(this):
        this.ctxdict_s = copy.deepcopy(this._vdict_s)


    def __upload(this):
        for i in range(len(this.ctxdict_s)):
            gdict = this._gdict_s[i]
            vdict = this.ctxdict_s[i]
            for k in vdict:
                gdict[k] = vdict[k]
        return this


    def __download(this):
        for i in range(len(this.ctxdict_s)):
            gdict = this._gdict_s[i]
            vdict = this.ctxdict_s[i]
            for k in vdict:
                vdict[k] = gdict[k]
        return this


    def on(this):
        if this._active[0] == None:
            this._active[0] = this
            this.__upload()
        else:
            this._active[0].__download()
            this.__upload()
            this._active[0] = this
        return this


    def off(this):
        if this._active[0] != this:
            print('try to turn off inactive ctx')
            errrrrrrrrrrrr()
        for i in range(len(this.ctxdict_s)):
            gdict = this._gdict_s[i]
            vdict = this.ctxdict_s[i]
            for k in vdict:
                del(gdict[k])
        this.__download()
        this._active[0] = None
        return this

#} //class Ctx


class Static(object):
    def __init__(this, default):
        Ctx.register(this, default)

    def __getitem__(this, i):
        return this.__getattribute__(i)

    def __setitem__(this, i, v):
        this.__setattr__(i,v)

    def __delitem__(this, i):
        v = this.__getattribute__(i)
        del(v)

#} //class Static

