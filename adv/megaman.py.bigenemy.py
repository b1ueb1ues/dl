import adv.megaman

def module():
    return Mega_Man

class Mega_Man(adv.megaman.Mega_Man):
    comment = 'rollfs; means bleed; 32 hits leaf shield (Fafnir Roy III sized enemy)'

    def init(self):
        super().init()
        self.conf.s2.x.hit = 32

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)