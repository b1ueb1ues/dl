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


    def __init__(self):
        self.ctxdict_s = copy.deepcopy(self._vdict_s)


    def __upload(self):
        for i in range(len(self.ctxdict_s)):
            gdict = self._gdict_s[i]
            vdict = self.ctxdict_s[i]
            for k in vdict:
                gdict[k] = vdict[k]
        return self


    def __download(self):
        for i in range(len(self.ctxdict_s)):
            gdict = self._gdict_s[i]
            vdict = self.ctxdict_s[i]
            for k in vdict:
                vdict[k] = gdict[k]
        return self


    def on(self):
        if self._active[0] == None:
            self._active[0] = self
            self.__upload()
        else:
            self._active[0].__download()
            self.__upload()
            self._active[0] = self
        return self


    def off(self):
        if self._active[0] != self:
            print('try to turn off inactive ctx')
        for i in range(len(self.ctxdict_s)):
            gdict = self._gdict_s[i]
            vdict = self.ctxdict_s[i]
            for k in vdict:
                del(gdict[k])
        self.__download()
        self._active[0] = None
        return self

#} //class Ctx


class Static(object):
    def __init__(self, default):
        Ctx.register(self, default)

    def __getitem__(self, i):
        return self.__getattribute__(i)

    def __setitem__(self, i, v):
        self.__setattr__(i,v)

    def __delitem__(self, i):
        v = self.__getattribute__(i)
        del(v)

#} //class Static

