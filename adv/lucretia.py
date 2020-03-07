import adv.adv_test
from core.advbase import *

def module():
    return Lucretia

class Lucretia(Adv):
    a1 = ('energized_att', 0.20)
    a3 = ('bk',0.3)
    conf = {}
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, s=2
        `s1, s=3
        `s1, seq=5 and cancel
        """

    def s1_proc(self, e):
        self.energy.add(1, team=True)

    def s2_proc(self, e):
        self.energy.add(2)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)



'''
2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 5 0.| 2 2 3 | 5 0 | 2 2 3 |

2 1 | 2 1 3 | 2 1 | 2 1 3 |
2 3 | 5 0 0 | 2 3 | 5 0 0 |

2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 6.0 1 |

2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 1 2 | 3 2 1
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 4 6.| 0 2 3
'''
