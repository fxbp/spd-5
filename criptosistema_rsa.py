from genera_claus import genera_claus
from funcions import *
import sys


nbits = 1024
fitxer_xifrat = "_xifrat.txt"
fitxer_desxifrat = "_desxifrat.txt"

def obtenir_bytes(enter):
    return enter.to_bytes((enter.bit_length()+7)//8,byteorder='big')

def codifica(fitxer_original, fitxer_codificat, e, n):
    bytes = open(fitxer_original, 'rb').read()
    enter_pla =int.from_bytes(bytes,byteorder='big')
    ## codifiquem l'enter amb la clau publica que s'ha obtingut
    codificat = potencia_modular_eficient(enter_pla,e,n)
    open(fitxer_codificat, 'w').write(str(codificat))

def descodifica(fitxer_codificat, fitxer_resultat, d, n):
    codificat = int(open(fitxer_codificat, 'r').read())
    # Per descodificar agafem l'enter codificat i li aplicem la potencaicio modular amb la clau privada
    descodificat = potencia_modular_eficient(codificat, d, n)
    #obtenim el text descodicifat a partir de l'enter obtingut
    bytes_descodificats = obtenir_bytes(descodificat)
    print(bytes_descodificats)
    missatge_descodificat = str(bytes_descodificats,'utf-8')
    open(fitxer_resultat, 'w').write(missatge_descodificat)

def genera_noves_claus():
    n, e, d, p, q = genera_claus(nbits)
    print("S'ha codificat el missatge al fitxer: " +fitxer+ fitxer_xifrat)
    print("S'ha descodificat el missatge xifrat a :"+ fitxer + fitxer_desxifrat)
    print()
    print("Nombre primer p: " + str(p))
    print("Nombre primer q: " + str(q))
    print("Modul (N): "+ str(n))
    print("Exponent public (e): "+ str(e))
    print("Exponent privat (d): "+ str(d))

    return n, e, d, p, q


fitxer = sys.argv[1]

## Es generen les claus publica i privada
n, e, d, p, q = genera_noves_claus()
fitxer_codificat=fitxer+fitxer_xifrat
fitxer_descodificat = fitxer+fitxer_desxifrat
codifica(fitxer, fitxer_codificat,e,n)
print("S'ha xifrat el contingut del fitxer a: "+ fitxer_codificat)
descodifica(fitxer_codificat,fitxer_descodificat,d,n)
print("S'ha desxifrat el text xifrat a: "+ fitxer_descodificat)
