from ctx import *

def foo(e):
    pass

ctx = Ctx()
log('test','test')
Event('test')(foo)
print(ctx.el)
print(ctx.tl)
print(ctx.log)
print(now())

c = Conf()
c.a.b = 0
print(c)

ctx_o = ctx
ctx = Ctx()
log('test2','test2')
print(ctx.el)
print(ctx.tl)
print(ctx.log)
print(now())

ctx = ctx_o
ctx()
print(ctx.el)
print(ctx.tl)
print(ctx.log)
print(now())
