conf = {
    'xtype': 'ranged',

    'x1.dmg': 0.29*3,
    'x1.sp': 184,
    'x1.startup': 23 / 60.0,
    'x1.recovery': 35 / 60.0,
    'x1.hit': 3,

    'x2.dmg': 0.37*2,
    'x2.sp': 92,
    'x2.startup': 0,
    'x2.recovery': 33 / 60.0,
    'x2.hit': 2,

    'x3.dmg': 0.42*3,
    'x3.sp': 276,
    'x3.startup': 0,
    'x3.recovery': 51 / 60.0,
    'x3.hit': 3,

    'x4.dmg': 0.63*2,
    'x4.sp': 414,
    'x4.startup': 0,
    'x4.recovery': 66 / 60.0,
    'x4.hit': 2,

    'x5.dmg': 0.35*5,
    'x5.sp': 529,
    'x5.startup': 0,
    'x5.recovery': 24 / 60.0,
    'x5.hit': 5,

    'fs.dmg': 0.31*8,
    'fs.sp': 460,
    'fs.charge': 20 / 60.0,
    'fs.startup': 45 / 60.0, 
    'fs.recovery': 43 / 60.0, 
    'fs.hit': 8,

    'x1fs.charge': 22 / 60.0, # 2 delay + fs
    'x2fs.charge': 27 / 60.0, # 7 delay + fs

    'fsf.charge': 20 / 60.0,
    'fsf.startup': 12 / 60.0,
    'fsf.recovery': 0 / 60.0,

    # 'dfs.startup': (86-36) / 60.0, # ???
    # 'dfs.recovery': 37 / 60.0,
    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,

    'missile_iv': {
        'fs': 0.0,
        'x1': 0.0,
        'x2': 0.0,
        'x3': 0.0,
        'x4': 0.0,
        'x5': 0.0,
    },
}

lv2 = {
    'x1.dmg': 0.3625*3,
    'x2.dmg': 0.4625*2,
    'x3.dmg': 0.525*3,
    'x4.dmg': 0.7875*2,
    'x5.dmg': 0.4375*5,
}

# Bow FS Framedata - MsNyara
# Roll: 36
# FS: 20 (Charge) + 45 (Projectile Creation) + 43 (Recovery, from Projectile Creation)
# FS Hits (from Projectile Creation): 42 + 7 + 9 + 7 + 9 + 7 + 9 + 8
# FS to FS Recovery (from Projectile Creation): ?

# C1FS: 22 (C1) + 2 (FS Delay) + FS
# C2FS: 22 (C1) + 20 (C2A) + 13 (C2B) + FS

# I suspect there is no FS Delay for following combos. All C1 hits lands at the same frame, too. If you cancel before projectile creation you lost it altogether.