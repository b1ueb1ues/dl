import adv_test
import ieyasu

def module():
    return Ieyasu

class Ieyasu(ieyasu.Ieyasu):
    comment = ''
    def prerun(this):
        super().prerun()
        if this.condition('always poisoned'):
            this.poisoned=True
        else:
            this.poisoned=False


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)
