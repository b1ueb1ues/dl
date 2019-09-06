from ctx import *

c = Condition()

if c('test') :
    print('1')
else:
    print('0')

print(c.conditions)
