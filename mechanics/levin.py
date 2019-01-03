for crit in range(2,100):
    dmg = crit*0.7+100
    if crit > 92:
        crit = 92
    wpdmg = (crit+8)*0.83+100
    print crit, dmg, wpdmg, wpdmg/dmg


print '------------'
for crit in range(2,100):
    dmg = crit*0.9+100
    if crit > 92:
        crit = 92
    wpdmg = (crit+8)*1.03+100
    print crit, dmg, wpdmg, wpdmg/dmg

