from adv.advbase import *

class Bleed(Dot):
    _static = Static()
    _static.all_bleeds = []
    _static.stacks = 0

    def __init__(this, name, dmg_p):
        Dot.__init__(this, name, dmg_p, 30, 4.99)
        this.tdmg_event = Event("true_dmg")
        this.tdmg_event.name = "o_bleed"
        this.tdmg_event.comment = ""
        this.quickshot_event = Event("dmg_formula")
        this.quickshot_event.dmg_p = dmg_p
        this.dot_end_event = Event("bleed_end", this.dot_end_proc)

    def tick_proc(this, e):
        dmg_sum = 0
        stacks = this._static.stacks
        for i in this._static.all_bleeds:
            dmg_sum += i.quickshot_event.dmg
        if stacks == 1:
            this.tdmg_event.dmg = dmg_sum
        elif stacks == 2:
            this.tdmg_event.dmg = dmg_sum * 1.5
        elif stacks == 3:
            this.tdmg_event.dmg = dmg_sum * 2
        else:
            print "err in bleed tick_proc"
            exit()
        this.tdmg_event.comment = "%d stacks"%(stacks)
        this.tdmg_event.trigger()
        e.timing += this.iv

    def dot_end_proc(this, e):
        idx = this._static.all_bleeds.index(this)
        this._static.all_bleeds.pop(idx)
        this._static.stacks -= 1
        if this._static.stacks < 0:
            print 'err in bleed dot_end_proc'
            exit()
        if this._static.stacks == 0:
            this._static.tick_event.off()


    def on(this):
        if this._static.stacks == 3:
            log('resist','bleed')
            return
        elif this._static.stacks > 3:
            print "err in bleed on"
            exit()

        this.quickshot_event.trigger()
        this._static.all_bleeds.append(this)
        this.dot_end_event.on(now()+this.duration)

        if this._static.stacks == 0:
            this._static.tick_event = Event("bleed_tick", this.tick_proc).on(now()+this.iv)
        elif this._static.stacks < 3:
            pass
        this._static.stacks += 1



            
