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
            if cond == 'fs':
                this.mod = [('sp','fs',value)]
            else:
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

        # if name == 'sp':
        #     if cond == 'fs':
        #         # adv.conf.fs.sp *=(1+value)
        #         name = 'sp_fs'
        if name[:2] == 'lo':
            if len(name) > 2:
                buff_args = name[3:].split('_')
            else:
                buff_args = ('att', 'buff')
            if adv.condition('last offense'):
                adv.Buff(name,value,15,*buff_args).on()
        elif name[:2] == 'bc':
            if len(name) > 2:
                buff_args = name[3:].split('_')
            else:
                buff_args = ('att', 'buff')
            def defchain(e):
                adv.Buff('defchain',value,15,*buff_args).on()
            adv.Event('defchain').listener(defchain)
        elif name == 'sts':
            for _ in range(5):
                adv.Buff('striker_strength',value,-1).on()
        elif name == 'sls':
            for _ in range(5):
                adv.Buff('slayerstrength',value,-1).on()
        elif name == 'dc':
        #     # adv.Buff('dragonclaw',(float(value)+3.0)/200.0,-1).on()
        #     if hasattr(adv, 'no_dclaws') and not adv.no_dclaws:
        #         from adv.adv_test import sim_duration
        #         timing = int(sim_duration/2)
        #         buff_value = value
        #         def dc_buff(t):
        #             if adv.condition('shapeshift at {}s'.format(timing)):
        #                 adv.Buff('dragons_claw', buff_value, -1).on()
        #         adv.dragon_claw_buff = adv.Timer(dc_buff)
        #         adv.dragon_claw_buff.on()
        # elif name == 'dc_true': # real dclaws, based on Event('dragon')
            from core.timeline import Event
            dc_levels = {
                1: (0.04,0.06,0.10),
                2: (0.05,0.08,0.12),
                3: (0.06,0.09,0.15),
                4: (0.10,0.15,0.15)
            }
            this.dc_values = dc_levels[value]
            this.dc_level = 1
            def l_dc_buff(t):
                if this.dc_level <= len(this.dc_values):
                    adv.Buff('dc{}_{}'.format(value, this.dc_level), this.dc_values[this.dc_level-1], -1).on()
                    this.dc_level += 1
            Event('dragon').listener(l_dc_buff)
        elif name == 'ro':
            if isinstance(value, tuple) and len(value) == 2:
                buff_value, timing = value
            else:
                buff_value, timing = value, 90
            if adv.condition('hp30 every {}s'.format(timing)):
                def ro_buff(t):
                    adv.Buff('resilient_offense',buff_value, -1).on()
                ro_buff(0)
                for i in range(1, 3):
                    adv.Timer(ro_buff).on(timing*i)        
        elif name == 'uo':
            if isinstance(value, tuple) and len(value) == 2:
                buff_value, timing = value
            else:
                buff_value, timing = value, 20
            if adv.condition('hp70 every {}s'.format(timing)):
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
        elif name == 'prep_charge':
            adv.charge_p('amulet prep','100%')
            if type(value) == int:
                value = "%d%%"%value
            if type(value) == float:
                value = "%d%%"%(value*100)
            def skill_charge(e):
                adv.charge_p('skill charge',value)
            this.l_s = adv.Listener('s', skill_charge)
        elif name == 'resist':
            adv.conf.resist = (cond, value)
        elif name[:2] == 'k_':
            this.m = adv.Modifier('afflic_killer',name[2:] + '_killer','passive',value)
        elif name[:7] == 'primed_':
            from core.timeline import Event, Timer
            if isinstance(value, tuple) and len(value) == 2:
                buff_value, timing = value
            else:
                buff_value, timing = value, 10
            
            this.pm_is_cd = False
            def pm_cd_end(t):
                this.pm_is_cd = False
                adv.log('cd',name,'end')
                        
            def l_primed(e):
                if not this.pm_is_cd:
                    if name[7:] == 'def':
                        buff = adv.Buff(name,0,timing,'def')
                        buff.bufftime = buff.nobufftime
                        buff.on()
                        Event('defchain')()
                    else:
                        buff_args = name[7:].split('_')
                        buff = adv.Buff(name,buff_value,timing,*buff_args)
                        buff.bufftime = buff.nobufftime
                        buff.on()
                    this.pm_is_cd = True
                    Timer(pm_cd_end).on(15)

            Event('s1_charged').listener(l_primed)

#        elif name == 'ex' and value == 'wand':
#            this.ex_wand(adv)

        j = this.mod
        i = ''
        if afrom :
            i = afrom
        i += name
        if cond:
            i += cond

        def flurry_get():
            return m.mod_value if adv.hits >= flurry_hits else 0

        if type(j) == tuple:
            m = adv.Modifier(i,*j)
            if cond and cond.startswith('hit'):
                flurry_hits = int(cond[3:])
                m.get = flurry_get
        elif type(j) == list:
            idx = 0
            for k in j:
                m = adv.Modifier(i+'_%d'%idx,*k)
                idx += 1
                if cond and cond.startswith('hit'):
                    flurry_hits = int(cond[3:])
                    m.get = flurry_get
        elif type(j) == dict:
            idx = 0
            for k in j:
                m = adv.Modifier(i+k+'_%d'%idx,*j[k])
                idx += 1
                if cond and cond.startswith('hit'):
                    flurry_hits = int(cond[3:])
                    m.get = flurry_get

    def __repr__(this):
        return str((this.name,this.value,this.cond))

    def __str__(this):
        return str((this.name,this.value,this.cond))

