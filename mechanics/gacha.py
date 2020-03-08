import random
random.seed()


rate = 0.06
last = 5

def main():
    test()

def test():
    g_sum = 0
    pull_sum = 0
    g = Get()
    for i in range(1000000):
        g.bl = last
        g.r_now = rate
        for i in range(last):
            g.get1()
        g.get10()
    print g.g5, g.gall, float(g.g5)/g.gall, float(g.g5)/1000000

    g.reset()
    for i in range(1000000):
        g.bl = last
        g.r_now = rate
        g.get10()
        for i in range(last):
            g.get1()
    print g.g5, g.gall, float(g.g5)/g.gall,  float(g.g5)/1000000

class Get(object):
    def __init__(self):
        self.bl = 10
        self.r_base = 0.04
        self.r_now = 0.04
        self.g5 = 0
        self.gall = 0

    def reset(self):
        self.__init__()

    def get1(self):
        r = random.random()
        self.gall+=1
        if r <= self.r_now:
            self.g5+=1
            self.r_now = self.r_base
        else:
            self.bl -= 1
            if self.bl <= 0:
                self.bl = 10
                self.r_now += 0.005
            
    def get10(self):
        for i in range(10):
            r = random.random()
            self.gall+=1
            tmp = self.g5
            if r <= self.r_now:
                self.g5+=1
            else:
                pass
        if self.g5 != tmp:
            self.bl = 10
            self.r_now = self.r_base
        else:
            self.r_now += 0.005

if __name__ == '__main__':
    main()
