# fake class for skill share purposes bolb
class Dummy:
    def __init__(self, is_on=False, is_get=False):
        self.is_on = is_on
        self.is_get = is_get

    def on(self):
        return self.is_on
        
    def get(self):
        return self.is_get