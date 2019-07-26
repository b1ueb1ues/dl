#!/usr/bin/env python
# -*- encoding:utf8 -*-
import os
import sys

redirect = 'tee -a'
#redirect = '>>'

ex = [ '_', 'k', 'r', 'd', 'b',
       'kr','kd','kb','rd','rb','db',
       'rdb','kdb','krb','krd',
       'krdb' ]

chart_title = 'dps,name,star,element,weapon,str,amulets,condition,comment,\n' 


opt = []
name = 0


def sh(cmd):
    global opt
    global fsh
    global name
    if '-s' in opt:
        print(cmd)
    else:
        os.system(cmd)



def main(argv):
    global opt
    global name
    while(len(argv)>=2):
        if '-c' in argv:
            opt += ['-c']
            argv.pop(argv.index('-c'))
            continue
        if '-a' in argv:
            opt += ['-a']
            argv.pop(argv.index('-a'))
            continue
        if '-s' in argv:
            opt += ['-s']
            argv.pop(argv.index('-s'))
            continue

        name = argv[1]
        argv.pop(1)
        one_character(name)
        continue


    if '-c' in opt and '-s' in opt:
        print('can not -c -s both')
        errrrrr()

    if '-c' in opt:
        combine()
        return

    if '-s' in opt and name:
        one_character(name)
        return

    if not name : 
        chara_quick()
        sp_quick()
        chara_slow()
        sp_slow()
        if '-s' not in opt:
            combine()



fs = {}
def clean():
    global fs
    dr = 'www/dl-sim/'

    time = '60'
    for i in ex:
        f = open(dr+time+'/data_'+i+'.csv','w')
        f.write(chart_title)
        fs[time+'_'+i] = f

    time = '120'
    for i in ex:
        f = open(dr+time+'/data_'+i+'.csv','w')
        f.write(chart_title)
        fs[time+'_'+i] = f

    time = '180'
    for i in ex:
        f = open(dr+time+'/data_'+i+'.csv','w')
        f.write(chart_title)
        fs[time+'_'+i] = f

    time = 'sp'
    for i in ex:
        f = open(dr+time+'/data_'+i+'.csv','w')
        f.write(chart_title)
        fs[time+'_'+i] = f

def combine():
    global chart_title
    global fs
    clean()
    sp_combine('chara_sp_quick.txt')
    time_combine('chara_quick.txt')

def time_combine(fname):
    global chart_title
    global fs
    fcs = open(fname,'r')
    for c in fcs:
        c = c.strip()
        print c
        fc = open('www/dl-sim/chara/'+c+'.csv')
        for i in fc:
            if i[0] == '-':
                c = i.strip().split(',')
                time = c[1]
                affix = c[2]
                continue
            else:
                fname = time + '_' + affix
                f = fs[fname]
                f.write(i)

def sp_combine(fname):
    global chart_title
    global fs
    fcs = open(fname,'r')
    for c in fcs:
        c = c.strip()
        print c
        fc = open('www/dl-sim/chara/'+c+'.csv','r')
        for i in fc:
            if i[0] == '-':
                c = i.strip().split(',')
                time = c[1]
                affix = c[2]
                continue
            else:
                fname = 'sp_'+affix
                f = fs[fname]
                f.write(i)


def sp_quick():
    f = open('chara_sp_quick.txt')
    for i in f:
        name = i.strip()
        sp_character(name)

def sp_slow():
    f = open('chara_sp_slow.txt')
    for i in f:
        name = i.strip()
        sp_character(name)

def chara_quick():
    f = open('chara_quick.txt')
    for i in f:
        name = i.strip()
        one_character(name)

def chara_slow():
    f = open('chara_slow.txt')
    for i in f:
        name = i.strip()
        one_character(name)


def one_character(name):
    global ex
    sh('echo -n '' > www/dl-sim/chara/%s.csv'%name)
    time = 60
    for i in ex:
        single_sim(name, time, i)
    time = 120
    for i in ex:
        single_sim(name, time, i)
    time = 180
    for i in ex:
        single_sim(name, time, i)


def sp_character(name):
    global ex
    sh('echo -n '' > www/dl-sim/chara/%s.csv'%name)
    for i in ex:
        single_sim(name, 180, i)

def single_sim(name, time, ex):
    cmd = "echo '-,%s,%s' >> www/dl-sim/chara/%s.csv ; "%(time, ex, name)
    cmd += 'python adv/%s -2 %s %s | %s www/dl-sim/chara/%s.csv'%(name, time, ex, redirect, name)
    sh(cmd)




if __name__ == '__main__' :
    main(sys.argv)
