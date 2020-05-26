conf = {
    'xtype': 'melee',

    'x1.dmg': 114 / 100.0,
    'x1.sp': 200,
    'x1.startup': 17 / 60.0,
    'x1.recovery': 46 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 122 / 100.0,
    'x2.sp': 240,
    'x2.startup': 0,
    'x2.recovery': 61 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 204 / 100.0,
    'x3.sp': 360,
    'x3.startup': 0 / 60.0,
    'x3.recovery': 39 / 60.0,
    'x3.hit': 1,

    'x4.dmg': 216 / 100.0,
    'x4.sp': 380,
    'x4.startup': 0,
    'x4.recovery': 78 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 228 / 100.0,
    'x5.sp': 420,
    'x5.startup': 0,
    'x5.recovery': 18 / 60.0,
    'x5.hit': 1,

    'fs.dmg': 192 / 100.0,
    'fs.sp': 300,
    'fs.charge': 26 / 60.0,
    'fs.startup': 28 / 60.0,
    'fs.recovery': 34 / 60.0,
    'fs.hit': 1,

    'x1fs.charge': 33 / 60.0, # 7 delay + fs
    'x2fs.charge': 35 / 60.0, # 10 delay + fs

    'fsf.charge': 26 / 60.0, # https://streamable.com/36bjj
    'fsf.startup': 8 / 60.0,
    'fsf.recovery': 0 / 60.0,

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,
}

lv2 = {
    'x1.dmg': 125.4 / 100.0,
    'x2.dmg': 134.2 / 100.0,
    'x3.dmg': 224.4 / 100.0,
    'x4.dmg': 237.6 / 100.0,
    'x5.dmg': 250.8 / 100.0,
}

# Axe FS Framedata - MsNyara
# Roll: 36
# FS: 26 (Charge) + 28 (Hit) + 34 (Recovery)

# C1FS: 17 (C1) + 7 (FS Delay) + FS
# C2FS: 17 (C1) + 46 (C2) + 10 (FS Delay) + FS
# Roll FS: Roll + FS, for glory.

# Pretty sure C2FS FS Delay would be improved with more attempts but I'm lazy. Unlike the other weapons, I suspect that C3 and C4 might also have some FS Delay shenanigans.