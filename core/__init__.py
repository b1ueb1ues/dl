import copy
#from adv import *

class lobject(object):
    def __init__(this, conf={}):
        for i in conf:
            this[i] = conf[i]

    def __getitem__(this, i):
        l = i.find('.')
        if l >= 1:
            p = i[:l]
            c = i[l+1:]
            return this.__getattribute__(p)[c]
        elif l < 0 and i != '':
            return this.__getattribute__(i)

    def __next__(this):
        return this.__dict__.__next__()

    def __iter__(this):
        return this.__dict__.__iter__()
    
    def __getattr__(this, k):
        if k[:2] != '__':
            i = this.__new__(this.__class__)
            this.__setattr__(k, i)
            return i
        else:
            return object.__getattr__(this,k)

    def __setitem__(this, i, v):
        l = i.find('.')
        if l >= 1:
            p = i[:l]
            c = i[l+1:]
            tmp = this.__new__(this.__class__)
            tmp.__setitem__(c,v)
            this.__setattr__(p,tmp)
            return 
        elif l < 0 and i != '':
            this.__setattr__(i,v)
            return
        print('can\' set item')
        errrrrrrrrrrr()
        return

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
    __sync = None

    def __init__(this, template={}):
        if type(template) == dict:
            this.__fromdict(template)
        if type(template) == this.__class__:
            this.__fromdict(template.__todict())


    def __todict(this):
        ret = {}
        for k,v in this.__dict__.items():
            if k[:7] == '_Conf__':
                continue
            if type(v) == this.__class__:
                ret[k] = v.__todict()
            elif type(v) == dict:
                ret[k] = ('__realdict',v)
            else:
                ret[k] = v
        return ret

    def __todict_all(this):
        ret = {}
        for k,v in this.__dict__.items():
            if type(v) == this.__class__:
                ret[k] = v.__todict()
            elif type(v) == dict:
                ret[k] = ('__realdict',v)
            else:
                ret[k] = v
        return ret

    def __fromdict(this,dic):
        if type(dic) != dict:
            print('err fromdict')
            errrrrrrrrr()
        for k,v in dic.items():
            if type(v) == tuple and v[0] == '__realdict':
                this[k] = v[1]
            elif type(v) == dict:
                tmp = this.__new__(this.__class__)
                tmp.__fromdict(v)
                this[k] = tmp
            else:
                this[k] = v

    def __str__(this):
        return this.__tostr()

    def __tostr(this):
        ret = ''
        ret2 = ''
        tmp = this.__new__(this.__class__)
        tmp.__init__(this.__todict_all())
        this = tmp
        #this = copy.deepcopy(this)
        if not this.__parentname and not this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not this.__parentname and this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(this.__name)
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= this.__name+'.'+k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s=%s\n'%(this.__name, k, repr(i))
        else :
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s.%s'%(this.__parentname, this.__name)
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= this.__parentname+'.'+this.__name+'.'+k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s.%s=%s\n'%(this.__parentname, this.__name, k, repr(i))
        return ret+ret2

    @staticmethod
    def showsync(this):
        ret = ''
        ret2 = ''
        tmp = this.__new__(this.__class__)
        tmp.__init__(this)
        this = tmp
        if not this.__parentname and not this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not this.__parentname and this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(this.__name)
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= this.__name+'.'+k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s.%s=%s\n'%(this.__name, k, repr(i))
        else :
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s.%s'%(this.__parentname, this.__name)
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= this.__parentname+'.'+this.__name+'.'+k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s.%s.%s=%s\n'%(this.__parentname, this.__name, k, repr(i))
        return ret+ret2

    @staticmethod
    def show(this, name):
        this.__name = name
        print(this)


    @staticmethod
    def update(this, a):
        if type(a) == dict:
            tmp = this.__new__(this.__class__)
            tmp.__fromdict(a)
            a = tmp
        if type(a) == Conf:
            for k,i in a.__dict__.items():
                if type(i) == Conf:
                    if type(this[k]) == Conf:
                        Conf.update(this[k], i)
                this[k] = i
        else:
            print('Conf can only update from Conf/dict')
            errrrrrrrrrrrrrrrrrrrr()

    def __add__(this, a):
        if type(a) != Conf:
            print('Conf can only add Conf')
            errrrrrrrrrrrrrrrrrrrr()
            return
        merge = this.__new__(this.__class__)
        merge.__init__(this)
        for k,i in a.__dict__.items():
            if k not in merge:
                merge[k] = i
            elif type(i) == Conf and type(merge[k]) == Conf:
                merge[k] = merge[k] + i
            else:
                merge[k] = i
        return merge

    def __setitem__(this,i,v):
        super(Conf, this).__setitem__(i,v)
        if i[:7] != '_Conf__':
            if this.__sync:
                this.__sync(this)

    def __setattr__(this,i,v):
        super(Conf, this).__setattr__(i,v)
        if i[:7] != '_Conf__':
            if this.__sync:
                this.__sync(this)

    def __call__(this, a):
        def foo():
            pass
        if type(a) == type(this.__foo):
            this.__sync = a
            a(this)
        elif type(a) == type(foo):
            this.__sync = a
            a(this)
        elif type(a) == this.__class__:
            print 'update'
            Conf.update(this, a)
        elif type(a) == dict:
            print 'update'
            Conf.update(this, a)


    def __foo(this):
        pass

## all method in conf will be sync funtion, so use [function] to set a config to function
#    @staticmethod
#    def sync(this):
#        def foo():
#            pass
#        for k,i in this.__dict__.items():
#            if type(i) == Conf:
#                Conf.sync(i)
#            elif type(i) == type(this.__foo):
#                i()
#            elif type(i) == type(foo):
#                i()
#sync = Conf.sync


class Test(object):
    def d1(this,c):
        print('d1',str(c))


if __name__ == '__main__':
    def test(c):
        print('test')
        print(c)


    t = Test()

    a = Conf()
    a.a.a = 'a'
    a.a.b.c.e = 1
    a.dict = {'dict':'test'}
    a.a.b.c.d = Conf()
    a.a.b.d = Conf()
    a.l = Conf()
    print(a)
    print a.a
    a.a(t.d1)



    exit()
    b = Conf(a)
    c = Conf()
    c.c = 'c'
    b+=c
    a.a.b(t.d1)
    a.a.b.c.e = 2
    Conf.showsync(a)
    print(a)
    exit()
    print(b)

    exit()
