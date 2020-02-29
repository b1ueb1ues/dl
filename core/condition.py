class Condition(dict):
    def __init__(self, cond):
        self.global_cond = True
        self.base_cond = {}
        super().__init__({})
        if cond is None or isinstance(cond, bool):
            if cond is not None:
                self.global_cond = cond
        elif isinstance(cond, dict):
            self.base_cond = cond

    def cond_str(self):
        return ' & '.join([k for k, v in self.items() if v])
        
    def cond_set(self, key, cond=True):
        if key in self.base_cond:
            self[key] = self.base_cond[key]
        elif key not in self:
            self[key] = cond
        return self[key] and self.global_cond

    def exist(self):
        return any(self.values()) and self.global_cond

    def __call__(self, key, cond=True):
        return self.cond_set(key, cond)