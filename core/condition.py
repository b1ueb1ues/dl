from ctx import Ctx

Ctx.register(globals(),{
    '_if_condition':0,
    '_conditions':{},
    '_switch':-1,
    })

def setcondition(c):
    global _if_condition
    _if_condition = c

def getconditions():
    global _conditions
    ret = []
    for i in _conditions:
        ret.append(i)
    return ret

def on():
    global _if_condition
    _if_condition = 1

def off():
    global _if_condition
    _if_condition = 0

def condition_do(cond):
    global _conditions
    global _if_condition
    global _switch
    _conditions[cond] = 1
    if _switch == -1:
        _switch = _if_condition
    elif _switch != _if_condition:
        print 'condition_do not match same condition' 
        errrrrrrrrrrr()

    return _if_condition
##def condition_do(func):
##    global _if_condition
##    def foo(*args,**kwargs):
##        pass
##    if _if_condition :
##        return func
##    else:
##        return foo
do = condition_do

def __test():
    Ctx().on()
    on()
    if do('test'):
        print '1'
    if do('test2'):
        print '2'
    print getconditions()
    off()

    #Ctx().on()
    #def t1(s='s'):
    #    print 't1', s
    #on()
    #do(t1)('b')

if __name__ == '__main__':
    __test()
