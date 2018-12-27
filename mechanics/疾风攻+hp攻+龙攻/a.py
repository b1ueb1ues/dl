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

已知龙与hp攻加算
1060攻 水库 无能力基础攻731
70血攻13 疾风攻13 龙攻45


c1
+x add  : 148 156 164 <
+x mult : < 154 163 171

c2
+x add  : 75 79 83 <
+x mult : < 78 82 86

实测c1 149 c2 76
疾风攻+hp攻+龙攻 加算

'''

def main():
    dmg = dagger * 731
    a = 1.58
    b = 1.13

    addormult("+x",dmg, a, b)

    dmg = dagger2 * 731
    a = 1.58
    b = 1.13

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
