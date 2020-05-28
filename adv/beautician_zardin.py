from core.advbase import *

def module():
    return Beautician_Zardin

class Beautician_Zardin(Adv):
    comment = 'no s2'

    a3 = ('s',0.35,'hp70')

    conf = {}
    conf['acl'] = """
        `dragon
        `s1
        `s3
        """
    coab = ['Halloween_Elisanne','Dagger','Peony']

    def s1_proc(self, e):
        self.energy.add(1)

    def s2_proc(self, e):
        self.energy.add(2)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)