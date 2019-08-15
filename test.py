import inspect
import slot.w
def is_adventurer(obj):
    return (inspect.isclass(obj) and issubclass(obj, Adv))
if __name__ == '__main__':
    import adv.addis
    members = inspect.getmembers(adv.addis)
    for m in members:
        print(m)