from core.timeline import *
from core.log import *
import random


class Dot(object):
    """
    Damage over time; e.g. poison
    """

    def __init__(this, name, coef, duration, iv):
        this.name = name
        this.active = 0
        this.coef = coef
        this.iv = iv  # Seconds between each damage tick
        this.duration = duration
        this.true_dmg_event = Event('true_dmg')
        this.true_dmg_event.dname = name
        this.true_dmg_event.dtype = 's'
        this.true_dmg_event.comment = ''
        this.tick_dmg = 0
        this.quickshot_event = Event('dmg_formula')
        this.tick_timer = Timer(this.tick_proc)
        this.dotend_timer = Timer(this.dot_end_proc)

    def dot_end_proc(this, t):
        log('dot',this.name,'end\t')
        this.active = 0
        this.tick_timer.off()
        this.cb_end()

    def cb_end(this):
        pass

    def tick_proc(this, t):
        if this.active == 0:
            return
        t.timing += this.iv
        this.true_dmg_event.count = this.tick_dmg
        this.true_dmg_event.on()
        
    def __call__(this):
        return this.on()

    def get(this):
        return this.active

    def on(this):
        if this.active :
            log('dot',this.name,'failed\t')
            return 0
        this.active = 1
        this.tick_timer.on(this.iv)
        this.dotend_timer.on(this.duration)
        this.quickshot_event.dmg_coef = this.coef
        this.quickshot_event.dname = 's_dot'
        this.quickshot_event()
        this.tick_dmg = this.quickshot_event.dmg
        log('dot',this.name,'start\t','%f/%d'%(this.iv,this.duration))
        return 1

    def off(this):
        this.tick_timer.off()
        this.dotend_timer.off()
        log('dot',this.name,'end by other reason')



    
class Afflic(object):
    class Node(object):
        resist_after = 0
        chance = 0
        proc = 0
        lnode = 0
        rnode = 0
        def __init__(this, chance, resist_after, proc):
            this.chance = chance
            this.resist_after = resist_after
            this.proc = proc

        def add(this, rate, tolerance):
            if this.resist_after >= 1:
                this.lnode = Afflic.Node(this.chance, 1, 0)
                this.rnode = 0 #Afflic.Node(0, 1, 0)
                return
            if rate <= this.resist_after:
                this.lnode = Afflic.Node(this.chance, this.resist_after, 0)
                this.rnode = 0 #Afflic.Node(0, this.resist_after, 0)
                return

            chance = rate-this.resist_after
            if chance > 1:
                chance = 1
            if chance == 1:
                this.lnode = 0 #Afflic.Node(this.chance * (1-chance), this.resist_after, 0)
                this.rnode = Afflic.Node(this.chance , this.resist_after+tolerance, 1)
                return
            this.lnode = Afflic.Node(this.chance * (1-chance), this.resist_after, 0)
            this.rnode = Afflic.Node(this.chance * chance, this.resist_after+tolerance, 1)

    def __init__(this, name=None):
        this.name = name
        this.resist = 0
        this.rate = 1
        this.tolerance = 0.2
        #this.history = 0
        this.history = []
        #this.maxproc = int((this.rate-this.get_resist())/this.get_tolerance()+0.9999)
        this.maxdeep = 25
        this.duration = 12
        this.stack = {}
        this.stack_x_chance = 0.0
        this.tree = []

    def get_tolerance(this):
        if this.tolerance > 1:
            return float(this.tolerance)/100.0
        else:
            return this.tolerance

    def get_rate(this):
        if this.rate > 2:
            return float(this.rate)/100.0
        else:
            return this.rate


    def get_resist(this):
        if this.resist > 1 :
            return float(this.resist)/100.0
        else:
            return this.resist

    def p_tree(this, serial):
        this.tree.append([])
        rate = this.history[serial-1]
        rsum = 0
        if serial == 1:
            root = Afflic.Node(1, this.resist, 0)
            root.add(rate, this.get_tolerance())
            if root.lnode :
                this.tree[serial-1].append(root.lnode)
            if root.rnode :
                this.tree[serial-1].append(root.rnode)
                rsum += root.rnode.chance
        else:
            for i in this.tree[serial-2]:
                i.add(rate, this.get_tolerance())
                if i.lnode:
                    this.tree[serial-1].append(i.lnode)
                if i.rnode:
                    this.tree[serial-1].append(i.rnode)
                    rsum += i.rnode.chance
        return rsum


    def p_recursive(this, count, cmax ,resist):
        rate = this.history[count-1]
        if resist >= 1:
            return 0
        pchance = rate - resist
        if pchance > 1:
            pchance = 1
        if pchance < 0:
            pchance = 0
        if count == cmax:
            return pchance
        p1 = pchance * this.p_recursive(count+1, cmax, resist+this.tolerance)
        p2 = (1-pchance) * this.p_recursive(count+1,cmax, resist)
        return p1+p2


    def stack_end(this, t):
        this.stack.pop(t)


    def get(this):
        nostackchance = 1.0
        for i in this.stack:
            nostackchance *= (1.0-this.stack[i])
        return 1.0-nostackchance

    def __call__(this, *args, **argv):
        return this.on(*args, **argv)

    def on(this):
        this.resist = this.get_resist()
        this.rate = this.get_rate()
        this.tolerance = this.get_tolerance()
        this.history.append(this.rate)
        t = Timer(this.stack_end)
        count = len(this.history)
        #in order not too deep
        #if count > (1-this.resist)/this.tolerance*5:
        if count > this.maxdeep:
            return 0
        else:
            t.p = this.p_recursive(1, count, this.resist)
            #t.p = this.p_tree(count)
            this.stack[t] = t.p
            t.on(this.duration)
            return t.p

