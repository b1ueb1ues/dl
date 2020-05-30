from typing import Union
from collections import defaultdict

class Condition(dict):
    def __init__(self, cond: Union[bool, dict]):
        self.global_cond = True
        self.base_cond = {}
        self.hp_cond = {'>': {}, '<': {}, '=': {}}
        self.prev_hp_key = None
        self.prev_hp = 100
        super().__init__({})
        if isinstance(cond, dict):
            self.base_cond = cond
        elif isinstance(cond, bool):
            self.global_cond = cond

    def cond_str(self):
        return ' & '.join([k for k, v in self.items() if v])
        
    def cond_set(self, key, cond=True):
        if key.startswith('hp'):
            try:
                if key[2] == '≤':
                    hp = int(key[3:])
                    op = '<'
                else:
                    hp = int(key[2:])
                    op = '>'
                return self.hp_cond_update(key, hp, op) and self.global_cond
            except ValueError:
                pass
        return self.cond_set_value(key, cond)

    def cond_set_value(self, key, cond=True):
        if key in self.base_cond:
            self[key] = self.base_cond[key]
        elif key not in self:
            self[key] = cond
        return self[key] and self.global_cond

    def hp_cond_set(self, hp, cond=True):
        key = f'hp={hp}%' if hp > 0 else 'hp=1'
        return self.hp_cond_update(key, hp, '=') and self.global_cond

    def hp_threshold_cond_set(self, hp, cond=True, op='>'):
        key = f'hp{op}{hp}'
        return self.hp_cond_update(key, hp, op) and self.global_cond

    def hp_cond_update(self, key, hp, op):
        self.hp_cond[op][hp] = key
        try:
            if op == '=':
                target_hp, target_key = hp, key
            elif self.hp_cond['=']:
                target_hp, target_key = min(filter(lambda hpc: self[hpc[1]], self.hp_cond['='].items()), key=lambda hpc: hpc[0])
            elif self.hp_cond['<']:
                target_hp, target_key = min(filter(lambda hpc: self[hpc[1]], self.hp_cond['<'].items()), key=lambda hpc: hpc[0])
            elif self.hp_cond['>']:
                target_hp, target_key = max(filter(lambda hpc: self[hpc[1]], self.hp_cond['>'].items()), key=lambda hpc: hpc[0])
            self.cond_set_value(target_key, True)
            if self.prev_hp_key is not None:
                self[self.prev_hp_key] = False
            self.prev_hp, self.prev_hp_key = target_hp, target_key
            for hpt, hpt_key in self.hp_cond['>'].items():
                self[hpt_key] = target_hp > hpt
            for hpt, hpt_key in self.hp_cond['<'].items():
                self[hpt_key] = target_hp < hpt
            self[target_key] = True
            if op == '<':
                return target_hp <= hp
            elif op == '>':
                return target_hp >= hp
            else:
                return True
        except:
            return self.cond_set_value(key, True)

    def hp_threshold_list(self, threshold=0):
        return sorted(filter(lambda hp: hp > threshold, list(self.hp_cond['='].keys())+list(self.hp_cond['<'].keys())))

    def exist(self):
        return any(self.values()) and self.global_cond

    def __call__(self, key, cond=True):
        return self.cond_set(key, cond)