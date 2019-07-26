import os

redirect = 'tee -a'

ex = [ '_', 'k', 'r', 'd', 'b',
       'kr','kd','kb','rd','rb','db',
       'rdb','kdb','krb','krd',
       'krdb' ]

chart_title = 'dps,name,star,element,weapon,str,amulets,condition,comment,' 


def main():
    #sp_quick()
    chara_quick()
    combine()
    #sp_quick()
    #one_character('mikoto.py')

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
    sp_combine('chara_quick.txt')

def time_combine():
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
        fc = open('www/dl-sim/chara/'+c+'.csv')
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
    os.system('echo -n '' > www/dl-sim/chara/%s.csv'%name)
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
    os.system('echo -n '' > www/dl-sim/chara/%s.csv'%name)
    for i in ex:
        single_sim(name, 180, i)

def single_sim(name, time, ex):
    cmd = "echo '-,%s,%s' >> www/dl-sim/chara/%s.csv ; "%(time, ex, name)
    cmd += 'python adv/%s -2 %s %s | %s www/dl-sim/chara/%s.csv'%(name, time, ex, redirect, name)
    os.system(cmd)




if __name__ == '__main__' :
    main()
