
def printboost(name, dmg, boost, p=1):
    dmg = dmg / 6.0
    dmgmin = dmg *0.95
    dmgmax = dmg *1.05
    if p:
        print name, int(dmgmin*boost), int(dmg*boost), int(dmgmax*boost)
    return "%s %d %d %d"%(name, dmgmin*boost, dmg*boost, dmgmax*boost)


def addormult(name, dmg, boost1, boost2):
    a = printboost(name+" add  :", dmg, boost1 + boost2 - 1, 0)
    b = printboost(name+" mult : <", dmg, boost1 * boost2, 0)
    print a,"<"
    print b


dmg = 1812 *1.08 * 1.61/6

addormult("n",dmg, 1.25,1.4)
