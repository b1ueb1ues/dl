import math

class Afflic(object):
    def __init__(this):
        this.resist = 0
        this.rate = 1
        this.resistup = 0.2
        this.history = 0
        this.maxproc = int((this.rate-this.resist)/this.resistup+0.9999)

    def c(this, total, hit):
        z = 1
        m = 1
        i = hit
        while(i>0):
            z *= (total - i + 1)
            i -= 1
        i = hit
        while(i>0):
            m *= i
            i -= 1
        return z/m

    def proc_m(this):
        chance = 0
        for i in range(1,this.history+1):
            if this.resistup*i + this.resist > 1:
                break
            if this.resistup*i + this.resist > this.rate:
                break
            chance += c(this.history, i)/(2**this.history)


        this.history += 1


    def on(this):
        this.history += 1
        chance = this.rate - this.resist
        count = this.history

a = Afflic()
print a.c(5, 3)
