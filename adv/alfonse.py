import adv_test
import adv
from adv import *
from core.log import *

def module():
    return Alfonse

class Alfonse(adv.Adv):
    a1 = ('lo',0.50*10.0/15.0)
    a3 = ('sp',0.08)

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

        if dmg_coef :
            this.dmg_make(e.name , dmg_coef)


        func = e.name + '_proc'
        getattr(this, func)(e)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2,fsc
        `s3,fsc 
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

