
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

def compile(acl):
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
    return line


def create_think(acl, prepare):
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
    return line

if __name__ == "__main__":
    a = 1
    b = 0

    acl = """
        s1,a>b and pin!='sp'
        s2
        s3

        """
    print compile(acl)

