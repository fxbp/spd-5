# encoding: utf-8
from funcions import *
import sys


sys.setrecursionlimit(5000)

def genera_claus(nbits):

    #Pas 3: obtenir 2 nobmres primers grans, no gaire diferents, pero no propers entre ells
    p = troba_primer(nbits)
    q = troba_primer(nbits+7)

    #print("El primer nombre primer és:")
    #print(p);
    #print("El segon nombre primer és:")
    #print(q);

    #Pas 2: Obtenir la N que forma part de la clau privada i de la publica
    n = p*q
    #print("El nombre N (p*q):")
    #print(n)

    #Pas 3: Obtenir Euler(n)
    ## Com que p i q son nombres primers la funcio de Euler(p) sera p-1 i Euler(q) = q-1
    ## S'aprofita la propietat de l'artimetica modular i podem obtnerir que:
    ###     Euler(n) = Euler(p) * Euler(q) = (p-1)*(q-1)
    phi_n = (p-1)*(q-1)
    #print("Trobem la phi(n) Euler")
    #print(phi_n)

    #Pas 4: Obtenim una e < phi(n) i coprimer amb phi(n)
    e = random.getrandbits(nbits)
    while(mcd_euclides(phi_n,e) != 1):
        e = random.getrandbits(nbits)
    #print("Exponent public: ")
    #print(e)

    #Pas 5: obtenir d fent l'invers modular de e a Z/phi(n)
    result, d = invers_modular(e,phi_n)

    #print("Exponent de desxifrat: ")
    #print(d)

    return n, e, d, p, q
