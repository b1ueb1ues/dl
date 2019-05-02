import slot
from adv import adv_test

t = 0

def test(adv, conf, duration=180):
    print('dps,cname,star,ele,wt,att,cond,-,amulet1,amulet2,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-')

    global t
    if t == 0:
        t = 1
    else:
        errrrrrrrrrr()

    ams = slot.a.amulets
    amlen = len(ams)
    for m in range(amlen):
        for n in range(m+1,amlen):
            i = ams[m]
            j = ams[n]
            conf['slots.a'] = i() + j()
            adv.comment = '(',type(i()).__name__, type(j()).__name__,')'
            adv_test.test(adv, conf, verbose=255, mass=0, duration=duration)
