from slot.a import Amulet, Conf


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


#class Together_We_Stand(Amulet):
#    att = 52
#    a = [('sts',0.05),
#         ('s',0.20)]


class FirstRate_Hospitality(Amulet):
    att = 55
    a = [('a',0.08,'hp70'),
         ('bc',0.10)]
FRH = FirstRate_Hospitality


class The_Bustling_Hut(Amulet):
    att = 50
    a = [('bc',0.08), ('sp',0.07,'light')]


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
    a = [('cd',0.20), ('cc',0.12,'water_hit15')]

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
    a = [('resist',25,'paralysis'), ('bt',0.25,'shadow')]


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
    a = [('s',0.20), ('cc',0.14,'axe')]
KFM = Kung_Fu_Masters


class Forest_Bonds(Amulet):
    att = 64
    a = [('sp',0.12,'fs'), ('s',0.40,'bow')]
FB = Forest_Bonds


class Dragon_and_Tamer(Amulet):
    att = 57
    a = [('s',0.40, 'lance')]
DnT = Dragon_and_Tamer


class Twinfold_Bonds(Amulet):
    att = 65
    a = [('a',0.15,'hit15'), ('s',0.40,'dagger')]
TB = Twinfold_Bonds


class Summer_Paladyns(Amulet):
    att = 64
    a = [('s',0.40, 'axe'), ('bc_energy', 1)]


class The_Shining_Overlord(Amulet):
    att = 65
    a = [('dc', 3), ('s',0.40,'sword')]
TSO = The_Shining_Overlord

class Halidom_Grooms(Amulet):
    att = 50
    a = [('bt',0.2), ('bc_energy', 1)]
HG = Halidom_Grooms


class Beach_Battle(Amulet):
    att = 50
    a = [('bt',0.2), ('sp',0.07,'water')]
BB = Beach_Battle


class The_Petal_Queen(Amulet):
    att = 53
    a = [('eprep', 5)]


class Hanetsuki_Rally(Amulet):
    att = 51
    a = [('cc',0.05),('lo',0.4)]
HR = Hanetsuki_Rally


class Indelible_Summer(Amulet):
    att = 52
    a = [('sp',0.09,'water')]
IS = Indelible_Summer


class Sisters_Day_Out(Amulet):
    att = 64
    a = [('fs',0.40), ('fsprep', 3, 0.25)]
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
    a = [('sp',0.06), ('fsprep', 3, 0.25)]
CCC = Castle_Cheer_Corps

class Honest_Repose(Amulet):
    att = 53
    a = [('sp', 10, 'flame')]


class High_Dragon_WP(Amulet):
    att = 39

class Candy_Couriers(Amulet):
    att = 65
    a = [('bk',0.25), ('s',0.40,'wand')]
CC = Candy_Couriers

class From_Whence_He_Comes(Amulet):
    att = 50
    a = [('bt',0.2),
         ('prep',0.25)]
FWHC = From_Whence_He_Comes

class Dear_Diary(Amulet):
    att = 65
    a = [('ro', 0.10), ('cc',0.14,'bow')]
DD = Dear_Diary

class Dear_Diary_RO_30(Amulet):
    att = 65
    a = [('ro', 0.1, 30), ('cc',0.14,'bow')]

class Dear_Diary_RO_60(Amulet):
    att = 65
    a = [('ro', 0.1, 60), ('cc',0.14,'bow')]

class Dear_Diary_RO_90(Amulet):
    att = 65
    a = [('ro', 0.1, 90), ('cc',0.14,'bow')]

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

class Wily_Warriors_Bubble_and_Wood(Amulet):
    att = 54
    a = [('a', 0.13, 'hp70')]

class Wily_Warriors_Air_and_Crash(Amulet):
    att = 49
    a = [('a', 0.2, 'hit15')]

class Howling_to_the_Heavens(Amulet):
    att = 65
    a = [('cd',0.20), ('cc',0.12,'shadow_hit15')]
HttH = Howling_to_the_Heavens

class Spirit_of_the_Season(Amulet):
    att = 65
    a = [('a',0.15,'hp100'),('k_paralysis',0.2)]
SotS = Spirit_of_the_Season

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
    a = [('bt', 0.25,'light')]
AGoCaB = A_Game_of_Cat_and_Boar

class The_Plaguebringer(Amulet):
    att = 50
    a = [('k_poison',0.25)]
TP = The_Plaguebringer

class A_Dogs_Day(Amulet):
    att = 62
    a = [('bt',0.25,'wind'), ('sp',0.1,'wind')]
ADD = A_Dogs_Day

class The_Bridal_Dragon(Amulet):
    att = 64
    a = [('dp',10),('da',0.18)]
TBD = The_Bridal_Dragon

class A_Suit_of_Midnight(Amulet):
    att = 52
    a = [('dp',10), ('ag', 3)]

class Primal_Crisis(Amulet):
    att = 55
    a = [('a', 0.20, 'hit15'), ('cc', 0.10, 'hit15')]
PC = Primal_Crisis

class Felyne_Hospitality(Amulet):
    att = 65
    a = [('cc', 0.10, 'hp70'), ('bc_crit_damage', 0.15)]
FH = Felyne_Hospitality

class Unexpected_Requests(Amulet):
    att = 65
    a = [('lo', 0.50), ('lo_crit_chance', 0.30)]

class The_Lurker_in_the_Woods(Amulet):
    att = 65
    a = [('fs', 0.50), ('bk', 0.25)]

class Prayers_Unto_Him(Amulet):
    att = 64
    a = [('da', 0.18), ('dt', 0.15)]

class An_Ancient_Oath(Amulet):
    att = 65
    a = [('da', 0.18), ('dc', 4)]

class The_Fires_of_Hate(Amulet):
    att = 65
    a = [('k_poison', 0.2), ('a', 0.15, 'hp100')]

class The_Queen_of_the_Knife(Amulet):
    att = 52
    a = [('cd', 0.13), ('cc', 0.1, 'hit15')]

class Breakfast_at_Valerios(Amulet):
    att = 65
    a = [('cc', 0.08, 'hp70'), ('a', 0.2, 'hit15')]

class Brothers_in_Arms(Amulet):
    att = 65
    a = [('bc',0.13), ('bk', 0.25)]

class A_Small_Courage(Amulet):
    att = 52
    a = [('bc',0.08), ('a', 0.13, 'hp100')]

class The_Red_Impulse(Amulet):
    att = 65
    a = [('dcs', 3), ('dc', 3)]

class Proper_Maintenance(Amulet):
    att = 64
    a = [('a', 0.15, 'hp100'),('bt',0.20)]

class His_Clever_Brother(Amulet):
    att = 51
    a = [('k_frostbite',0.20),('sp',0.05)]

class Memory_of_a_Friend(Amulet):
    att = 64
    a = [('sp', 0.08), ('a', 0.2, 'hit15')]

amulets = []
for k in list(globals()):
    v = globals()[k]
    if type(v) == type(Conf):
        if v.__module__ == 'slot.a.all':
            amulets.append(v)
