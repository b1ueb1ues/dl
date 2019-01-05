import base_str

conf = {}
conf.update(base_str.conf)

def get(name):
    global conf
    return conf

