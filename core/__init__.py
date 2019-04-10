import copy

class lobject(object):
    def __init__(this, conf={}):
        for i in conf:
            this[i] = conf[i]

    def __getitem__(this, i):
        return this.__getattribute__(i)

    def __next__(this):
        return this.__dict__.__next__()

    def __iter__(this):
        return this.__dict__.__iter__()

    def __setitem__(this, i, v):
        this.__setattr__(i,v)

    def __delitem__(this, i):
        v = this.__getattribute__(i)
        del(v)

   # def __repr__(this):
   #     ret = ''
   #     line = ''
   #     for i in this.__dict__:
   #         line = '%s='%i
   #         line += this.__dict__[i]
   #         line += '\n'
   #         ret += line
   #     return ret

#} //class lobject


class Conf(lobject):
    __parentname = None
    __name = None

    def __repr__(this):
        ret = ''
        ret2 = ''
        this = copy.deepcopy(this)
        if not this.__parentname and not this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    ret2 += str(i)
                elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not this.__parentname and this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(this.__name)
                    ret2 += str(i)
                elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s=%s\n'%(this.__name, k, repr(i))
        else :
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s.%s'%(this.__parentname, this.__name)
                    ret2 += str(i)
                elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s.%s=%s\n'%(this.__parentname, this.__name, k, repr(i))
        return ret+ret2

    @staticmethod
    def update(this, a):
        if type(a) == Conf:
            for k,i in a.__dict__.items():
                this[k] = i
        elif type(a) == dict:
            for k,i in a.items():
                this[k] = i

    @staticmethod
    def update_re(this, a):
        if type(a) == Conf:
            for k,i in a.__dict__.items():
                if type(i) == Conf:
                    if type(this[k]) == Conf:
                        Conf.update_re(this[k], i)
                this[k] = i
        elif type(a) == dict:
            for k,i in a.items():
                this[k] = i

    def __add__(this, a):
        if type(a) != Conf:
            print('Conf can only add Conf')
            errrrrrrrrrrrrrrrrrrrr()
            return
        merge = copy.deepcopy(this)
        for k,i in a.__dict__.items():
            if k not in merge:
                merge[k] = i
            elif type(i) == Conf and type(merge[k]) == Conf:
                merge[k] = merge[k] + i
            else:
                merge[k] = i
        return merge

    @staticmethod
    def show(this):
        print this.__repr__()

    def __foo(this):
        pass

# all method in conf will be sync funtion, so use [function] to set a config to function
    @staticmethod
    def sync(this):
        def foo():
            pass
        for k,i in this.__dict__.items():
            if type(i) == Conf:
                Conf.sync(i)
            elif type(i) == type(this.__foo):
                i()
            elif type(i) == type(foo):
                i()


class Test(object):
    def d1(this):
        print 'd1'


if __name__ == '__main__':
    def test():
        print 'test'

    a = Conf()
    a.a = 'test'
    a.b = Conf()
    a.b.a = 'foo'
    a.b.b = Conf()
    a.b.b.a = 'foo'

    b = Conf()
    b.b = Conf()
    b.b.a = 'bar'

    c = a+b
    print c
    exit()



    c.b.d.a = 'bara'
    c.b.d.b = 'barb'
    c.b.d.c = Conf()
    c.b.d.c.zz = 'zz'
    c.b.d.c.yy = Conf()
    c.b.d.c.yy.tt = 'tt'
    c.b.e = 'baz'
    c.c = test
    t = Test()
    c.d = t.d1

    #c.b.d.show()
    #c.show()
    Conf.sync(c)


