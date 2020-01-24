from slot.a import *


class Plunder_Pals(Amulet): #Plunder Pals or Hitting the Books
    att = 54
    a = [('s',0.30)]
PP = Plunder_Pals


class Resounding_Rendition(Amulet):
    att = 64
    a = [('s',0.30),
         ('cc',0.08,'hp70')]
RR = Resounding_Rendition


class Crystalian_Envoy(Amulet):
    att = 57
    a = [('a',0.13,'hp70')]
CE = Crystalian_Envoy


class Bonds_Between_Worlds(Amulet):
    att = 54
    a = [('a',0.13,'hp70'),
         ('prep',25)]
Bonds = Bonds_Between_Worlds
BBW = Bonds_Between_Worlds


class Levins_Champion(Amulet):
    att = 64
    a = [('cd',0.15),
         ('cc',0.10,'hp70')]
LC = Levins_Champion


class Valiant_Crown(Amulet):
    att = 65
    a = [('s',0.30),
         ('bc',0.10)]
VC = Valiant_Crown


class Tough_Love(Amulet):
    att = 65
    a = [('s',0.25),
         ('lo',0.50)]
TL = Tough_Love


class Flash_of_Genius(Amulet): # Flash of Genius
    att = 57
    a = [('a',0.20,'hit15')]
FG = Flash_of_Genius
FoG = Flash_of_Genius


class Fresh_Perspective(Amulet):
    att = 52
    a = [('fs',0.40),
         ('s',0.20)]
FP = Fresh_Perspective


class Bellathorna(Amulet):
    att = 25
    a = [('bt',0.20)]
BT = Bellathorna


#class Together_We_Stand(Amulet):
#    att = 52
#    a = [('sts',0.05),
#         ('s',0.20)]


class First_Rate_Hospitality(Amulet):
    att = 55
    a = [('a',0.08,'hp70'),
         ('bc',0.10)]
FRH = First_Rate_Hospitality


class The_Bustling_Hut(Amulet):
    att = 50
    a = [('bc',0.08)]
    def on(this, c):
        if c.ele == 'light':
            a = [('bc',0.08),
                 ('sp',0.07)]


class Jewels_of_the_Sun(Amulet):
    att = 64
    a = [('sp',0.08),
         ('a',0.10,'hp70')]
JotS = Jewels_of_the_Sun


class United_by_One_Vision(Amulet):
    att = 54
    a = [('sp',0.08),
         ('a',0.13,'hp70')]


class Heralds_of_Hinomoto(Amulet):
    att = 64
    a = [('s',0.30),
         ('sp',0.06)]
HoH = Heralds_of_Hinomoto
HH = Heralds_of_Hinomoto


class One_with_the_Shadows(Amulet):
    att = 51
    a = [('cc',0.06),
         ('bk',0.20)]


class Flower_in_the_Fray(Amulet):
    att = 52
    a = [('cd',0.15),
         ('s',0.20)]
FitF = Flower_in_the_Fray


class The_Prince_of_Dragonyule(Amulet):
    att = 63
    a = [('cd',0.20)]
    def on(this, c):
        if c.ele == 'water':
            this.a = [('cd',0.20)]
            this.a += [('cc',0.12,'hit15')]


class Evening_of_Luxury(Amulet):
    att = 65
    a = [('a',0.15,'hp100'),
         ('cd',0.15)]
EoL = Evening_of_Luxury


class Seaside_Princess(Amulet):
    att = 65
    a = [('a',0.15,'hp100'),
         ('cd',0.22,'hp100')]
SSP = Seaside_Princess


class The_Chocolatiers(Amulet):
    att = 62
    a = [('prep',100)]
Choco = The_Chocolatiers


class Worthy_Rivals(Amulet):
    att = 64
    a = [('bk',0.30),
         ('prep',25)]


class Lord_of_the_Skies(Amulet):
    att = 46
    a = [('od',0.10)]


class Witchs_Kitchen(Amulet):
    att = 57
    a = [('s',0.40,'hp100'),
         ('resist',50,'blind')]


class Silke_Lends_a_Hand(Amulet):
    att = 42
    a = [('s',0.20),
         ('resist',50,'blind')]


class Saintly_Delivery(Amulet):
    att = 42
    a = [('s',0.20),
         ('resist',50,'stun')]


class Luck_of_the_Draw(Amulet):
    att = 33
    a = [('resist',25,'paralysis')]
    def on(this, c):
        if c.ele == 'shadow':
            this.a = [('resist',25,'paralysis')]
            this.a += [('bt',0.25)]


class Lunar_Festivities(Amulet):
    att = 51
    a = [('fs',0.40),
         ('sp',0.10,'fs')]


