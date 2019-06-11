import adv_test
import adv
from adv import *
import marth

def module():
    return Marth

class Marth(marth.Marth):
    comment = 'dodge*2 to miss s2p3 then dodge*2 back to attack'

    def s2_proc(this, e):
        if this.stance == 0:
            this.stance = 1
            Selfbuff('s21',0.1,10).on()
            this.dmg_make('s2',6.85)
        elif this.stance == 1:
            this.stance = 2
            Teambuff('s22',0.1,10).on()
            this.dmg_make('s2',6.85)
            this.conf.s2.startup += 42.0*2/60
            this.conf.s2.recovery += 42.0*2/60
        elif this.stance == 2:
            Teambuff('s23',0.1,10).on()
            Teambuff('s23s',0.3,10,'att','speed').on()
    def l_s(this, e):
        prev, index, stat = this.getprev()
        if prev == 'fs':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after fs)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name) )
        elif prev[0] == 'x':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after c%s)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, index ) )
        else:
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after %s)'%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, prev ) )

        dmg_coef = this.conf[e.name+'.dmg']
        if dmg_coef :
            if e.name != 's2':
                this.dmg_make(e.name , dmg_coef)


        if 'buff' in this.conf[e.name]:
            buffarg = this.conf[e.name+'.buff']
            wide = buffarg[0]
            buffarg = buffarg[1:]
            if wide == 'team':
                Teambuff(e.name, *buffarg).on()
            elif wide == 'self':
                Selfbuff(e.name, *buffarg).on()
            elif wide == 'debuff':
                Debuff(e.name, *buffarg).on()
            else:
                Buff(e.name, *buffarg).on()

        func = e.name + '_proc'
        getattr(this, func)(e)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=-2)

