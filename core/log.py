from core.timeline import *
import core.timeline
import sys

loglevel = 0

#g_log = []
g_log_active = []
#g_logs = {"default":g_log_active}


def loginit(log=None):
    global g_log_active
    if log == None :
        g_log_active = []
        return g_log_active
    else:
        g_log_active = log
        return 1

def log(t, name, amount=None, misc=""):
    g_log_active.append([core.timeline.now(), t, name, amount, misc])
    #e = Event('log_'+name)
    #e.log = [now(), t, name, amount, misc]
    #e.trigger()

def logcat(filter=None, log=None):
    if log == None:
        log = g_log_active
        
    if filter == None :
        for i in log:
            if i[3] == None:
                print("%-8.3f: %-16s, %-16s, \t\t, %s"%(i[0],i[1],i[2],i[4]))
            elif type(i[3]) == float:
                print("%-8.3f: %-16s, %-16s, %-16.4f, %s"%(i[0],i[1],i[2],i[3],i[4]))
            elif type(i[3]) == int:
                print("%-8.3f: %-16s, %-16s, %-16d, %s"%(i[0],i[1],i[2],i[3],i[4]))
            else:
                print("%-8.3f: %-16s, %-16s, %-16s, %s"%(i[0],i[1],i[2],i[3],i[4]))
    else :
        for i in log:
            for j in filter :
                if i[1] == j:
                    if type(i[3]) == float:
                        print("%-8.3f: %-16s, %-24s, %-16.4f, %s"%(i[0],i[1],i[2],i[3],i[4]))
                    elif type(i[3]) == int:
                        print("%-8.3f: %-16s, %-24s, %-16d, %s"%(i[0],i[1],i[2],i[3],i[4]))
                    else:
                        print("%-8.3f: %-16s, %-24s, %-16s, %s"%(i[0],i[1],i[2],i[3],i[4]))



def logget():
    return g_log_active

def logreset():
    global g_log_active
    g_log_active = []