class Afflic_dot(Afflic):
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.coef = 0.97
        this.iv = 3.99
        this.duration = 12

    def on(this, name, rate, coef, duration=None, iv=None):
        this.rate = rate
        this.coef = coef
        if duration:
            this.duration = duration
        if iv:
            this.iv = iv
        r = Afflic.on(this)
        coef_x_chance = r * this.coef
        Dot('o_%s_%s'%(name, this.name) ,coef_x_chance, this.duration, this.iv).on()
        return r

class Afflic_cc(Afflic):
    _static = Static({
        'active_name': 0,
        'active_cc': 0,
        })
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.cc = Dot('',0,0,0)

    def on(this, name, rate, duration=None):
        this.rate = rate
        if duration:
            this.duration = duration

        if this._static.active_cc and this._static.active_cc.get():
            if this._static.active_name == this.name:
                this.cc.on()
                return 0
            else:
                r = Afflic.on(this)
                if random.random() < r:
                    this._static.active_cc.off()
                    this.cc = Dot('o_%s_%s'%(name, this.name), 0, this.duration, this.duration+0.001)
                    this.cc.cb_end = this.cb_end
                    this.cc.on()
                    this._static.active_name = this.name
                    this._static.active_cc = this.cc
                    return 1
                else:
                    log('debug','cc', 'miss %f'%r, '%s_%s'%(name,this.name))
                    return 0
        else:
            # clean now
            log('debug','cc', 'clean')
            this.cc = Dot('o_%s_%s'%(name, this.name), 0, this.duration, this.duration+0.001)
            this.cc.cb_end = this.cb_end
            this.cc.on()
            this._static.active_name = this.name
            this._static.active_cc = this.cc
            return Afflic.on(this)

    def cb_end(this):
        pass


class Afflic_scc(Afflic):
    def __init__(this, name=None):
        Afflic.__init__(this, name)
        this.cc = Dot('',0,0,0)

    def on(this, name, rate, duration=None):
        this.rate = rate
        if duration:
            this.duration = duration
        if this.cc.get():
            this.cc.cb_end = this.cb_end
            this.cc.on()
            return 0
        this.cc = Dot('o_%s_%s'%(name, this.name) ,0, this.duration, this.duration+0.001)
        this.cc.cb_end = this.cb_end
        this.cc.on()
        return Afflic.on(this)

    def cb_end(this):
        pass



