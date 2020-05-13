from core.advbase import *

class Tension:
    MAX_STACK = 5
    def __init__(self, name, mod, event=None):
        # self.adv = adv
        # self.o_dmg_make = adv.dmg_make
        # self.adv.dmg_make = self.dmg_make
        self.name = name
        self.modifier = mod
        self.damage_sources = mod._static.damage_sources # need to account for healing skills bleh
        self.modifier.off()
        self.event = event or Event(name)
        self.scope = {'s1', 's2', 's3', 's'}
        self.current_scope = None
        self.stack = 0
        self.has_stack = Buff('has_'+self.name, 1, -1, self.name, self.name)

    def add(self, n=1, team=False):
        if n < 1:
            return
        if team:
            log(self.name, 'team', n)
        # cannot add if max stacks
        if self.stack == self.MAX_STACK:
            return
        self.stack += n
        self.has_stack.on()
        if self.stack >= self.MAX_STACK:
            self.stack = self.MAX_STACK
        log(self.name, '+{}'.format(n), 'stack <{}>'.format(self.stack))

        self.event.stack = self.stack
        self.event.on()

    def check(self, scope):
        if self.stack >= self.MAX_STACK:
            if self.current_scope is None and scope in self.scope and scope in self.damage_sources:
                # entering a new s1/s2/s3 block
                if scope in self.scope:
                    self.current_scope = scope
                    log(self.name, 'active', 'stack <{}>'.format(self.stack))
                    self.modifier.on()
                    return True
            elif self.current_scope == scope:
                # staying in the same block
                return True
            elif self.current_scope is not None:
                # leaving the block
                self.reset()
        return False

    def reset(self, t=None):
        self.stack = 0
        self.current_scope = None
        self.modifier.off()
        self.has_stack.off()
        log(self.name, 'reset', 'stack <{}>'.format(self.stack))

        self.event.stack = self.stack
        self.event.on()

    def __call__(self):
        return self.stack

class Energy(Tension):
    def __init__(self):
        super().__init__(
            'energy',
            mod=Modifier('mod_energized','s','passive',0.50))

class Inspiration(Tension):
    def __init__(self):
        super().__init__(
            'inspiration',
            mod=Modifier('mod_inspired','crit','chance',1.00))