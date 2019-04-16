import adv_test
import adv


def module():
    return Kleimann

class Kleimann(adv.Adv):
    a1 = ('fs',0.4)
    a3 = ('s',0.2)

if __name__ == '__main__':
    conf = {}

    # s2 after s1 will increase kleimann's damage a little since his s2's sp is too strange

    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel 
        `s2, s=1
        """

    if 1:
        conf['acl'] = """
            `s1, seq=5 and cancel or pin='fs'
            `s2, seq=5 and cancel or pin='fs'
            `fs, seq=5
            """
    # add 1 fs can increase lots of damage 
    if 0:
        conf['acl'] = """
            `fs, seq=5 and s1.charged >= 2500
            `s1, seq=5 and cancel or pin='fs'
            `s2, seq=5 and cancel or pin='fs'
            """
    if 0:  # add some sphaste also work!
        conf.update( {
            "mod.sp":('sp','ex',0.11)
            } )
        conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel 
            """

    adv_test.test(module(), conf, verbose=0)
    import core.log

