def c(ele,wt):
    r = 0
    if ele == 'flame':
        r += (0.18+0.07+0.04+0.16)
    elif ele == 'water':
        r += (0.18+0.07+0.07+0.04)
    elif ele == 'wind':
        r += (0.18+0.07+0.04)
    elif ele == 'light':
        r += (0.18+0.07+0.07)
    elif ele == 'shadow':
        r += (0.18+0.07+0.04)

    if wt :
        r += 0.30

    if wt == 'dagger' or wt == 'bow':
        r += 0.05

    return 1+r

def d(ele):
    return 1.115

