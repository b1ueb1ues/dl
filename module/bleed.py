from core.advbase import *

class Bleed(Dot):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0

    def __init__(this, name, dmg_coef):
        Dot.__init__(this, name, dmg_coef, 30, 4.99)
        this.quickshot_event = Event("dmg_formula")
        this.quickshot_event.dmg_coef = dmg_coef
        this.quickshot_event.dname = 's_bleed'
        this.dot_end_timer = Timer(this.dot_end_proc)
        this.true_dmg_event = Event("true_dmg")
        this.true_dmg_event.dname = 'o_bleed'
        this.true_dmg_event.dtype = 's'

    def reset(this):
        this._static['all_bleeds'] = []
        this._static['stacks'] = 0
        return this

    def tick_proc(this, e):
        dmg_sum = 0
        stacks = this._static['stacks']
        for i in this._static['all_bleeds']:
            dmg_sum += i.quickshot_event.dmg
        if stacks == 1:
            dmg = dmg_sum
        elif stacks == 2:
            dmg = dmg_sum * 1.5
        elif stacks == 3:
            dmg = dmg_sum * 2
        else:
            print("err in bleed tick_proc")
            exit()
        this.true_dmg_event.comment = "%d stacks"%stacks
        this.true_dmg_event.count = dmg 
        this.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += this.iv

    def dot_end_proc(this, e):
        idx = this._static['all_bleeds'].index(this)
        this._static['all_bleeds'].pop(idx)
        this._static['stacks'] -= 1
        log('debuff','bleed','stack_end',"stack <%d>"%this._static['stacks'])
        if this._static['stacks'] < 0:
            print('err in bleed dot_end_proc')
            exit()
        if this._static['stacks'] == 0:
            this._static['tick_event'].off()


    def on(this):
        if this._static['stacks'] == 3:
            log('resist','bleed')
            return
        elif this._static['stacks'] > 3:
            print("err in bleed on")
            exit()

        log('debuff','bleed')
        this.quickshot_event()
        this._static['all_bleeds'].append(this)
        this.dot_end_timer.on(this.duration)

        if this._static['stacks'] == 0:
            this._static['tick_event'] = Timer(this.tick_proc).on(this.iv)
        elif this._static['stacks'] < 3:
            pass
        this._static['stacks'] += 1


class mBleed(Bleed):
    _static = {}
    _static['all_bleeds'] = []
    _static['stacks'] = 0

    def tick_proc(this, e):
        dmg_sum = 0
        stacks = this._static['stacks']
        for i in this._static['all_bleeds']:
            dmg_sum += i.quickshot_event.dmg
        if stacks == 1:
            #this.tdmg_event.dmg = dmg_sum
            dmg = dmg_sum * 0.8
        elif stacks == 2:
            #this.tdmg_event.dmg = dmg_sum * 1.5
            dmg = dmg_sum * 1.12
        elif stacks == 3:
            #this.tdmg_event.dmg = dmg_sum * 2
            dmg = dmg_sum * 1.44
        else:
            print("err in bleed tick_proc")
            exit()

        this.true_dmg_event.comment = "%d stacks"%stacks
        this.true_dmg_event.count = dmg 
        this.true_dmg_event.on()
        #log("dmg",'o_bleed',dmg,"%d stacks"%stacks)
        e.timing += this.iv

            
