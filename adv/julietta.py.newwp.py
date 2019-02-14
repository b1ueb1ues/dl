import adv_test
import julietta

def module():
    return Julietta_newWP

class Julietta_newWP(julietta.Julietta):
    adv_name = 'Julietta'
    conf = {
        'mod_wp': [
            ('s','passive',0.15),
            ('crit','rate',0.12),
        ],
    }

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        """
    adv_test.test(module(), conf, verbose=0)

