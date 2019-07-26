
def ceiling(a):
    b = int(a)
    if b == a:
        return b
    else:
        return b + 1

print ceiling(1.0)
print ceiling(1.000000001)
