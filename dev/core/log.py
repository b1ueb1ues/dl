

_g_log = []


class Log(object):
    @classmethod
    def init(cls, l=None):
        global _g_log
        if l:
            _g_log = l
        else:
            return _g_log


def log(t, name, amount=None, misc=""):
    _g_log.append([now(), t, name, amount, misc])
    #e = Event('log_'+name)
    #e.log = [now(), t, name, amount, misc]
    #e.trigger()


def logcat(filter=None, log=None):
    if log == None:
        log = _g_log
        
    if filter == None :
        for i in log:
            if i[3] == None:
                print("%-8.3f: %-8s\t, %-8s\t, \t\t, %s"%(i[0],i[1],i[2],i[4]))
            elif type(i[3]) == float:
                print("%-8.3f: %-8s\t, %-8s\t, %-8.4f\t, %s"%(i[0],i[1],i[2],i[3],i[4]))
            elif type(i[3]) == int:
                print("%-8.3f: %-8s\t, %-8s\t, %-8d\t, %s"%(i[0],i[1],i[2],i[3],i[4]))
            else:
                print("%-8.3f: %-8s\t, %-8s\t, %s\t, %s"%(i[0],i[1],i[2],i[3],i[4]))
    else :
        for i in log:
            for j in filter :
                if i[1] == j:
                    if type(i[3]) == float:
                        print("%-8.3f: %-8s\t, %-16s\t, %-8.4f\t, %s"%(i[0],i[1],i[2],i[3],i[4]))
                    elif type(i[3]) == int:
                        print("%-8.3f: %-8s\t, %-16s\t, %-8d\t, %s"%(i[0],i[1],i[2],i[3],i[4]))
                    else:
                        print("%-8.3f: %-8s\t, %-16s\t, %-8s\t, %s"%(i[0],i[1],i[2],i[3],i[4]))


def logget():
    return _g_log
