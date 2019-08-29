if __package__ is None or __package__ == '':
    import os
    os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.timer import *
from core.event import *
from core.conf import *


class Ctx(object):
    def __init__(this):
        this.el = Event.init()
        this.tl = Timer.init()

    def on(this):
        Event.init(this.el)
        Timer.init(this.tl)

Ctx()
