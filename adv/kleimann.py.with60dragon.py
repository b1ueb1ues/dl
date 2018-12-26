import adv_test
import adv
import adv.kleimann
import wep.wand


def module():
    return Kleimann2

class Kleimann2(adv.kleimann.Kleimann):
    pass


if __name__ == '__main__':
    conf = {}
    conf.update( {
        "mod_d" : ('att' , 'ex' , 0.6) ,
        } )


    # s2 after s1 will increase kleimann's damage a little since his s2's sp is too strange
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s2, s=1
        """

    # add little fs to increace very little damage


    if 1:
        conf['acl'] = """
            `fs, seq=5 and s1.charged >= 2500
            `s1, seq=5 and cancel or pin='fs'
            `s2, seq=5 and cancel or pin='fs'
            """
    if 0:
        conf.update( {
            "mod_sp":('sp','ex',0.11)
            } )
        conf['acl'] = """
            `s1, seq=5 and cancel or pin='fs'
            `s2, seq=5 and cancel
            """

    #if 1:
    #    conf['acl'] = """
    #        `s1, seq=5 and cancel or pin='fs'
    #        `fs, seq=5 and this.s2.charged < 7090 and this.s2.charged >= 6400
    #        `s2, seq=5 and cancel or pin='fs' or sp='fs' 
    #        """


    adv_test.test(module(), conf, verbose=0)
    import core.log

