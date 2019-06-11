from slot.a import *


class PP(Amulet): #Plunder Pals or Hitting the Books
    att = 54
    a = [('s',0.25)]

class RR(Amulet):
    att = 64
    a = [('s',0.30),
         ('cc',0.08,'hp70')]

class CE(Amulet): 
    att = 57
    a = [('a',0.13,'hp70')]

class Bonds_Between_Worlds(Amulet):
    att = 54
    a = [('a',0.13,'hp70'),
         ('prep',25)]

Bonds = Bonds_Between_Worlds
    


class LC(Amulet):
    att = 64
    a = [('cd',0.15),
         ('cc',0.10,'hp70')]


class VC(Amulet):
    att = 65
    a = [('s',0.30),
         ('bc',0.10)]

class FoG(Amulet): # Flash of Genius
    att = 57
    a = [('a',0.20,'hit15')]
FG = FoG

class FP(Amulet):
    att = 52
    a = [('fs',0.40),
         ('s',0.20)]

class Bellathorna(Amulet):
    att = 25
    a = [('bt',0.20)]


#class Together_We_Stand(Amulet):
#    att = 52
#    a = [('sts',0.05),
#         ('s',0.20)]

class First_Rate_Hospitality(Amulet):
    att = 55
    a = [('a',0.08,'hp70'),
         ('bc',0.10)]

class Jewels_of_the_Sun(Amulet):
    att = 64
    a = [('sp',0.08),
         ('a',0.10,'hp70')]
JotS = Jewels_of_the_Sun

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

class The_Prince_of_Dragonyule(Amulet):  
    att = 63
    a = [('cd',0.15)]
    def on(this, c):
        if c.ele == 'water':
            this.a = [('cd',0.20)]
            this.a += [('cc',0.12,'hit15')]



class Evening_of_Luxury(Amulet): 
    att = 65
    a = [('a',0.15,'hp100'),
         ('cd',0.15)]


class The_Chocolatiers(Amulet):
    att = 62
    a = [('prep',100)]


class Worthy_Rivals(Amulet):
    att = 64
    a = [('bk',0.30),
         ('prep',25)]


class Lord_of_the_Skies(Amulet):
    att = 46
    a = [('od',0.10)]


class Witchs_Kitchen(Amulet):  #??
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

class Lunar_Festivities(Amulet): #??
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

class KFM(Amulet):
    att = 64
    a = [('s',0.20)]
    def on(this, c):
        if c.wt == 'axe':
            this.a = [('s',0.20)]
            this.a += [('cc',0.14)]

class Forest_Bonds(Amulet):
    att = 64
    a = [('sp',0.12,'fs')]
    def on(this, c):
        if c.wt == 'bow':
            this.a = [('sp',0.12,'fs')]
            this.a += [('s',0.40)]

class Dragon_and_Tamer(Amulet):  #??
    att = 57
    def on(this, c):
        if c.wt == 'lance':
            this.a = [('s',0.40)]

class The_Shining_Overlord(Amulet):  #??
    att = 65
    a = [('dc',3)]
    def on(this, c):
        if c.wt == 'sword':
            this.a = [('dc',3)]
            this.a += [('s',0.40)]

amulets = []
for k in list(globals()):
    v = globals()[k]
    if type(v) == type(Conf):
        if v.__module__ == 'slot.a.all':
            amulets.append(v)
