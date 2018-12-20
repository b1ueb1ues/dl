
class Acl(object):
    def compile(this, acl):
        aif = []
        acl_list = acl.strip().split('\n')
        for i in acl_list:
            aif.append(i.strip().split(','))

        line = ""
        line_list = []
        for i in aif:
            if len(i) == 1:
                line += "%s()\n"%i[0]
                line_list.append("%s()\n"%i[0])
            elif len(i) == 2:
                line += "if %s :\n"%i[1]
                line += "    %s()\n"%i[0]
                line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )
        this.aif = aif
        return line_list

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


def create_think(acl, prepare):
    aif = []
    acl_list = acl.strip().split('\n')
    for i in acl_list:
        aif.append(i.strip().split(','))

    prepare_list = []
    prepare_list = prepare.strip().split('\n')

    line = ""

    line += "def foo(this, e):\n"

    for i in prepare_list:
        line += "    %s\n"%(i.strip())

    for i in aif:
        if len(i) == 1:
            line += "    if %s():\n"%i[0]
            line += "        return '%s'\n"%i[0]
            #line_list.append("%s()\n"%i[0])
        elif len(i) == 2:
            line += "    if %s :\n"%i[1]
            line += "        if %s():\n"%i[0]
            line += "            return '%s'\n"%i[0]
            #line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )
    line += '    return 0'
    exec(line)
    return foo

if __name__ == "__main__":
    a = 1
    b = 0

    acl = """
        s1,a>b and pin!='sp'
        s2
        s3

        """
    print compile(acl)

