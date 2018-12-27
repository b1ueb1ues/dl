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
586攻石油
5%狮子*5 4%爆发*5

+x add  : 100.9 106.2 111.5 <
+x mult : < 104.4 109.9 115.4

出现100  
狮子+爆发 加算
'''

def main():
    dmg = sword * 586
    addormult("+x",dmg, 1.25,1.20)



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