class The_Warrioresses(Amulet):
    att = 52
    a = [('fs',0.40),
         ('cd',0.13)]


class Stellar_Show(Amulet):
    att = 65
    a = [('fs',0.50),
         ('cd',0.15)]
SS = Stellar_Show


class Kung_Fu_Masters(Amulet):
    att = 64
    a = [('s',0.20)]
    def on(this, c):
        if c.wt == 'axe':
            this.a = [('s',0.20)]
            this.a += [('cc',0.14)]
KFM = Kung_Fu_Masters


class Forest_Bonds(Amulet):
    att = 64
    a = [('sp',0.12,'fs')]
    def on(this, c):
        if c.wt == 'bow':
            this.a = [('sp',0.12,'fs')]
            this.a += [('s',0.40)]
FB = Forest_Bonds


class Dragon_and_Tamer(Amulet):
    att = 57
    def on(this, c):
        if c.wt == 'lance':
            this.a = [('s',0.40)]
DnT = Dragon_and_Tamer


class Twinfold_Bonds(Amulet):
    att = 65
    a = [('a',0.15,'hit15')]
    def on(this, c):
        if c.wt == 'dagger':
            this.a = [('s',0.40)]
            this.a += [('a',0.15,'hit15')]
TB = Twinfold_Bonds


class Summer_Paladyns(Amulet):
    att = 64
    def on(this, c):
        if c.wt == 'axe':
            this.a = [('s',0.40)]

    def dc_energy(this, e):
        e = this.adv.Event('add_energy')
        e.name = 'self'
        e()

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        from module import energy
        energy.Energy(adv, {}, {})
        adv.Listener('defchain',this.dc_energy)


class The_Shining_Overlord(Amulet):
    att = 65
    a = [('dc', 0.06)]
    def on(this, c):
        if c.wt == 'sword':
            this.a = [('dc', 0.06)]
            this.a += [('s',0.40)]
TSO = The_Shining_Overlord

class The_Shining_Overlord_Max_Stacks(Amulet):
    att = 65
    a = [('dc_max', (0.06, 0.09, 0.15))]
    def on(this, c):
        if c.wt == 'sword':
            this.a = [('dc_max', (0.06, 0.09, 0.15)), ('s',0.40)]

class Halidom_Grooms(Amulet):
    att = 50
    a = [('bt',0.2)]

    def dc_energy(this, e):
        e = this.adv.Event('add_energy')
        e.name = 'self'
        e()

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        from module import energy
        energy.Energy(adv, {}, {})
        adv.Listener('defchain',this.dc_energy)
HG = Halidom_Grooms


class Beach_Battle(Amulet):
    att = 50
    a = [('bt',0.2)]
    def on(this, c):
        if c.ele == 'water':
            this.a = [('bt',0.2), ('sp',0.07)]
BB = Beach_Battle


class The_Petal_Queen(Amulet):
    att = 53

    def startup(this, t):
        e = this.adv.Event('add_energy')
        e.name = 'self'
        e()
        e()
        e()
        e()
        e()

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        adv.Timer(this.startup).on()


class Hanetsuki_Rally(Amulet):
    att = 51
    a = [('cc',0.05),('lo',0.4)]
HR = Hanetsuki_Rally


class Indelible_Summer(Amulet):
    att = 52
    def on(this, c):
        if c.ele == 'water':
            this.a = [('sp',0.09)]
IS = Indelible_Summer


class Sisters_Day_Out(Amulet):
    att = 64
    a = [('fs',0.40)]
    def fs_proc(this, e):
        fs_hits = {'sword': 1, 'blade': 1, 'dagger': 3, 'axe': 1, 'lance': 5, 'wand': 2, 'bow': 8, 'staff': 4}
        this.o_fs_proc(e)
        if this.adv.fs_prep_c > 0:
            diff = this.adv.fs_prep_c - max(this.adv.fs_prep_c-fs_hits[this.adv.slots.c.wt], 0)
            for _ in range(diff):
                this.adv.charge_p('fs_charge','25%')
            this.adv.fs_prep_c = this.adv.fs_prep_c - diff

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        this.adv.fs_prep_c = 3
        this.o_fs_proc = adv.fs_proc
        adv.fs_proc = this.fs_proc
SDO = Sisters_Day_Out


class Elegant_Escort(Amulet):
    att = 54
    a = [('k_burn',0.3)]
EE = Elegant_Escort

class Beautiful_Nothingness(Amulet):
    att = 52
    a = [('a',0.10,'hp70'),('cc',0.05)]
BN = Beautiful_Nothingness

