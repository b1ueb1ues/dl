class Ability:
    COND_ELE = ('flame', 'water', 'wind', 'light', 'dark')
    COND_WT = ('axe', 'blade', 'bow', 'dagger', 'lance', 'staff', 'sword', 'wand')
    def __init__(self, name, mod=None):
        self.name = name
        self.mod = mod or []

    def check_ele_wt(self, m, adv):
        cond = m[3]
        if '_' in cond:
            classifier, cond = cond.split('_')
        else:
            classifier = cond
            cond = None
        new_m = (m[0], m[1], m[2], cond)
        if classifier in self.COND_ELE:
            return adv.slots.c.ele == classifier, new_m
        elif classifier in self.COND_WT:
            return adv.slots.c.wt == classifier, new_m
        else:
            return True, m

    def flurry_modifier(self, m, adv):
        cond = m[3]
        if cond.startswith('hit'):
            flurry_hits = int(cond[3:])
            def flurry_get():
                return adv.hits >= flurry_hits
            return (m[0], m[1], m[2], cond, flurry_get)
        return m

    def oninit(self, adv, afrom=None):
        if afrom is not None:
            afrom += '_'
        else:
            afrom = ''
        for idx, m in enumerate(self.mod):
            if len(m) > 3 and m[3] is not None:
                is_ele_wt, m = self.check_ele_wt(m, adv)
                if not is_ele_wt:
                    continue
                if m[3] is not None:
                    m = self.flurry_modifier(m, adv)
            adv.Modifier('{}{}_{}'.format(afrom, self.name, idx),*m)


ability_dict = {}

class Strength(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('att','passive',value, cond)])

ability_dict['a'] = Strength
ability_dict['att'] = Strength


class Skill_Damage(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('s','passive',value, cond)])

ability_dict['s'] = Skill_Damage
ability_dict['sd'] = Skill_Damage


class Critical_Chance(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('crit','chance',value, cond)])

ability_dict['cc'] = Critical_Chance


class Critical_Damage(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('crit','damage',value, cond)])

ability_dict['cd'] = Critical_Damage


class Force_Strike(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('fs','passive',value, cond)])

ability_dict['fs'] = Force_Strike


class Buff_Time(Ability):
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('buff','time',value, cond)])

ability_dict['bt'] = Buff_Time


class Killer(Ability):
    def __init__(self, name, value, cond=None):
        if name == 'k':
            super().__init__(name, [('att','killer',value, cond)])
        else:
            afflict = name.split('_')[1]
            super().__init__(name, [('{}_killer'.format(afflict), 'passive', value, cond)])

ability_dict['k'] = Killer


class Skill_Haste(Ability):
    def __init__(self, name, value, cond=None):
        if cond == 'fs':
            super().__init__(name, [('sp','fs',value)])
        else:
            super().__init__(name, [('sp','passive',value, cond)])

ability_dict['sp'] = Skill_Haste


class Broken_Punisher(Ability):
    EFFICIENCY = 0.15
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('att','bk',value*self.EFFICIENCY, cond)])

ability_dict['bk'] = Broken_Punisher


class Overdrive_Punisher(Ability):
    EFFICIENCY = 0.35
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('overdrive_killer','passive',value, cond)])

ability_dict['od'] = Overdrive_Punisher


class Dragon_Damage(Ability):
    EFFICIENCY = 0.35
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('da','passive',value,cond)])

ability_dict['da'] = Dragon_Damage


class Dragon_Time(Ability):
    EFFICIENCY = 0.35
    def __init__(self, name, value, cond=None):
        super().__init__(name, [('dt','passive',value,cond)])

ability_dict['dt'] = Dragon_Time


