from core.log import *
import sys

g_line = ""

def acl_func_str(acl):
    s = acl_str(acl)
    exec(s)
    return foo, s

def acl_func(acl):
    s = acl_str(acl)
    exec(s)
    return foo

def acl_str(acl):
    global g_line
    aif = []
    aif_list = []
    prepare_list = []


    aifline = -1
    prepareline = -1
    curr = 'none'
    for i in acl:
        if i == "`":
            aifline += 1
            aif.append("")
            curr = 'aif'
        elif i == "#":
            prepareline += 1
            prepare_list.append("")
            curr = 'prepare'
        else:
            if curr == 'aif':
                aif[aifline] += i
            elif curr == 'prepare':
                prepare_list[prepareline] += i

    for i in aif:
        aif_list.append( i.split(',', 1) )


    #acl_list = acl.strip().split('`')
    #for i in acl_list:
    #    i = i.strip()
    #    loc = i.find('#')
    #    if loc == 0:
    #        prepare_list += i.split('#')
    #    elif loc > 0:
    #        tmp = i.split('#')
    #        aif_list.append(tmp[0].split(','))
    #        prepare_list += tmp[1:]
    #    else:
    #        if i == '':
    #            continue
    #        aif_list.append(i.split(','))

    line = ""

    line += "def foo(this, e):\n"

    for i in prepare_list:
        line += "    %s\n"%(i.strip().replace('\n','\n    '))

    for i in aif_list:
        if len(i) == 1:
            line += "    if %s():\n"%( i[0].strip() )
            line += "        return '%s'\n"%( i[0].strip() )
            #line_list.append("%s()\n"%i[0])
        elif len(i) == 2:
            condi = i[1].strip().replace("=","==")
            condi = condi.replace("====","==")
            condi = condi.replace("!==","!=")
            condi = condi.replace(">==",">=")
            condi = condi.replace("<==","<=")
            #condi = i[1].strip()
            line += "    if %s :\n"%( condi )
            line += "        if %s():\n"%( i[0].strip() )
            line += "            return '%s'\n"%( i[0].strip() )
            #line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )

    line += '    return 0'
    g_line = line
   # if len(sys.argv) >= 2:
   #     if sys.argv[1] != 0:
   #         if int(sys.argv[1]) >= 2:
   #             print line
    return line


if __name__ == "__main__":
    a = 1
    b = 0
    this = 0
    e = 0
    epin = 'a'
    def foo():
        print 'foo'


    acl = """
        #if a>b :\n    b=3\n
        `s1,a>b and pin!='sp'
        `s2
        `s3
        #s1 = foo
        #s2 = foo
        #s3 = foo
        #pin = epin
        """
    try:
        acl_func(acl)(this, e)
    except Exception, e:
        pass
    print g_line
    

