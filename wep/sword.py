conf = {
    'xtype': 'melee',

    'x1.dmg': 75 / 100.0,
    'x1.sp': 150,
    'x1.startup': 10 / 60.0,
    'x1.recovery': 26 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 80 / 100.0,
    'x2.sp': 150,
    'x2.startup': 0,
    'x2.recovery': 22 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 95 / 100.0,
    'x3.sp': 196,
    'x3.startup': 0,
    'x3.recovery': 36 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 100 / 100.0,
    'x4.sp': 265,
    'x4.startup': 0,
    'x4.recovery': 33 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 150 / 100.0,
    'x5.sp': 391,
    'x5.startup': 0,
    'x5.recovery': 35 / 60.0,
    'x5.hit': 1,

    'fs.dmg': 115 / 100.0,
    'fs.sp': 345,
    'fs.charge': 2 / 60.0,
    'fs.startup': 9 / 60.0,
    'fs.recovery': 18 / 60.0,
    'fs.hit': 1,

    'x1fs.charge': 17 / 60.0, # 15 delay + FS
    'x2fs.charge': 3 / 60.0, # 1 delay + FS

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,
}

lv2 = {
    'x1.dmg': 90 / 100.0,
    'x2.dmg': 96 / 100.0,
    'x3.dmg': 114 / 100.0,
    'x4.dmg': 120 / 100.0,
    'x5.dmg': 180 / 100.0,
}

# Sword FS Framedata - MsNyara
# Roll: 36
# FS: 2 (Charge) + 9 (Hit) + 18 (Recovery)

# C1FS: 11 (Hit) + 15 (FS Delay) + FS
# C2FS: 11 (Hit 1) + 26 (Hit 2) + 1 (FS Delay) + FS
# Roll FS: Roll... +... FS, no delays

# Suspected: There is no FS Delay for C3, C4 or C5.
