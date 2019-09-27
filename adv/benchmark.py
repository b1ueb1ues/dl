import cProfile

def run(proc, repeat=None):
    p = cProfile.Profile()
    if repeat:
        p.enable()
        for i in range(repeat):
            proc()
    else:
        p.enable()
        proc()
    p.print_stats()
