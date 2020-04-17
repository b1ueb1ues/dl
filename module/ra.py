import slot
from adv import adv_test

t = 0

def test(adv, conf, duration=180):
    print('dps,cname,star,ele,wt,att,wpset,cond,-,amulet1,amulet2,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-')

    ams = []
    amulets_withalias = slot.a.amulets
    for i in amulets_withalias:
        if i not in ams:
            ams.append(i)
    amlen = len(ams)
    for m in range(amlen):
        for n in range(m+1,amlen):
            i = ams[m]
            j = ams[n]
            conf['slots.a'] = i() + j()
            conf['slots.a'] = conf['slots.a']
            def foo(self):
                self.conf['slots.a'] = i()+j()
                self.conf['slots.a'] = self.conf['slots.a']
            adv.slot_backdoor = foo
            adv.comment = '(' + type(i()).__name__ + type(j()).__name__ + ')'
            adv_test.test(adv, conf, verbose=255, mass=0, duration=duration)
