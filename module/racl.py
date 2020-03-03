import slot
from adv import adv_test

t = 0

acls = {
    1: """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    ,2: """
        `s1
        `s2
        `s3
        """

    ,3: """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    ,4: """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """

    ,5: """
        `s1, seq=5 and cancel or fsc
        `s2
        `s3
        """
    ,6: """
        `s1
        `s2, seq=5 and cancel or fsc
        `s3
        """
    ,7: """
        `s1
        `s2
        `s3, seq=5 and cancel or fsc
        """
    ,8: """
        `s1
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """
    ,9: """
        `s1, seq=5 and cancel or fsc
        `s2
        `s3, seq=5 and cancel or fsc
        """
    ,10: """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3
        """
}

def test(adv, conf, duration=180):
    global acls
    print('dps,cname,star,ele,wt,att,cond,-,acl_idx,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-')

    for i in acls:
        conf['acl'] = acls[i]
        adv.comment = '('+str(i)+')'
        adv_test.test(adv, conf, verbose=255, mass=0, duration=duration)
