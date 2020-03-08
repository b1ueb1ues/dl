import adv.adv_test
from core.advbase import *
import marth

def module():
    return Marth

class Marth(marth.Marth):
    comment = 'dodge*2 to miss s2p3 then dodge*2 back to attack'

    def s2_proc(self, e):
        if self.stance == 0:
            self.stance = 1
            Selfbuff('s21',0.1,10).on()
            self.dmg_make('s2',6.85)
        elif self.stance == 1:
            self.stance = 2
            Teambuff('s22',0.1,10).on()
            self.dmg_make('s2',6.85)
            self.conf.s2.startup += 42.0*2/60
            self.conf.s2.recovery += 42.0*2/60
        elif self.stance == 2:
            Teambuff('s23',0.1,10).on()
            Teambuff('s23s',0.3,10,'att','speed').on()
    def l_s(self, e):
        prev, index, stat = self.getprev()
        if prev == 'fs':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after fs)'%(\
                self.s1.charged, self.s1.sp, self.s2.charged, self.s2.sp, self.s3.charged, self.s3.sp, e.name) )
        elif prev[0] == 'x':
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after c%s)'%(\
                self.s1.charged, self.s1.sp, self.s2.charged, self.s2.sp, self.s3.charged, self.s3.sp, e.name, index ) )
        else:
            log('cast', e.name, 0,'<cast> %d/%d, %d/%d, %d/%d (%s after %s)'%(\
                self.s1.charged, self.s1.sp, self.s2.charged, self.s2.sp, self.s3.charged, self.s3.sp, e.name, prev ) )

        dmg_coef = self.conf[e.name+'.dmg']
        if dmg_coef :
            if e.name != 's2':
                self.dmg_make(e.name , dmg_coef)


        if 'buff' in self.conf[e.name]:
            buffarg = self.conf[e.name+'.buff']
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
        getattr(self, func)(e)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