class Afflics(object):
    def __init__(this):
        this.rinit()
        this.poison = Afflic_dot('poison')
        this.poison.duration = 15
        this.poison.iv = 2.99

        this.burn = Afflic_dot('burn')
        this.burn.duration = 12
        this.burn.iv = 3.99

        this.paralysis = Afflic_dot('paralysis')
        this.paralysis.duration = 13
        this.paralysis.iv = 3.99

        this.blind = Afflic_scc('blind')
        this.blind.duration = 8

        this.bog = Afflic_scc('bog')
        this.blind.duration = 8

        this.freeze = Afflic_cc('freeze')
        this.blind.duration = 4.5

        this.stun = Afflic_cc('stun')
        this.blind.duration = 6.5

        this.sleep = Afflic_cc('sleep')
        this.blind.duration = 6.5

        this.poison.resist    = 0
        this.burn.resist      = 0
        this.paralysis.resist = 80
        this.blind.resist     = 80
        this.bog.resist       = 80
        this.freeze.resist    = 80
        this.stun.resist      = 80
        this.sleep.resist     = 80

        this.poison.tolerance    = 5
        this.burn.tolerance      = 5
        this.paralysis.tolerance = 5
        this.blind.tolerance     = 10
        this.bog.tolerance       = 20
        this.freeze.tolerance    = 20
        this.stun.tolerance      = 20
        this.sleep.tolerance     = 20

    
    def add(this, name, atype, rate, duration, coef=0, iv=0):
        if atype == 'burning':
            atype = 'burn'
        if atype == 'para':
            atype = 'paralysis'
        if atype in ['poison','burn','paralysis']:
            return this.add_dot(name, atype, rate, coef, duration, iv)
        elif atype in ['blind','freeze','stun','sleep','bog']:
            return this.add_cc(name, atype, rate, coef, duration, iv)

    def get(this, atype):
        if atype in ['poison','burn','paralysis']:
            stack = 0
            for i in this.dot:
                if i[0] == atype and i[1].get():
                    stack += 1
            return stack
        elif atype in ['blind','freeze','stun','sleep','bog']:
            if atype in this.cc:
                return this.cc[atype].get()

    def r(this):
        return random.random()/this.luck

    def refresh_dot(this):
        tmp = []
        for i in this.dot:
            if i[1].get():
                tmp.append(i)
        this.dot = tmp

    def refresh_cc(this):
        tmp = {}
        for i in this.cc:
            if this.cc[i].get():
                tmp.append(i)
        this.cc = tmp

    def add_dot(this, name, atype, rate, coef, duration, iv):
        if not iv :
            errrrrr()
        if this.resist[atype] < 100:
            r = this.r()
            log('afflic',rate, this.resist[atype],r*100)
            if rate < this.resist[atype]:
                return 0
            if r*100 < (rate-this.resist[atype]):
                log('afflic', 'succ', name, atype)
                this.refresh_dot()
                dot = Dot('o_'+name+'_'+atype, coef, duration, iv)
                dot.on()
                this.dot.append((atype,dot))
                this.resist[atype] += 20 # 5
                return 1
        else:
            log('afflic','perfect_resist')
        return 0

    def add_cc(this, name, atype, rate, coef, duration, iv):
        if this.resist[atype] < 100:
            r = this.r()
            log('afflic',rate, this.resist[atype],r*100)
            if atype in this.cc:
                this.cc[atype].on()
                return 0
            elif rate < this.resist[atype]:
                return 0
            elif r*100 < (rate-this.resist[atype]):
                log('afflic', 'succ', name, atype)
                this.refresh_cc()
                cc = Dot('o_'+name+'_'+atype, 0, duration, duration+0.01)
                cc.on()
                this.cc[atype] = cc

                if atype == 'blind':
                    this.resist[atype] += 20 # 10
                else:  #elif atype in ['freeze','stun','sleep','bog']:
                    this.resist[atype] += 20
                return 1
        else:
            log('afflic','perfect_resist')
        return 0

    def rinit(this):
        this.resist = {}
        this.resist['poison'] = 0
        this.resist['burn'] = 0
        this.resist['freeze'] = 80
        this.resist['paralysis'] = 80
        this.resist['blind'] = 80
        this.resist['stun'] = 80
        this.resist['curse'] = 0
        this.resist['bog'] = 80
        this.resist['sleep'] = 80
        this.dot = []
        this.cc = {}
        this.luck = 1

