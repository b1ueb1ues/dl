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
2661攻 10%ex 无技能伤害 打风龙
s1 don't buff s1 : 2707.1 2849.5 2992.0
s1 buff s1       : 2830.1 2979.1 3128.0
实测2788 2823 2958

1级武器技能3.19
带0破教官护符2623攻
无背水  打风龙
s1 don't buff s3 : 2513.9 2646.2 2778.5
s1 buff s3       : 2765.3 2910.8 3056.3
1接3
2973 2910 2792
1技能确定提高武器技能伤害

触发背水
===================================
s3with2attbuff add : 3519.4 3704.7 3889.9
s3with2attbuff mult : 3594.8 3784.0 3973.2
-----------------------------------
if dmg < 3594.8 : + add +
if dmg > 3889.9 : * mul *
-----------------------------------
实测1接3
3797 3707 3537
1技能buff与其他攻击buff加算

'''

def main():
    p = 3.54
    pw = 3.19
    dmg = p * 2661 * 1.1 * 1.5
    printboost('s1', dmg, 1.1, p=1)
    printboost('s1', dmg, 1.15, p=1)

    dmg = pw * 2623 * 1.1 * 1.5 *1.15
    printboost('s3', dmg, 1.0, p=1)
    printboost('s3', dmg, 1.1, p=1)

    addormult('s3with2attbuff', dmg, 1.1, 1.3)


def printboost(name, dmg, boost, p=1):
    dmg = dmg / 6.0
    dmgmin = dmg *0.95
    dmgmax = dmg *1.05
    if p:
        print name, "%.1f"%(dmgmin*boost), "%.1f"%(dmg*boost), "%.1f"%(dmgmax*boost)
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
