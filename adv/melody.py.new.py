import adv_test
import adv
import slot

class new(slot.d.DragonBase):
    ele = 'wind'
    att = 127
    aura = [('sp','passive',0.35)]



def module():
    return Melody

class Melody(adv.Adv):
    comment = 'no s2'
    conf = {}
    a1 = ('cc',0.08,'hp100')
    #conf['slots.a'] = slot.a.Bellathorna()+slot.a.JotS()
    conf['slots.a'] = slot.a.Bellathorna()+slot.a.HG()
    conf['slots.d'] = new()

#    def init(this):
#        this.conf['mod'] = {'ex':('sp','passive',0.15)}



if __name__ == '__main__':
    conf = {}
 #   conf['acl'] = """
 #       `s1, fsc
 #       `fs, seq=3 and s1.charged>(s1.sp-400)
 #       """
    conf['acl'] = """
        `s1
        """
        #s3, seq=5
    adv_test.team_dps = 5000
    adv_test.test(module(), conf, verbose=-2)

