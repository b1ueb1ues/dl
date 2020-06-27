from core.advbase import *
import adv.hunter_sarisse


def module():
    return Hunter_Sarisse

class Hunter_Sarisse(adv.hunter_sarisse.Hunter_Sarisse):
    def init(self):
        super().init()
        for fs in ('fs1', 'fs2', 'fs3', 'fs4'):
            self.conf[f'{fs}.pierce'] = 5

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(Hunter_Sarisse, *sys.argv)