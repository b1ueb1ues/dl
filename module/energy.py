def e_dmg_proc(this, name, amount):
    if not this.energized :
        return
    if name[0] != 's':
        return
    if name[:2] == this.energized:
        this.dmg_make('o_energizedmg_'+this.name, amount*0.4)
    if this.energy_consume[name[:2]]:
        this.energizing = name



def add_energy(this, count):
    if this.energized == 1:
        return
    this.energy += count
    log("energy",'+',this.energy)
    if this.energy >= 5 :
        this.energy = 0
        this.energized = 1
        Event('energized').trigger()


def e_s1_proc(this, e):
    add_energy(this, energy_produce['s1'])
    this.s1_proc_old()


def e_s2_proc(this, e):
    add_energy(this, energy_produce['s2'])
    this.s2_proc_old()


def e_s3_proc(this, e):
    add_energy(this, energy_produce['s3'])
    this.s3_proc_old()


def init(a, produce, consume):
    this.energy = 0
    this.energized = 0
    this.tdmg_e = Event('true_dmg')
    a.energy_produce = produce
    a.energy_consume = consume
    a.s1_proc_old = a.s1_proc
    a.s2_proc_old = a.s2_proc
    a.s3_proc_old = a.s3_proc
    a.dmg_proc_old = a.dmg_proc_old
    a.s1_proc = e_s1_proc
    a.s2_proc = e_s2_proc
    a.s3_proc = e_s3_proc
    a.dmg_proc = e_dmg_proc


