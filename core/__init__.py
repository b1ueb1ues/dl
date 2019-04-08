
class lobject(object):
    def __init__(this, conf):
        for i in conf:
            this[i] = conf[i]

    def __getitem__(this, i):
        return this.__getattribute__(i)

    def __setitem__(this, i, v):
        this.__setattr__(i,v)

    def __delitem__(this, i):
        v = this.__getattribute__(i)
        del(v)

#} //class Static

