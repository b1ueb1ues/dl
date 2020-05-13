conf = {
    'xtype': 'ranged',

    'x1.dmg': 0.98,
    'x1.sp': 130,
    'x1.startup': 15/60.0,
    'x1.recovery': 33/60.0,
    'x1.hit': 1,

    'x2.dmg': 0.53*2,
    'x2.sp': 200,
    'x2.startup': 0,
    'x2.recovery': 31/60.0,
    'x2.hit': 2,

    'x3.dmg': 0.36*3,
    'x3.sp': 240,
    'x3.startup': 0,
    'x3.recovery': 53/60.0,
    'x3.hit': 3,

    'x4.dmg': 0.78*2,
    'x4.sp': 430,
    'x4.startup': 0,
    'x4.recovery': 64/60.0,
    'x4.hit': 2,

    'x5.dmg': 0.3605*4+0.618,
    'x5.sp': 600,
    'x5.startup': 0,
    #'x5.recovery': 68/60.0,
    'x5.recovery': 29/60.0,
    'x5.hit': 5,

    'fs._startup': 0,
    'fs._recovery': 29/60.0,

    'fs.dmg': 0.9*2,
    'fs.sp': 400,
    'fs.charge': 28 / 60.0,
    'fs.startup': 43 / 60.0, # 30f for 2nd hit not considered
    'fs.recovery': 46 / 60.0,
    'fs.hit': 2,

    'x1fs.startup': 39 / 60.0, # 11 delay + FS
    'x2fs.startup': 35 / 60.0, # 7 delay + FS

    'fsf.charge': 28 / 60.0,
    'fsf.startup': 1 / 60.0,
    'fsf.recovery': 0 / 60.0,

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,

    'missile_iv': {
        #'fs': 0.7/2,
        #'x1': 0.7,
        #'x2': 0.7,
        #'x3': 0.7,
        #'x4': 0.7,
        #'x5': 0.7,
        'fs': 0,
        'x1': 0,
        'x2': 0,
        'x3': 0,
        'x4': 0,
        'x5': 0,
    }, 
}

lv2 = {
    'x1.dmg': 1.127,
    'x2.dmg': 0.6095*2,
    'x3.dmg': 0.414*3,
    'x4.dmg': 0.897*2,
    'x5.dmg': (0.414575*4)+0.7107,
}

# Wand FS Framedata - MsNyara
# Roll: 36
# FS: 28 (Charge) + 15 (FS1) + 30 (FS2) + 46 (Recovery, from FS1, since it is a projectile)
# FS to FS Recovery (from FS1): 99

# C1FS: 15 (C1) + 11 (FS Delay) + FS
# C2FS: 15 (C1) + 33 (C2) + 7 (FS Delay) + FS

# Note #1: You cannot dodge or skill cancel before FS1 connects. Not perfectly verified, but dodge 1 frame after worked fine (FS2 wasn't lost neither) and with dodge 2 frames before hit the whole FS was lost, so I have little doubts you cannot cancel before FS1 hit. This was tested in MG. Obviously hit timings are going to vary if you are attacking from distance (and size of the objective, for FS2), by which case the projectile (since it is a proper one) is generated at the same timing as FS1 Hit and it is safe to cancel then.