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

print(len('Anyone can use the public key to encrypt a message, but only someone with knowledge of the prime numbers can decode the message. ')*8)
print(len(str(77611523584793038313011780284441728933224468801682601746519040783724611948721555734359801982802933927936823101218786051595099849434076045037461503775360202187568048782760337059637774070499029501576669963800321519775315579696426414668247758256509272454550802582063427840911419032171452866685105778714167744515889515549358209147094584935742742190454464743635905988571958489645022278556087041672129854210749701128156557125466137226338273649759224958893961566349825219473799517769941498131237578617151203619592526088781721801617946259791393473646227967749393890524952760182325901828408512424756206614670986718985927303099)*8))
