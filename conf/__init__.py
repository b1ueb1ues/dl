import base_str
import skillframe

conf = {}
conf.update(base_str.conf)

def get(name):
    global conf
    for i in skillframe.skills:
        if name == i:
            conf.update({
                "s1_recovery":skillframe.skills[i][0],
                "s2_recovery":skillframe.skills[i][1],
                })
            print conf
            exit()
    return conf
    

