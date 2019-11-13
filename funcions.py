import random

primes = [2,3,5,7,11, 13, 17, 19, 23, 29] # 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def potencia_modular_eficient(base, expo, p):
# p>1
# retorna (base^expo) mod
    if expo == 0:
        return 1
    elif base == 0:
        return 0
    else:
        base_to_exp_div2 = potencia_modular_eficient(base, expo//2, p)
        if expo % 2 == 0 :
            return (base_to_exp_div2 * base_to_exp_div2) % p
        else:
            return (base_to_exp_div2 * base_to_exp_div2* base) % p


def fermat_primalitat(n):

    i = 0

    while i < len(primes) and primes[i] < n:
        b = primes[i]
        result = potencia_modular_eficient(b,n-1,n)
        i+=1
        if result != 1:
            return False
    return True


def get_prime_number(nbits):
    test_number =random.getrandbits(nbits)
    while(not fermat_primalitat(test_number)):
        test_number +=1
    return test_number


def mcd_euclides(dividend , divisor):
#Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides
    residu = dividend % divisor
    while residu != 0:
        dividend = divisor
        divisor = residu
        residu = dividend % divisor

    return divisor

def bezoud(dividend , divisor):
#Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides
    residu = dividend % divisor
    q = dividend // divisor
    i = 2
    r =[1,0]
    s= [0,1]
    while residu != 0:
        r.append(q*r[i-1]+r[i-2])
        s.append(q*s[i-1]+s[i-2])
        dividend = divisor
        divisor = residu
        residu = dividend % divisor
        q = dividend // divisor
        i+=1
    sRes = s[i-1]
    rRes = r[i-1]
    if (i-1)%2==0:
        sRes *=-1
    else:
        rRes *= -1
    return divisor , rRes, sRes


def invers_modular(k,n):
#retorna k^-1 (mod n) si existeix l'invers modular de k a (mod n)
    mcd, r, s = bezoud(k,n)
    if mcd != 1:
        False, k
    else:
        return True, (r % n)
