class lobject(object):
    def __init__(self, conf={}):
        for i in conf:
            self[i] = conf[i]

    def __getitem__(self, i):
        l = i.find('.')
        if l >= 1:
            p = i[:l]
            c = i[l+1:]
            return self.__getattribute__(p)[c]
        elif l < 0 and i != '':
            return self.__getattribute__(i)

    def __next__(self):
        return self.__dict__.__next__()

    def __iter__(self):
        return self.__dict__.__iter__()
    

    def __getattr__(self, k):
        if k[:2] != '__':
            i = self.__new__(self.__class__)
            self.__setattr__(k, i)
            return i
        else:
            return object.__getattr__(self,k)

    def __setitem__(self, i, v):
        l = i.find('.')
        if l >= 1:
            p = i[:l]
            c = i[l+1:]

            tmp = self.__new__(self.__class__)
            tmp.__setitem__(c,v)
            if p in self:
                if type(self[p]) == self.__class__:
                    self[p](tmp)
                else:
                    self.__setattr__(p,tmp)
            else:
                self.__setattr__(p,tmp)
            return 
        elif l < 0 and i != '':
            self.__setattr__(i,v)
            return
        raise ValueError('can\' set item')
        return

    def __delitem__(self, i):
        v = self.__getattribute__(i)
        del(v)

   # def __repr__(self):
   #     ret = ''
   #     line = ''
   #     for i in self.__dict__:
   #         line = '%s='%i
   #         line += self.__dict__[i]
   #         line += '\n'
   #         ret += line
   #     return ret

#} //class lobject


