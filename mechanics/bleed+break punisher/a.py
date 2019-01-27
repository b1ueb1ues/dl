# encoding: utf8
sword = 0.75
blade = 0.97
blade2 = 0.97
dagger = 0.75
dagger2 = 0.38
axe = 1.14
lance = 0.84
lance2 = 0.45
bow = 0.29
bow2 = 0.37
wand = 0.98
staff = 0.69


'''

str1393*1.03 addis attact water enemy
1.08 1.20 punisher

===================================
+x add : 705.2 742.3 779.4
+x mult : 714.0 751.5 789.1
-----------------------------------
if dmg < 714.0 : + add +
if dmg > 779.4 : * mul *
-----------------------------------

'''

def main():
    dmg = blade * 1393*1.03 * 1.5 /6*10
    addormult("+x",dmg, 1.2, 1.08)



def printboost(name, dmg, boost, p=1):
    dmg = dmg / 6.0
    dmgmin = dmg *0.95
    dmgmax = dmg *1.05
    if p:
        print name, int(dmgmin*boost), int(dmg*boost), int(dmgmax*boost)
    return name, dmgmin*boost, dmg*boost, dmgmax*boost


def addormult(name, dmg, boost1, boost2):
    a,amin,aave,amax = printboost(name, dmg, boost1 + boost2 - 1, 0)
    m,mmin,mave,mmax = printboost(name, dmg, boost1 * boost2, 0)
    print '==================================='
    print "%s add : %.1f %.1f %.1f"%(a, amin, aave, amax)
    print "%s mult : %.1f %.1f %.1f"%(m, mmin, mave, mmax)
    print '-----------------------------------'
    print "if dmg < %.1f : + add +"%mmin
    print "if dmg > %.1f : * mul *"%amax
    print '-----------------------------------'

if __name__ == "__main__":
    main()