class Co_Ability(Ability):
    EX_MAP = {
        'blade': [('att','ex',0.10)],
        'dagger': [('crit','chance',0.10)],
        'bow': [('sp','passive',0.15)],
        'wand': [('s','ex',0.15)],
        'sword': [('dh','passive',0.15)],
        'axe2': [('crit','damage',0.30)],
        'geuden': [('da','passive',0.10),('dt','passive',0.20)],
        'tobias': [('buff','time',0.20)]
    }
    def __init__(self, name, value, cond=None):
        try:
            super().__init__(name, self.EX_MAP[value])
        except KeyError:
            super().__init__(name)

ability_dict['ex'] = Co_Ability


class BuffingAbility(Ability):
    def __init__(self, name, value, duration):
        self.buff_args = (name, value, duration, 'att', 'buff')
        if '_' in name:
            self.buff_args = (name, value, duration, *name.split('_')[1:])
        super().__init__(name)

class Last_Offense(BuffingAbility):
    def __init__(self, name, value):
        super().__init__(name, value, 15)

    def oninit(self, adv, afrom=None):
        if adv.condition('last offense'):
            adv.Buff(*self.buff_args).on()
        # super().oninit(adv, afrom)

ability_dict['lo'] = Last_Offense


class Doublebuff(BuffingAbility):
    def __init__(self, name, value):
        super().__init__(name, value, 15)

    def oninit(self, adv, afrom=None):
        if self.name == 'bc_energy':
            def defchain(e):
                adv.energy.add(self.buff_args[1])
            adv.Event('defchain').listener(defchain)
        else:
            def defchain(e):
                adv.Buff(*self.buff_args).on()
            adv.Event('defchain').listener(defchain)

ability_dict['bc'] = Doublebuff


class Slayer_Strength(BuffingAbility):
    def __init__(self, name, value):
        super().__init__(name, value, -1)

    def oninit(self, adv, afrom=None):
        for _ in range(5):
            adv.Buff(*self.buff_args).on()

ability_dict['sts'] = Slayer_Strength
ability_dict['sls'] = Slayer_Strength


class Dragon_Claw(Ability):
    DC_LEVELS = {
        1: (0.04,0.06,0.10),
        2: (0.05,0.08,0.12),
        3: (0.06,0.09,0.15),
        4: (0.10,0.15,0.15)
    }
    DM_LEVELS = {
        1: (0.10, 0.10)
    }
    def __init__(self, name, value):
        if name == 'dc':
            self.dc_values = self.DC_LEVELS[value]
        elif name == 'dm':
            self.dc_values = self.DM_LEVELS[value]
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        self.dc_level = 0
        def l_dc_buff(t):
            if self.dc_level < len(self.dc_values):
                adv.Buff('dc', self.dc_values[self.dc_level], -1).on()
                self.dc_level += 1
        adv.Event('dragon').listener(l_dc_buff)

ability_dict['dc'] = Dragon_Claw
ability_dict['dm'] = Dragon_Claw


class Resilient_Offense(Ability):
    def __init__(self, name, value, interval=None):
        self.value = value
        if name == 'ro':
            self.proc_chances = 3
            self.interval = interval or 180
        elif name == 'uo':
            self.proc_chances = 5
            self.interval = interval or 30
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        if adv.condition('hp30 every {}s'.format(self.interval)):
            def ro_buff(t):
                adv.Buff(self.name,self.value, -1).on()
            for i in range(self.proc_chances):
                adv.Timer(ro_buff).on(self.interval*i)

ability_dict['ro'] = Resilient_Offense
ability_dict['uo'] = Resilient_Offense


class Skill_Prep(Ability):
    def __init__(self, name, value):
        if name == 'prep_charge':
            self.value = 1
            self.charge = value
        else:
            self.value = value
            if isinstance(self.value, str):
                self.value = float(value.replace('%', ''))
            if self.value > 1:
                self.value /= 100
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        adv.charge_p('skill prep',self.value)
        if self.name == 'prep_charge':
            def l_skill_charge(e):
                adv.charge_p('skill_charge',self.charge)
            adv.Event('s').listener(l_skill_charge)

ability_dict['prep'] = Skill_Prep


