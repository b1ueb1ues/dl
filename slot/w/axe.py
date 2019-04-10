from slot import *
import slot

class axe5b1(WeaponBase):
    ele = ['flame','light','shadow']
    wt = 'axe'
    att = 567
    s3 = Conf() 
    s3.buff     = ['self',0.5, 20, 'crit','dmg']
    s3.sp       = 4711       
    s3.startup  = 0.10+0.15  
    s3.recovery = 1.05-0.15  

class axe5b2(WeaponBase):
    ele = ['water','wind']
    att = 584
    wt = 'axe'
    s3 = Conf()
    s3.dmg      = 4.18*3   
    s3.sp       = 9025     
    s3.startup  = 0.1      
    s3.recovery = 2.25     

class axev(WeaponBase):
    pass

flame  = axe5b1
light  = axe5b1
shadow = axe5b1

water  = axe5b2
wind   = axe5b2

