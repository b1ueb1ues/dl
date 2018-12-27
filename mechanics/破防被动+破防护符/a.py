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

683攻天才 dagger c1系数0.75 break增伤10/6
自身25%破防特效 护符20%破防特效

c1伤害
===================================
+x add : 196.0 206.3 216.6
+x mult : 202.8 213.4 224.1
-----------------------------------
if dmg < 202.8 : + add +
if dmg > 216.6 : * mul *
-----------------------------------

实测出现199  
破防特效+破防特效 加算

'''

def main():
    dmg = dagger * 683 *10/6
    a = 1.25
    b = 1.20

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
