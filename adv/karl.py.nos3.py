if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
import karl

def module():
    return Karl

class Karl(karl.Karl):
    pass



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=0)

