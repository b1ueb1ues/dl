from slot.a import *


class PP(Amulet): #Plunder Pals or Hitting the Books
    att = 54
    a = [('s',0.25)]

class RR(Amulet):
    att = 64
    a = [('s',0.25),
         ('cc',0.06,'hp70')]

class LC(Amulet):
    att = 64
    a = [('cd',0.13),
         ('cc',0.08,'hp70')]

class VC(Amulet):
    att = 65
    a = [('s',0.25),
         ('bc',0.08)]

class FG(Amulet): # Flash of Genius
    att = 57
    a = [('a',0.15,'15hits')]

class FP(Amulet):
    att = 52
    a = [('fs',0.30),
         ('s',0.15)]

class Bellathorna(Amulet):
    att = 25
    a = [('bt',0.15)]


class Together_We_Stand(Amulet):
    att = 52
    a = [('sts',0.04),
         ('s',0.15)]

class Jewels_of_the_Sun(Amulet):
    att = 64
    a = [('sp',0.06),
         ('a',0.08,'hp70')]

class One_with_the_Shadows(Amulet):
    att = 51
    a = [('cc',0.05),
         ('bk',0.15)]

class Flower_in_the_Fray(Amulet):
    att = 52
    a = [('cd',0.13),
         ('s',0.15)]

class The_Prince_of_Dragonyule(Amulet):
    att = 63
    a = [('cd',0.15)]
    def on(this, c):
        if c.ele == 'water':
             this.a += [('cc',0.10,'hit15')]


class Crystalian_Envoy(Amulet):
    att = 57
    a = [('a',0.10,'hp70')]
    

class Evening_of_Luxury(Amulet): 
    att = 65
    a = [('a',0.13,'hp100'),
         ('cd',0.13)]


class The_Chocolatiers(Amulet):
    att = 62
    a = [('prep',100)]


class Worthy_Rivals(Amulet):
    att = 64
    a = [('bk',0.25),
         ('prep',20)]


class Lord_of_the_Skies(Amulet):
    att = 46
    a = [('od',0.08)]


class Witchs_Kitchen(Amulet):
    att = 57
    a = [('s',0.35,'hp100'),
         ('resist',25,'blind')]

class Silke_Lends_a_Hand(Amulet):
    att = 42
    a = [('s',0.15),
         ('resist',25,'blind')]

class Saintly_Delivery(Amulet):
    att = 42
    a = [('s',0.15),
         ('resist',25,'stun')]

class Luck_of_the_Draw(Amulet):
    att = 33
    a = [('resist',20,'paralysis')]
    def on(this, c):
        if c.ele == 'shadow':
            this.a += [('bt',0.20)]

class Lunar_Festivities(Amulet):
    att = 51
    a = [('fs',0.30),
         ('sp',0.08,'fs')]

class The_Warrioresses(Amulet):
    att = 52
    a = [('fs',0.30),
         ('cd',0.10)]

class Stellar_Show(Amulet):
    att = 65
    a = [('fs',0.40),
         ('cd',0.13)]

class KFM(Amulet):
    att = 64
    a = [('s',0.15)]
    def on(this, c):
        if c.wt == 'axe':
            this.a += [('cc',0.12)]

class Forest_Bonds(Amulet):
    att = 64
    a = [('sp',0.10)]
    def on(this, c):
        if c.wt == 'bow':
            this.a += [('s',0.35)]

class Dragon_and_Tamer(Amulet):
    att = 57
    def on(this, c):
        if c.wt == 'lance':
            this.a += [('s',0.35)]

class The_Shining_Overlord(Amulet):
    att = 65
    a = [('dc',2)]
    def on(this, c):
        if c.wt == 'sword':
            this.a += [('s',0.35)]

