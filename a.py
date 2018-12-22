
def printboost(name, dmg, boost, p=1):
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


dmg = 2845*1.1*0.97/6

addormult("n",dmg, 1.1,1.7)

dmg = 690*7.43 /6 *1.24

addormult("n",dmg, 1.20,1.25)
