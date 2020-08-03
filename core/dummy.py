# fake class for skill share purposes bolb
class Dummy:
    def __init__(self, *args, **kargs):
        pass

    def on(self, *args, **kargs):
        return False

    def off(self, *args, **kargs):
        return False

    def get(self, *args, **kargs):
        return False

def dummy_function(*args, **kargs):
    return False