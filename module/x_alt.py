from core.advbase import Fs_group
from core.log import log
from core.config import Conf

class Fs_alt:
    def __init__(self, adv, conf, fs_proc=None):
        self.adv = adv
        self.a_fs_og = adv.a_fs
        self.conf_og = adv.conf
        self.fs_proc_og = adv.fs_proc
        self.conf_alt = adv.conf + Conf(conf)
        self.a_fs_alt = Fs_group('fs_alt', self.conf_alt)
        self.fs_proc_alt = fs_proc
        self.uses = 0

    def fs_proc(self, e):
        if callable(self.fs_proc_alt):
            self.fs_proc_alt(e)
        self.uses -= 1
        if self.uses == 0:
            self.off()

    def on(self, uses = 1):
        log('debug', 'fs_alt on', uses)
        self.uses = uses
        self.adv.a_fs = self.a_fs_alt
        self.adv.conf = self.conf_alt
        self.adv.fs_proc = self.fs_proc

    def off(self):
        log('debug', 'fs_alt off', 0)
        self.uses = 0
        self.adv.a_fs = self.a_fs_og
        self.adv.conf = self.conf_og
        self.adv.fs_proc = self.fs_proc_og

    def get(self):
        return self.uses != 0

class X_alt:
    def __init__(self, adv, conf, disable_fs=False):
        self.xlist_og = []
        for i in range(1, 6):
            self.xlist_og.append(i)