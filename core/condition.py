class Condition(dict):
    def __init__(self, cond):
        self.global_cond = True
        if cond is None or isinstance(cond, bool):
            super().__init__({})
            if cond is not None:
                self.global_cond = cond
        elif isinstance(cond, dict):
            super().__init__(cond)
        self.override = False

    def cond_str(self):
        return ' & '.join([k for k, v in self.items() if v])
        
    def cond_set(self, key, cond=True):
        if self.override or key not in self:
            self[key] = cond
        return self[key] and self.global_cond

    def __call__(self, key, cond=True):
        return self.cond_set(key, cond)