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

568攻教官 1.03ex 0.97系数
1.2克制特效 1.2破防特效 break是10/6倍

+x add  : 209.7 220.7 231.7 <
+x mult : < 215.6 227.0 238.3

出现了236这样的数字

克制特效 破防特效 乘算


'''

def main():
    dmg = blade*1.03 *568* 10/6
    a = 1.2
    b = 1.2

    addormult("+x",dmg, a, b)



def printboost(name, dmg, boost, p=1):
    dmg = dmg / 6.0
    dmgmin = dmg *0.95
    dmgmax = dmg *1.05
    if p:
        print name, int(dmgmin*boost), int(dmg*boost), int(dmgmax*boost)
    return "%s %.1f %.1f %.1f"%(name, dmgmin*boost, dmg*boost, dmgmax*boost)


def addormult(name, dmg, boost1, boost2):
    a = printboost(name+" add  :", dmg, boost1 + boost2 - 1, 0)
    b = printboost(name+" mult : <", dmg, boost1 * boost2, 0)
    print a,"<"
    print b

if __name__ == "__main__":
    main()
