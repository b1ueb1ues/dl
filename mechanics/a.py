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


def main():
    dmg = dagger * 1060/1.45
    addormult("+x",dmg, 1.13,1.58)

    dmg = dagger2 * 1060/1.45
    addormult("+x",dmg, 1.13,1.58)


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

if __name__ == "__main__":
    main()
