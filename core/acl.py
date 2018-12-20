
def acl_compile(acl):
    aif = []
    acl_list = acl.strip().split('\n')
    for i in acl_list:
        aif.append(i.strip().split(','))


    line = "while 1:\n"
    #line = "def while 1:\n"
    #line_list = []
    for i in aif:
        if len(i) == 1:
            line += "    if %s():\n"%i[0]
            line += "        break\n"
            #line_list.append("%s()\n"%i[0])
        elif len(i) == 2:
            line += "    if %s :\n"%i[1]
            line += "        if %s():\n"%i[0]
            line += "            break\n"
            #line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )
    line += '    break'
    #return line
    return compile(line, "acl", "exec")

"""
# def 
/ cast
/ cast
# def
# def
/ cast
/ cast

"""
g_line = ""

def acl_func(acl):
    global g_line
    aif = []
    prepare_list = []

    acl_list = acl.strip().split('/')
    for i in acl_list:
        i = i.strip()
        loc = i.find('#')
        if loc == 0:
            prepare_list += i.split('#')
        elif loc > 0:
            tmp = i.split('#')
            aif.append(tmp[0].split(','))
            prepare_list += tmp[1:]
        else:
            if i == '':
                continue
            aif.append(i.split(','))

    line = ""

    line += "def foo(this, e):\n"

    for i in prepare_list:
        line += "    %s\n"%(i.strip().replace('\n','\n    '))

    for i in aif:
        if len(i) == 1:
            line += "    if %s():\n"%( i[0].strip() )
            line += "        return '%s'\n"%( i[0].strip() )
            #line_list.append("%s()\n"%i[0])
        elif len(i) == 2:
            condi = i[1].strip().replace("==","=").replace("=","==")
            #condi = i[1].strip()
            line += "    if %s :\n"%( condi )
            line += "        if %s():\n"%( i[0].strip() )
            line += "            return '%s'\n"%( i[0].strip() )
            #line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )
    line += '    return 0'
    g_line = line
    exec(line)
    return foo

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
        /s1,a>b and pin!='sp'
        /s2
        /s3
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
    

