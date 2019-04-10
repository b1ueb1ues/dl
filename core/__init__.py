import copy
#from adv import *

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

    def __str__(this):
        ret = ''
        ret2 = ''
        this = copy.deepcopy(this)
        if not this.__parentname and not this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    ret2 += str(i)
                elif k[:7]!='_Conf__' :
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not this.__parentname and this.__name:
            for k,i in this.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(this.__name)
                    ret2 += str(i)
                elif k[:7]!='_Conf__' :
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



    def __setitem__(this,i,v):
        super(Conf, this).__setitem__(i,v)
        if this.__sync:
            this.__sync(this)

    def __setattr__(this,i,v):
        super(Conf, this).__setattr__(i,v)
        if this.__sync:
            this.__sync(this)


    @staticmethod
    def sync(this, s):
        this.__sync = s

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

sync = Conf.sync


class Test(object):
    def d1(this,c):
        print 'd1'


if __name__ == '__main__':
    def test(c):
        print 'test'
        print c



    a = Conf()
    a.a = 3
    sync(a,test)
    exit()
    a.b = 4
    a['a'] = 4
    a['a.b'] = 4
    a['a.b'] = 4
    a['a'] = 4
    print(a)