class Conf(lobject):
    __parentname = None
    __name = None
    __sync = None

    def __init__(self, template={}):
        if type(template) == dict:
            self.__fromdict(template)
        if type(template) == self.__class__:
            self.__fromdict(template.__todict())


    def __todict(self):
        ret = {}
        for k,v in self.__dict__.items():
            if k[:7] == '_Conf__':
                continue
            if type(v) == self.__class__:
                ret[k] = v.__todict()
            elif type(v) == dict:
                ret[k] = ('__realdict',v)
            elif type(v).__name__ == 'method':
                continue
            elif type(v).__name__ == 'instancemethod':
                continue
            elif type(v).__name__ == 'function':
                continue
            else:
                ret[k] = v
        return ret



    def __todict_withname(self):
        ret = {}
        for k,v in self.__dict__.items():
            if type(v) == self.__class__:
                ret[k] = v.__todict_withname()
            elif type(v) == dict:
                ret[k] = ('__realdict',v)
            elif type(v).__name__ == 'method':
                continue
            elif type(v).__name__ == 'instancemethod':
                continue
            elif type(v).__name__ == 'function':
                continue
            else:
                ret[k] = v
        return ret

    def __todict_all(self):
        ret = {}
        for k,v in self.__dict__.items():
            if type(v) == self.__class__:
                ret[k] = v.__todict_all()
            elif type(v) == dict:
                ret[k] = ('__realdict',v)
            else:
                ret[k] = v
        return ret

    def __fromdict(self,dic):
        if type(dic) != dict:
            raise ValueError('err fromdict')
        for k,v in dic.items():
            if type(v) == tuple and v[0] == '__realdict':
                self[k] = v[1]
            elif type(v) == dict:
                tmp = self.__new__(self.__class__)
                tmp.__fromdict(v)
                self[k] = tmp
            else:
                self[k] = v

    def __str__(self):
        return self.__tostr()

    def __tostr(self):
        ret = ''
        ret2 = ''
        tmp = self.__new__(self.__class__)
        tmp.__init__(self.__todict_withname())
        self = tmp
        if not self.__parentname and not self.__name:
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not self.__parentname and self.__name:
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(self.__name)
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= self.__name+'.'+k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s=%s\n'%(self.__name, k, repr(i))
        else :
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s.%s'%(self.__parentname, self.__name)
                    tmp = i.__tostr()
                    ret2 += tmp
                    if tmp == '':
                        ret2+= self.__parentname+'.'+self.__name+'.'+k+'=Conf()\n'
                elif k[:7]!='_Conf__' :
                #elif k!='_Conf__name' and k!='_Conf__parentname':
                    ret += '%s.%s.%s=%s\n'%(self.__parentname, self.__name, k, repr(i))
        return ret+ret2

    @staticmethod
    def showsync(self):
        ret = ''
        ret2 = ''
        tmp = self.__new__(self.__class__)
        tmp.__init__(self)
        self = tmp
        if not self.__parentname and not self.__name:
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s=%s\n'%(str(k),repr(i))
        elif not self.__parentname and self.__name:
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s'%(self.__name)
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= self.__name+'.'+k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s.%s=%s\n'%(self.__name, k, repr(i))
        else :
            for k,i in self.__dict__.items():
                if type(i) == Conf:
                    i.__name = k
                    i.__parentname = '%s.%s'%(self.__parentname, self.__name)
                    tmp = str(i)
                    ret2 += tmp
                    if tmp == '':
                        ret2+= self.__parentname+'.'+self.__name+'.'+k+'=Conf()\n'
                elif k =='_Conf__sync' :
                    ret += '%s.%s.%s=%s\n'%(self.__parentname, self.__name, k, repr(i))
        return ret+ret2

    @staticmethod
    def show(self, name):
        self.__name = name
        print(self)


    @staticmethod
    def update(self, a):
        if type(a) == dict:
            tmp = self.__new__(self.__class__)
            tmp.__fromdict(a)
            a = tmp
        if type(a) == Conf:
            for k,i in a.__dict__.items():
                if type(i) == Conf:
                    if k in self :
                        if type(self[k]) == Conf:
                            Conf.update(self[k], i)
                            continue
                self[k] = i
        else:
            raise ValueError('Conf can only update from Conf/dict')

    def __add__(self, a):
        if type(a) != Conf:
            raise ValueError('Conf can only add Conf')
            return
        merge = self.__new__(self.__class__)
        merge.__init__(self)
        for k,i in a.__dict__.items():
            if k not in merge:
                merge[k] = i
            elif type(i) == Conf and type(merge[k]) == Conf:
                merge[k] = merge[k] + i
            else:
                merge[k] = i
        return merge

    def __setitem__(self,i,v):
        super(Conf, self).__setitem__(i,v)
        if i[:7] != '_Conf__':
            if self.__sync:
                self.__dosync()
            else:
                if type(v).__name__ == 'instancemethod':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)
                elif type(v).__name__ == 'function':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)
                elif type(v).__name__ == 'method':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)


    def __setattr__(self,i,v):
        super(Conf, self).__setattr__(i,v)
        if i[:7] != '_Conf__':
            if self.__sync:
                self.__dosync()
            else:
                #if i == 'sync_skill':
                #    print(type(v).__name__)
                if type(v).__name__ == 'instancemethod':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)
                elif type(v).__name__ == 'function':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)
                elif type(v).__name__ == 'method':
                    object.__setattr__(self, '_Conf__sync', 1)
                    v(self)

    def __call__(self, a):
        if type(a) == self.__class__:
            Conf.update(self, a)
        elif type(a) == dict:
            Conf.update(self, a)


# all method in conf will be sync funtion, so use [function] to set a config to function
    def __dosync(self):
        func = []
        for k,i in self.__dict__.items():
            if type(i).__name__ == 'instancemethod':
                func.append(i)
            elif type(i).__name__ == 'function':
                func.append(i)
            elif type(i).__name__ == 'method':
                func.append(i)
        for i in func:
            i(self)


class Test(object):
    def d1(self,c):
        print('d1')
        #print(c)


if __name__ == '__main__':
    def test(c):
        print('test')
        print(c)


    t = Test()

    a = Conf()
    b = Conf()


    a.a.a = 'aa'
    a.a.c = 'ac'
    a.a.sync = t.d1

    print(a)
    exit()

    b.a.a = 'ba'
    b.a.b = 'bb'
    a.a.a = 'change'
