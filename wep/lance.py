
conf = {
    'xtype': 'melee',

    'x1.dmg': 84 / 100.0,
    'x1.sp': 120,
    'x1.startup': 9 / 60.0,
    'x1.recovery': 41 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 45*2 / 100.0,
    'x2.sp': 240,
    'x2.startup': 0,
    'x2.recovery': 34 / 60.0,
    'x2.hit': 2,

    'x3.dmg': 108 / 100.0,
    'x3.sp': 120,
    'x3.startup': 0, 
    'x3.recovery': 37 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 150 / 100.0,
    'x4.sp': 480,
    'x4.startup': 0,
    'x4.recovery': 40 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 112 / 100.0,
    'x5.sp': 600,
    'x5.startup': 0,
    'x5.recovery': 35 / 60.0,
    # 'x5.recovery': 67 / 60.0,
    'x5.hit': 1,

    'fs._startup': 0,
    'fs._recovery': 35 / 60.0,

    'fs.dmg': 30*5 / 100.0,
    'fs.sp': 400,
    'fs.startup': 35 / 60.0,
    'fs.recovery': 36 / 60.0,
    'fs.hit': 5,

    'x1fs.startup': 51 / 60.0, # 16 delay + fs

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,
}

lv2 = {
    'x1.dmg': 92.4 / 100.0,
    'x2.dmg': 49.5*2 / 100.0,
    'x3.dmg': 118.8 / 100.0,
    'x4.dmg': 165 / 100.0,
    'x5.dmg': 123.2 / 100.0,
}

# Lance FS Framedata
# Roll: 36
# FS: 8 (Charge) + 7 (FS1) + 4 (FS2) + 7 (FS3) + 4 (FS4) + 5 (FS5) + 36 (Recovery)

# C1FS: 9 (C1) + 16 (FS Delay) + FS
# C2FS: 9 (C1) + 31 (C2A) + 10 (C2B)  + FS

# Roll FS: Fish Roll + Rice FS (no interactions)

# Pretty confident there is no FS Delay for further combo, too.