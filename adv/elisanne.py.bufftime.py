import adv_test
from adv import *
import elisanne

def module():
    return Elisanne

class Elisanne(elisanne.Elisanne):
    comment = 'do not use fs & 15bufftime WP'
    conf = {}
    conf['mod_wp'] = []
    conf['str_wp'] = 25
    def init(this):
        this.conf['s1_buff'][1] *= 1.4


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)


