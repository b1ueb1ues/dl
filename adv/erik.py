import adv_test
import adv

def module():
    return Erik

class Erik(adv.Adv):
    comment ='do not use weapon skill and fs'
    conf = {
        "mod_a": ('fs', 'passive', 0.30),
        } 


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        """
    adv_test.test(module(), conf, verbose=0)

