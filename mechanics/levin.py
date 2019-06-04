for crit in range(2,100):
    dmg = crit*0.7+100
    if crit > 92:
        crit = 92
    wpdmg = (crit+7)*0.85+100
    print crit, dmg, wpdmg, wpdmg/dmg


print '------------'
for crit in range(2,100):
    dmg = crit*0.9+100
    if crit > 92:
        crit = 92
    wpdmg = (crit+7)*1.05+100
    print crit, dmg, wpdmg, wpdmg/dmg

