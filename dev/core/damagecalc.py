from ctx import *
import core.condition as m_condition


class Modifier(object):
    _static = {}
    mod_name = '<nop>'
    mod_type = '_nop' or 'atk' or 'def' or 'dmg' or 'x' or 'fs' or 's' #....
    mod_order = '_nop' or 'p' or 'ex' or 'b' # chance dmg for crit 
    mod_value = 0

    @classmethod
    def init(cls):
        cls._static = {}
        cls._static['all_modifiers'] = []


    def __init__(this, name, mtype, morder, value, condition=None):
        this.mod_name = name
        this.mod_type = mtype
        this.mod_order = morder
        this.mod_value = value
        this.mod_condition = condition
        this.__active = 0
        this.on()
        #this._static.all_modifiers.append(this)
        #this.__active = 1

    @classmethod
    def mod(cls, mtype, all_modifiers=None):
        if not all_modifiers:
            all_modifiers = cls._static['all_modifiers']
        m = {}
        for i in all_modifiers:
            if mtype == i.mod_type:
                if i.mod_order in m:
                    m[i.mod_order] += i.get()
                else:
                    m[i.mod_order] = 1 + i.get()
        ret = 1.0
        for i in m:
            ret *= m[i]
        return ret

    def get(this):
        return this.mod_value


    def on(this, modifier=None):
        if this.__active == 1:
            return this
        if modifier == None:
            modifier = this
        if modifier.mod_condition :
            if not m_condition.on(modifier.mod_condition):
                return this

        this._static['all_modifiers'].append(modifier)
        this.__active = 1
        return this


    def off(this, modifier=None):
        if this.__active == 0:
            return this
        this.__active = 0
        if modifier==None:
            modifier = this
        idx = len(this._static['all_modifiers'])
        while 1:
            idx -= 1
            if idx < 0:
                break
            if this._static['all_modifiers'][idx] == modifier:
                this._static['all_modifiers'].pop(idx)
                break
        return this


    def __repr__(this):
        return '<%s %s %s %s>'%(this.mod_name, this.mod_type, this.mod_order, this.mod_value)


class Damagecalc(object):
    @classmethod
    def init(cls):
        Event('dc_cbd')(l_calc) # damageCalculation::calculationBaseDamage


    def __init__(this, src, dst):
        this.src = src
        this.dst = dst


    def calc_basedmg(this, name, src, dst):
        atk = 1.0 * src.mod('atk') * src.base_atk
        _def = dst.mod('def') * dst.base_def
        return 1.5/0.6 * atk / _def * src.mod('dmg') * src.dmg_mod(name)


    def l_calc(this, e):
        src = e.src
        dst = e.dst
        name = e.name

        atk = 1.0 * src.mod('atk') * src.base_atk
        _def = dst.mod('def') * dst.base_def
        e.dmg = 1.5/0.6 * atk / _def * src.mod('dmg') * src.dmg_mod(name)

if __name__ == '__main__':

    class Mod(Modifier):
        pass
    Mod.init()
    m1 = Mod('m1', 'atk', 'p', 0.15)
    print(Mod.mod('atk'))
    print(Mod.mod('def'))

    dc = Damagecalc()
    e = Event('dc_cbd')
