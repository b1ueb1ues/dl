import adv_test
import adv

def module():
    return Karina

class Karina(adv.Adv):
    s3 = ('prep','50%')

    def debug(this):
        print this.slots.a
        print this.slots.a.a2
        print this.slots.a.a
        print this.slots.a.a2.a
        #print this.slots.abilities



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2 
        `s3
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

