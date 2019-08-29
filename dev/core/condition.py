
class Condition(object):

    @classmethod
    def init(cls):
        cls.if_condition = 0
        cls.conditions = {}
        cls.switch = -1

    def __init__(this):
        this.if_condition = 0
        this.conditions = {}
        this.switch = -1

    def __str__():
        a = get()
        ret = ''
        for i in a:
            if ret != '':
                ret += ' & '
            ret += i
        return ret

    def condition_do(this):
        this.conditions[cond] = 1
        if this.switch == -1:
            this.switch = this.if_condition
        elif this.switch != this.if_condition:
            print('condition_do not match same condition' )
            errrrrrrrrrrr()

        return this.if_condition



Ctx.register(globals(),{
    '_if_condition':0,
    '_conditions':{},
    '_switch':-1,
    })

def set(c=1):
    global _if_condition
    _if_condition = c

def unset():
    global _if_condition
    _if_condition = 0

def get():
    global _conditions
    ret = []
    for i in _conditions:
        ret.append(i)
    return ret

def clean():
    global _if_condition
    global _conditions
    global _switch
    _if_condition = 0
    _conditions = {}
    _switch = -1

def p():
    a = get()
    ret = ''
    for i in a:
        if ret != '':
            ret += ' & '
        ret += i
    return ret


def condition_do(cond):
    global _conditions
    global _if_condition
    global _switch
    _conditions[cond] = 1
    if _switch == -1:
        _switch = _if_condition
    elif _switch != _if_condition:
        print('condition_do not match same condition' )
        errrrrrrrrrrr()

    return _if_condition


do = condition_do
on = condition_do

def __test():
    Ctx().on()
    set(1)
    if do('test'):
        print('1')
    if do('test2'):
        print('2')
    print(get())
    print(p())
    set(0)

    #Ctx().on()
    #def t1(s='s'):
    #    print('t1', s)
    #on()
    #do(t1)('b')

if __name__ == '__main__':
    __test()
