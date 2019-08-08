if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
import vanessa
import slot

def module():
    return Vanessa

class Vanessa(vanessa.Vanessa):
    comment = 'void weapon vs HMS'

    def init(this):
        this.conf['slots.w'] = slot.w.axe.axev5flame()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

