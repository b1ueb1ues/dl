import random
random.seed()


def main():
    g_sum = 0
    pull_sum = 0
    g = Get()
    for i in range(1000000):
        g.bl = 1
        g.r_now = 0.04
        g.get1()
        g.get10()
    print g.g5, g.gall, float(g.g5)/1000000

    g.reset()
    for i in range(1000000):
        g.bl = 1
        g.r_now = 0.04
        g.get10()
        g.get1()
    print g.g5, g.gall, float(g.g5)/1000000

class Get(object):
    def __init__(this):
        this.bl = 10
        this.r_base = 0.02
        this.r_now = 0.02
        this.g5 = 0
        this.gall = 0

    def reset(this):
        this.__init__()

    def get1(this):
        r = random.random()
        this.gall+=1
        if r <= this.r_now:
            this.g5+=1
            this.r_now = this.r_base
        else:
            this.bl -= 1
            if this.bl <= 0:
                this.bl = 10
                this.r_now += 0.005
            
    def get10(this):
        for i in range(10):
            r = random.random()
            this.gall+=1
            tmp = this.g5
            if r <= this.r_now:
                this.g5+=1
            else:
                pass

            if this.g5 != tmp:
                this.bl = 10
                this.r_now = this.r_base
            else:
                this.r_now += 0.005

if __name__ == '__main__':
    main()
