from adv import *


class Energy():
    def e_dmg_proc(this, name, amount):
        this.dmg_proc_old(name, amount)  # should prevent damage in next dmg_proc

        if not this.energized :
            return
        if this.energized == 1 and name[0] != 's':
            return

        if this.energized == 1:
            if this.energy_consume and this.energy_consume[name[:2]]:
                this.energized = name[:2]
            else:
                this.energized = name[:2]

        if this.energized == name[:2] :
            boost = this.get_energy_boost()
            log('dmg','o_%s_energized'%name,amount*boost, 'energy boost')

    def get_energy_boost(this):
            sd = this.a.mod('s')
            this.energy_mod.on()
            sd2 = this.a.mod('s')
            this.energy_mod.off()
            return sd2/sd-1



    def __call__(this):
        if this.energized :
            return 5
        else:
            return this.energy

    def add_energy(this, name, n=1):
        self = 0
        team = 0

        if name == 'self':
            self = n
        elif name == 'team':
            team = n
            log('energy','team',team)

        if name in this.energy_self:
            self = this.energy_self[name]

        if name in this.energy_team:
            team = this.energy_team[name]
            if team:
                log('energy','team',team)

        if not this.energized:
            this.energy += self
            if this.energy > 0:
                this.energy_buff.set(this.energy).on()
            if this.energy >= 5 :
                this.energy = 0
                this.energized = 1
                this.energized_event()



    def e_s1_proc(this, e):
        this.add_energy('s1')
        this.s1_proc_old(e)
        if this.energized and this.energized != 1 :
            this.energized = 0
            this.energy_buff.off()


    def e_s2_proc(this, e):
        this.add_energy('s2')
        this.s2_proc_old(e)
        if this.energized and this.energized != 1 :
            this.energized = 0
            this.energy_buff.off()


    def e_s3_proc(this, e):
        this.add_energy('s3')
        this.s3_proc_old(e)
        if this.energized and this.energized != 1 :
            this.energized = 0
            this.energy_buff.off()

    def l_add_energy(this, e):
        this.add_energy(e.name)



    def __init__(this, a, self, team, consume=None):
        this.a = a
        this.energy_self = self
        this.energy_team = team
        this.energy_consume = consume

        this.energy_mod = Modifier('energy_mod','s','passive',0.5).off()

        this.energy = 0
        this.energized = 0
        this.energized_event = Event('energized')

        this.energy_buff = Buff('energy',-1,-1,'energy','energy')

        this.s1_proc_old = a.s1_proc
        this.s2_proc_old = a.s2_proc
        this.s3_proc_old = a.s3_proc
        this.dmg_proc_old = a.dmg_proc

        #a.add_energy = this.add_energy
        a.s1_proc = this.e_s1_proc
        a.s2_proc = this.e_s2_proc
        a.s3_proc = this.e_s3_proc
        a.dmg_proc = this.e_dmg_proc

        Listener('add_energy', this.l_add_energy)


