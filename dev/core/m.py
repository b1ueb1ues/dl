from ctx import *

ctx = Ctx()
print(ctx.el)
print(ctx.tl)
print(ctx.log)
print(now())

c = Conf()
c.a.b = 0
print(c)