class Castle_Cheer_Corps(Amulet):
    att = 64
    a = [('sp',0.06)]
    def fs_proc(this, e):
        fs_hits = {'sword': 1, 'blade': 1, 'dagger': 3, 'axe': 1, 'lance': 5, 'wand': 2, 'bow': 8, 'staff': 4}
        this.o_fs_proc(e)
        if this.adv.fs_prep_c > 0:
            diff = this.adv.fs_prep_c - max(this.adv.fs_prep_c-fs_hits[this.adv.slots.c.wt], 0)
            for _ in range(diff):
                this.adv.charge_p('fs_charge','25%')
            this.adv.fs_prep_c = this.adv.fs_prep_c - diff

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        this.adv.fs_prep_c = 3
        this.o_fs_proc = adv.fs_proc
        adv.fs_proc = this.fs_proc
CCC = Castle_Cheer_Corps

class Honest_Repose(Amulet):
    att = 53
    def on(this, c):
        if c.ele == 'flame':
            this.a = [('sp', 10)]

class High_Dragon_WP(Amulet):
    att = 39

class Candy_Couriers(Amulet):
    att = 65
    a = [('bk',0.25)]
    def on(this, c):
        if c.wt == 'wand':
            this.a = [('bk',0.25), ('s',0.40)]


class Candy_Couriers(Amulet):
    att = 65
    a = [('bk',0.25)]
    def on(this, c):
        if c.wt == 'wand':
            this.a = [('bk',0.25)]
            this.a += [('s',0.40)]
CC = Candy_Couriers

class From_Whence_He_Came(Amulet):
    att = 50
    a = [('bt',0.2),
         ('prep',0.25)]
FWHC = From_Whence_He_Came

class Dear_Diary(Amulet):
    att = 65
    a = [('ro', (0.1, 60))]
    def on(this, c):
        if c.wt == 'bow':
            this.a = [('ro', (0.1, 60)), ('cc',0.14)]
DD = Dear_Diary

class Dear_Diary_Fast_RO(Amulet):
    att = 65
    a = [('ro', (0.1, 30))]
    def on(this, c):
        if c.wt == 'bow':
            this.a = [('ro', (0.1, 30)), ('cc',0.14)]

class Dear_Diary_Slow_RO(Amulet):
    att = 65
    a = [('ro', (0.1, 180))]
    def on(this, c):
        if c.wt == 'bow':
            this.a = [('ro', (0.1, 180)), ('cc',0.14)]

class Odd_Sparrows(Amulet):
    att = 51
    a = [('bc',0.8)]
OS = Odd_Sparrows

class Mega_Friends(Amulet):
    att = 55
    a = [('s',0.3),('fs',0.40)]
MF = Mega_Friends

class Wily_Warriors_Flash_and_Heat(Amulet):
    att = 53
    a = [('sp',0.08),('sp',0.12,'fs')]
WWFH = Wily_Warriors_Flash_and_Heat

class Howling_to_the_Heavens(Amulet):
    att = 65
    a = [('cd',0.20)]
    def on(this, c):
        if c.ele == 'shadow':
            this.a = [('cd',0.20)]
            this.a += [('cc',0.12,'hit15')]
HttH = Howling_to_the_Heavens

class Spirit_of_the_Season(Amulet):
    att = 65
    a = [('a',0.15,'hp100'),('k_paralysis',0.2)]
SotS = Spirit_of_the_Season

class Spirit_of_the_Season_No_HP100(Amulet):
    att = 65
    a = [('k_paralysis',0.2)]

class The_Wyrmclan_Duo(Amulet):
    att = 65
    a = [('s',0.30),
         ('cd',0.17,'hp70')]
TWD = The_Wyrmclan_Duo

class A_New_Years_Battle(Amulet):
    att = 52
    a = [('a',0.08,'hp70'),('cc',0.10, 'hit15')]
ANYB = A_New_Years_Battle

class A_Game_of_Cat_and_Boar(Amulet):
    att = 33
    a = []
    def on(self, c):
        if c.ele == 'light':
            self.a = [('bt', 0.25)]
AGoCaB = A_Game_of_Cat_and_Boar

class The_Plaguebringer(Amulet):
    att = 50
    a = [('k_poison',0.25)]
TP = The_Plaguebringer

class A_Dogs_Day(Amulet):
    att = 62
    def on(this, c):
        if c.ele == 'wind':
            this.a = [('bt',0.25), ('sp',0.1)]
ADD = A_Dogs_Day

amulets = []
for k in list(globals()):
    v = globals()[k]
    if type(v) == type(Conf):
        if v.__module__ == 'slot.a.all':
            amulets.append(v)
