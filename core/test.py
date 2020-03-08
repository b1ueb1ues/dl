from timeline import *
#import timeline2
import time

def bench(func):
    print '============='
    a = time.time()
    func()
    b = time.time()
    print '-------------'
    print b-a
    print '-------------'

def t1():
    a = 0
    for i in range(1000000):
        a += 1
    print a

def t2():
    a = [0]
    for i in range(1000000):
        a[0] += 1
    print a[0]

def t3():
    a = {0:0}
    for i in range(1000000):
        a[0] += 1
    print a[0]

_g_test = 0
def t4():
    global _g_test
    for i in range(1000000):
        _g_test += 1
    print _g_test

__g_test = 0
def t5():
    for i in range(1000000):
        globals()['__g_test'] += 1
    print globals()['__g_test']


a = 1
def l():
    global a 
    a += 1

add_event_listener('test',l)
def t6():
    global a
    for i in range(1000000):
        get_event_trigger('test')[0]()
    print a

a = 1
add_event_listener('test',l)
def t7():
    global a
    et = get_event_trigger('test')
    for i in range(1000000):
        et[0]()
    print a


class A():
    def __init__(self):
        return

def a():
    a = 0
    for i in range(1000000):
        a+=1
    print a

def b():
    a = {}
    a['a'] = 0
    for i in range(1000000):
        a['a']+=1
    print a

def c():
    a = A()
    a.a = 0
    for i in range(1000000):
        a.a+=1
    print a.a

def d():
    a = Static()
    a.a = 0
    for i in range(1000000):
        a.a+=1
    print a.a

bench(a)
bench(b)
bench(c)
bench(d)


