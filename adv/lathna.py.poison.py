import adv_test
import lathna

def module():
    return Lathna

class Lathna(lathna.Lathna):
    comment = ''
    def prerun(this):
        super().prerun()
        if this.condition('always poisoned'):
            this.poisoned=True
        else:
            this.poisoned=False



if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0, mass=0)