class Resist(Ability):
    def __init__(self, name, value, cond=None):
        self.resist = (cond, value)
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        adv.conf.resist = self.resist

ability_dict['resist'] = Resist


class Primed(BuffingAbility):
    PRIMED_CD = 15
    def __init__(self, name, value, duration=None):
        self.is_cd = False
        super().__init__(name, value, duration or 10)

    def oninit(self, adv, afrom=None):        
        def pm_cd_end(t):
            self.is_cd = False
                    
        def l_primed(e):
            if not self.is_cd:
                buff = adv.Buff(*self.buff_args)
                buff.bufftime = buff.nobufftime
                buff.on()
                self.is_cd = True
                adv.Timer(pm_cd_end).on(self.PRIMED_CD)

        adv.Event('s1_charged').listener(l_primed)

ability_dict['primed'] = Primed


class Dragon_Prep(Ability):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)

    def oninit(self, adv, afrom=None):        
        adv.dragonform.dragon_gauge += self.value

ability_dict['dp'] = Dragon_Prep


class Affliction_Guard(Ability):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)

    def oninit(self, adv, afrom=None):        
        adv.afflict_guard = self.value

ability_dict['ag'] = Affliction_Guard

class Energy_Prep(Ability):
    def __init__(self, name, value):
        self.energy_count = value
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        adv.energy.add(self.energy_count)

ability_dict['eprep'] = Energy_Prep


class Force_Charge(Ability):
    def __init__(self, name, charge, value=0.25):
        self.charge = charge
        self.value = value
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        if hasattr(adv, 'fs_prep_c'):
            adv.fs_prep_v += self.value
        else:
            def l_fs_charge(e):
                diff = min(adv.conf.fs.hit, self.charge)
                for _ in range(diff):
                    adv.charge_p(self.name, adv.fs_prep_v)
                self.charge -= diff
                adv.fs_prep_c = self.charge
                if self.charge == 0:
                    self.l_fs_charge.off()
            self.l_fs_charge = adv.Listener('fs', l_fs_charge)
            adv.fs_prep_c = self.charge
            adv.fs_prep_v = self.value

ability_dict['fsprep'] = Force_Charge

class Energized_Buff(BuffingAbility):
    def __init__(self, name, value, duration=None):
        super().__init__(name, value, duration or 15)

    def oninit(self, adv, afrom=None):                            
        def l_energized(e):
            if e.stack >= 5:
                adv.Buff(*self.buff_args).on()

        adv.Event('energy').listener(l_energized)

ability_dict['energized'] = Energized_Buff

class Energy_StrCrit(Ability):
    STR_LEVELS = {
        3: (0.0, 0.04, 0.06, 0.08, 0.10, 0.20),
        7: (0.0, 0.05, 0.10, 0.20, 0.30, 0.40)
    }
    CRIT_LEVELS = {
        3: (0.0, 0.01, 0.02, 0.03, 0.04, 0.08),
        7: (0.0, 0.01, 0.04, 0.07, 0.10, 0.15)
    }
    def __init__(self, name, value):
        # self.atk_buff = Selfbuff('a1atk',0.00,-1,'att','passive').on()
        # self.a1crit = Selfbuff('a1crit',0.00,-1,'crit','chance').on()
        self.att_values = self.STR_LEVELS[value]
        self.crit_values = self.CRIT_LEVELS[value]
        super().__init__(name)

    def oninit(self, adv, afrom=None):
        self.att_buff = adv.Selfbuff('epassive_att', 0.00,-1,'att', 'passive').on()
        self.crit_buff = adv.Selfbuff('epassive_crit', 0.00,-1,'crit', 'chance').on()
        def l_energy(e):
            self.att_buff.off()
            self.crit_buff.off()
            self.att_buff.set(self.att_values[e.stack])
            self.crit_buff.set(self.crit_values[e.stack])
            self.att_buff.on()
            self.crit_buff.on()
        adv.Event('energy').listener(l_energy)

ability_dict['epassive'] = Energy_StrCrit
