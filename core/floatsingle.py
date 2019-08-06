import struct 



def f2b(a):
    a = struct.pack('f',a)
    b = struct.unpack('4s',a)
    b = b[0]
    return "%02x%02x%02x%02x"%(ord(b[3]),ord(b[2]),ord(b[1]),ord(b[0]))

def b2f(a):
    s = [0,0,0,0]
    s[0] = chr(int(a[0:2],16))
    s[1] = chr(int(a[2:4],16))
    s[2] = chr(int(a[4:6],16))
    s[3] = chr(int(a[6:8],16))
    s = "%s%s%s%s"%(s[3],s[2],s[1],s[0])
    a = struct.pack('4s',s)
    b = struct.unpack('f',a)[0]
    return b

def tofloat(a):
    return struct.unpack('f', struct.pack('f', a))[0]


if __name__ == '__main__':
    a = b2f(f2b(1.08))* 600
   #print b2f(f2b(a))
   #print b2f(f2b(1.08*600))
   #print b2f(f2b(1.08*200))

   #print '-----------'
   #print b2f(f2b(1.08))
    x = tofloat(1.08)*600
    print( tofloat(x) )
    exit()
