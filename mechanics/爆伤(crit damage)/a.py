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
1890攻击力的家康
带0破雷维昂


===================================
+x add : 609.6 641.7 673.7
+x mult : 673.6 709.0 744.5
-----------------------------------
if dmg < 673.6 : + add +
if dmg > 673.7 : * mul *
-----------------------------------

实测
611 说明1.7与护符与人物被动都是加算

'''

def main():
    dmg = 1.05*1890*blade
    a = 1.7
    b = 1.3

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
