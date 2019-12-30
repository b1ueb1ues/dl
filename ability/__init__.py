class Ability(object):
    def __init__(this, name, value, cond=None):
        this.name = name
        this.value = value
        this.cond = cond
        this.mod = []
        if name == 'a' or name == 'att':
            this.mod = [('att','passive',value, cond)]
        elif name == 's' or name == 'sd':
            this.mod = [('s','passive',value, cond)]
        elif name == 'cc':
            this.mod = [('crit','chance',value, cond)]
        elif name == 'cd':
            this.mod = [('crit','damage',value, cond)]
        elif name == 'fs':
            this.mod = [('fs','passive',value, cond)]
        elif name == 'bt':
            this.mod = [('buff','time',value, cond)]
        elif name == 'k':
            this.mod = [('att','killer',value, cond)]


        elif name == 'sp':
            if cond != 'fs':
                this.mod = [('sp','passive',value, cond)]

        elif name == 'bk':
            this.mod = [('att','bk',value*0.15, cond)]
        elif name == 'od':
            this.mod = [('att','killer',value*0.35, cond)]

        elif name == 'ex':
            if value == 'blade':
                this.mod = [('att','ex',0.10)]
            elif value == 'dagger':
                this.mod = [('crit','chance',0.10)]
            elif value == 'bow':
                this.mod = [('sp','passive',0.15)]
            elif value == 'wand':
                this.mod = [('s','ex',0.15)]
            elif value == 'hmym':
                this.mod = [('crit','damage',0.3)]


    def ex_dmg_make(this, name, dmg_coef, dtype=None):
        count = this.adv_dmg_make(name, dmg_coef, dtype)

        if dtype == None:
            dtype = name
        if dtype[:2] == 'o_':
            dtype = dtype[2:]
        if dtype[0] == 's':
            this.adv.log('dmg', 'o_ex_wand', count*0.15)


    def defchain(this, e):
        this.adv.Buff('defchain',this.value,15).on()

    def get_killer(this):
        aff = vars(this.adv.afflics)[this.ktype]
        return aff.get()*this.kvalue


    def ex_true_dmg(this, e):
        if 'dtype' in vars(e):
            if e.dtype == 's':
                this.adv.log('dmg', 'o_ex_wand', e.count*0.15, e.comment)

        if e.name[:2] == 'o_':
            e.name = e[2:]
        if e.name[0] == 's':
            this.adv.log('dmg', 'o_ex_wand', e.count*0.15, e.comment)


    def ex_wand(this, adv):
        this.adv = adv
        this.adv_dmg_make = adv.dmg_make
        adv.dmg_make = this.ex_dmg_make
        adv.Listener('true_dmg', this.ex_true_dmg)


    def oninit(this, adv, afrom=None):
        this.adv = adv
        name = this.name
        cond = this.cond
        value = this.value

        if name == 'sp':
            if cond == 'fs':
                adv.conf.fs.sp *=(1+value)
        elif name == 'lo':
            if adv.condition('last offense'):
                adv.Buff('lo',value,15).on()
        elif name == 'bc':
            e = adv.Event('defchain').listener(this.defchain)
            this.adv = adv
        elif name == 'sts':
            adv.Buff('strikerstrength',value*5,-1).on()
        elif name == 'sls':
            adv.Buff('slayerstrength',value*5,-1).on()
        elif name == 'dc':
            adv.Buff('dragonclaw',(float(value)+3.0)/200.0,-1).on()
        elif name == 'ro':
            if isinstance(value, tuple) and len(value) == 2:
                buff_value, timing = value
            else:
                buff_value, timing = value, 30
            if adv.condition('RO proc at 0s {}s {}s'.format(timing, timing*2)):
                def ro_buff(t):
                    adv.Buff('resilient_offense',buff_value, -1).on()
                ro_buff(0)
                adv.Timer(ro_buff).on(timing)
                adv.Timer(ro_buff).on(timing*2)
        elif name == 'uo':
            if isinstance(value, tuple) and len(value) == 2:
                buff_value, timing = value
            else:
                buff_value, timing = value, 20
            if adv.condition('UO proc every {}s'.format(timing)):
                def uo_buff(t):
                    adv.Buff('unyielding_offense',buff_value, -1).on()
                uo_buff(0)
                for i in range(1, 5):
                    adv.Timer(uo_buff).on(timing*i)
        elif name == 'prep':
            if type(value) == int:
                adv.charge_p('amulet prep',"%d%%"%value)
            if type(value) == str:
                adv.charge_p('amulet prep',value)
            if type(value) == float:
                adv.charge_p('amulet prep',"%d%%"%(value*100))
        elif name == 'resist':
            adv.conf.resist = (cond, value)
        elif name[:2] == 'k_':
            this.m = adv.Modifier('afflic_killer','att','killer',0.0)
            this.m.get = this.get_killer
            this.kvalue = value
            this.ktype = name[2:]

#        elif name == 'ex' and value == 'wand':
#            this.ex_wand(adv)

        j = this.mod
        i = ''
        if afrom :
            i = afrom
        i += name
        if cond:
            i += cond

        if type(j) == tuple:
            adv.Modifier(i,*j)
        elif type(j) == list:
            idx = 0
            for k in j:
                adv.Modifier(i+'_%d'%idx,*k)
                idx += 1
        elif type(j) == dict:
            idx = 0
            for k in j:
                adv.Modifier(i+k+'_%d'%idx,*j[k])
                idx += 1


    def __repr__(this):
        return str((this.name,this.value,this.cond))

    def __str__(this):
        return str((this.name,this.value,this.cond))

