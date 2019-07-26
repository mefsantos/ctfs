#! /usr/bin/python2.7

from Crypto.Util.number import long_to_bytes

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def find_invpowAlt(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    low = 10 ** (len(str(x)) / n)
    high = low * 10

    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1



N = 374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811
e = 3
ciphertext = 2205316413931134031046440767620541984801091216351222789180573437837873413848819848972069088625959518346568495824756225842751786440791759449675594790690830246158935538568387091288002447511390259320746890980769089692036188995150522856413797

# since ciphertext = m**e (mod n)
# m = pow(ciphertext, 1/e) :: the 'eth' root of ciphertext
# since e is really small (3) we can find the cube root on ciphertext 
# and retrieve the clear text

plaintext = find_invpowAlt(ciphertext, e)

print long_to_bytes(plaintext)