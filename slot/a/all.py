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
BBW = Bonds_Between_Worlds



class LC(Amulet):
    att = 64
    a = [('cd',0.15),
         ('cc',0.10,'hp70')]


class VC(Amulet):
    att = 65
    a = [('s',0.30),
         ('bc',0.10)]

class TL(Amulet):
    att = 65
    a = [('s',0.25),
         ('lo',0.50)]

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

SS = Stellar_Show

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
FB = Forest_Bonds


class Dragon_and_Tamer(Amulet):  #??
    att = 57
    def on(this, c):
        if c.wt == 'lance':
            this.a = [('s',0.40)]
DnT = Dragon_and_Tamer

class The_Shining_Overlord(Amulet):  #??
    att = 65
    a = [('dc',3)]
    def on(this, c):
        if c.wt == 'sword':
            this.a = [('dc',3)]
            this.a += [('s',0.40)]
TSO = The_Shining_Overlord


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
        adv.Listener('defchain',this.dc_energy)

HG = Halidom_Grooms


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

class Sisters_Day_Out(Amulet):
    att = 64
    a = [('fs',0.40)]
    def fs_proc(this, e):
        this.o_fs_proc(e)
        if this.charges > 0:
            this.adv.charge_p('sisters_day_out','25%')
            this.charges -= 1

    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.charges = 3
        this.adv = adv
        this.o_fs_proc = adv.fs_proc
        adv.fs_proc = this.fs_proc

SDO = Sisters_Day_Out

class Elegant_Escort(Amulet):
    att = 54
    def oninit(this, adv):
        Amulet.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('Elegant_Escort','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.burn.get()*0.3
    
        
EE = Elegant_Escort


amulets = []
for k in list(globals()):
    v = globals()[k]
    if type(v) == type(Conf):
        if v.__module__ == 'slot.a.all':
            amulets.append(v)
