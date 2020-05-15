from typing import Union
class Condition(dict):
    def __init__(self, cond: Union[bool, dict]):
        self.global_cond = True
        self.base_cond = {}
        self.min_hp_cond = (None, 100)
        super().__init__({})
        if isinstance(cond, dict):
            self.base_cond = cond
        elif isinstance(cond, bool):
            self.global_cond = cond

    def cond_str(self):
        return ' & '.join([k for k, v in self.items() if v])
        
    def cond_set(self, key, cond=True):
        if key in self.base_cond:
            self[key] = self.base_cond[key]
        elif key not in self:
            self[key] = cond
        return self[key] and self.global_cond

    def hp_cond_set(self, hp, cond=True):
        key = f'hp={hp}%' if hp > 0 else 'hp=1'
        min_key, min_hp = self.min_hp_cond
        if hp < min_hp:
            if min_key is not None:
                del self[min_key]
            self.min_hp_cond = (key, hp)
            return self.cond_set(key, cond)
        else:
            return self[min_key] and self.global_cond

    def exist(self):
        return any(self.values()) and self.global_cond

    def __call__(self, key, cond=True):
        return self.cond_set(key, cond)