# encoding: utf-8
from funcions import *
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus

def factoritza(N,e):
    llista_factors = factors_primers(N)
    if (len(llista_factors)!=2):
        return 0, 0, 0
    
    p = llista_factors[0]
    q = llista_factors[1]
    phi_n = (p-1)*(q-1)
    d = invers_modular(e,phi_n)

    return p, q, d


def test():

    max = 25
    mides = list()
    temps = list()
    for i in range(8, max):
        n, e, d, p, q = genera_claus(i)
        temps_inicial = timeit.default_timer()
        pDesc, qDesc, dDesc = factoritza(n,e)
        temps_final = timeit.default_timer()
        mides.append(i)
        temps.append(temps_final - temps_inicial)
        print("S'ha factoritzat N")
        print("Nombre p real: " + str(p))
        print("Nombre q real: "+ str(q))

        print("Nombre p trobat: "+ str(pDesc))
        print("Nombre q trobat: "+ str(qDesc))

    plt.plot(mides,temps, '-gD')
    plt.xlabel("Nombre de bits")
    plt.ylabel("Segons")
    plt.show()


test()
