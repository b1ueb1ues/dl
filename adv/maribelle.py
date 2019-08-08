if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Maribelle

class Maribelle(adv.Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('prep','100%')

if __name__ == '__main__':
    conf = {}
   # import slot
   # conf['slots.d'] = slot.d.wind.Longlong()
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

   # conf['acl'] = """
   #     `s1, fsc
   #     `s2
   #     `s1, pin == 'prep'
   #     `fs, seq=4
   #     """

   # conf['acl'] = """
   #     `s1,seq=4
   #     `s2,seq=4
   #     `s1, pin == 'prep'
   #     `fsf, seq=4
   #     """

   # conf['acl'] = """
   #     `s1,seq=4
   #     `s2,seq=4
   #     `s1, pin == 'prep'
   #     `fsf, seq=4
   #     """


    adv_test.test(module(), conf, verbose=0)

