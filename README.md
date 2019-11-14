# SPD Exercici 5 Implementació d'un criptosistema RSA

**Autor:** Francesc Xavier Bullich Parra

## Generació de les claus publica i privada

[Veure fitxer genera_claus.py](https://github.com/fxbp/spd-5/blob/master/genera_claus.py)
[Veure fitxer funcions.py](https://github.com/fxbp/spd-5/blob/master/funcions.py)

RSA és un criptosistema de claus asimetrcia. Tenim una clau privada que només la coneixerà el propietari i una clau publica que tothom pot coneixer.
La seguretat es basa en el secret de la clau privada. 

- La clau privada éstà formada per un numero N i per un número d, anomenat també exponent privat.
- La clau pública està formada per un número N i per un número e, anomenat també exponent públic.

Com veiem Tan la clau privada com la clau pública comparteixen un número N en comú. Es podria pensar que tenint N i e, es pot aconseguir la d que és l'únic ingredient que falta per aconseguir la clau privada (secreta). 
Aconseguir aquest número és molt dificil i aquesta es la clau de RSA. El nombre d, es pot aconseguir fent l'invers modular de e, aixó si, en Z/phi(N).

La seguretat de RSA rau en la complexitat de trobar aquest phi(N) (Euler). Sabent que N està format per 2 nombres primers molt grans i aplicant les propietats de l'aritmètica modular, podem trobar phi(N) = phi(primer_primer)*phi(segon_primer). La funció phi() d'un primer = primer -1. Per tant ens quedaria que phi(N)== (primer_primer - 1)*(segon_primer - 1).

Així doncs "només" s'ha de factoritzar N per trobar els 2 primers que la formen però... Això no es gens senzill. L'algoritme per factoritzar un nombre en els seus factors primers te un cost exponencial en nombre de digits. Per tant, com que tractem amb numeros primers molt gans, aquest problema esta fora de l'abast del comput actual.

