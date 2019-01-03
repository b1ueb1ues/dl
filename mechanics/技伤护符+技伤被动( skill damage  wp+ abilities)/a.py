# encoding: utf8
sword  = 0.75
blade  = 0.97 ; blade2  = 0.97
dagger = 0.75 ; dagger2 = 0.38
axe    = 1.14
lance  = 0.84 ; lance2  = 0.45
bow    = 0.29 ; bow2    = 0.37
wand   = 0.98
staff  = 0.69


'''
1650攻击力的光枪

3级1技能系数1.15 30%技伤被动 带25%技伤护符
===================================
+x add : 465.7 490.2 514.7
+x mult : 488.2 513.9 539.6
-----------------------------------
if dmg < 488.2 : + add +
if dmg > 514.7 : * mul *
-----------------------------------

实测471 468 478

技伤被动+技伤护符 加算

'''

def main():
    dmg = 1.15 * 1650
    a = 1.25
    b = 1.30

    addormult("+x",dmg, a, b)



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
