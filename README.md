# SPD Exercici 5 Implementació d'un criptosistema RSA

**Autor:** Francesc Xavier Bullich Parra

## Introducció



RSA és un criptosistema de claus asimetrica. Tenim una clau privada que només la coneixerà el propietari i una clau publica que tothom pot coneixer.
La seguretat es basa en el secret de la clau privada. 

- La clau privada éstà formada per un numero N i per un número d, anomenat també exponent privat.
- La clau pública està formada per un número N i per un número e, anomenat també exponent públic.

Com veiem Tan la clau privada com la clau pública comparteixen un número N en comú. Es podria pensar que tenint N i e, es pot aconseguir la d que és l'únic ingredient que falta per aconseguir la clau privada (secreta). 
Aconseguir aquest número és molt dificil i aquesta es la clau de RSA. El nombre d, es pot aconseguir fent l'invers modular de e, aixó si, en Z/phi(N).

La seguretat de RSA rau en la complexitat de trobar aquest phi(N) (Euler). Sabent que N està format per 2 nombres primers molt grans  podem trobar phi(N) = phi(primer_primer)*phi(segon_primer). La funció phi(n) d'un primer n és n-1. Per tant ens quedaria que phi(N)== (primer_primer - 1)*(segon_primer - 1).

Així doncs "només" s'ha de factoritzar N per trobar els 2 primers que la formen però... Això no es gens senzill. L'algoritme per factoritzar un nombre en els seus factors primers te un cost exponencial en nombre de digits. Per tant, com que tractem amb numeros primers molt gans, aquest problema esta fora de l'abast del comput actual.

## Generació de les claus pública i privada

[Veure fitxer genera_claus.py](https://github.com/fxbp/spd-5/blob/master/genera_claus.py)
[Veure fitxer funcions.py](https://github.com/fxbp/spd-5/blob/master/funcions.py)

**Obtenció del nombres primers**

Com s'ha comentat necessitem 2 nombres primers que anomenem p i q per generar les 2 claus. Aquests nombres primers han de ser prou grans com perque al intentar facotritzar el seu producte (N, que forma pert de la clau) sigui realment difícil. Per tant el primer pas és generar aquests 2 nombres primers prou grans.

Per fer-ho s'utilitza la funció 'troba_primer(nbits)'. Aquesta funció genera un nombre aleatori de nbits (passat per paràmetre) i llavors comprova si es primer amb el test de primalitat de fermat. Si no passa el test de primalitat, es provarà incrementant en 1 el nombre fins que es trobi un nombre primer (passant el test de fermat).

Es pot veure la funció 'fermat_primalitat(n)'. El que fa aquesta funció és provar amb els 10 primers nombres primers a veure si el nombre n passat per paràmetre és divisible per algun d'ells. si no ho és llavors considerem que és primer. Aquesta funció pot fallar ja que no es comproven tots els possibles divisiors, pero la probabilitat de fallar és prou petita com perque no es tingui en compte.

Així doncs genero els 2 nombres primers amb aquestes funcions. Pel que fa al nombre de bits, utilitzo per el primer nombre 1024 bits i pel segon 1031.

Ho faig així perque una de les condicions és que no siguin nombres gaire diferents en nombre de bits, pero com a primers han d'estar prou allunyats entre ells.

Un cop tenim p i q només cal multiplicar-los entre ells per obtenir la N que forma part de la clau pública i privada.

**Trobar el valor de Euler de N**

Aquest número és necessari per trobar els exponents publics i privats. Si utilitzem aquest número es molt senzill trobar e i d.

Com s'ha comentat a la introducció necessitem trobar el valor phi(N). Com sabem que N es el producte de 2 nombres primers trobar phi(N) és tan senzill com fer (p-1)*(q-1).

**Generació de l'exponent públic**

Un cop s'ha aconseguit el valor phi(N) podem passar a trobar l'exponent públic e.

Per trobar d llavors necessitem que e sigui menor a phi(n) i coprimer amb phi(n). Per tant hem de trobar un nombre que satisfaci aquesta condició. Per trobar-lo és van generan nombres aleatoris de 1024 bits. un cop generat el nombre és comprova mitjançant l'algoritme del mcd per comprovar la seva coprimalitat amb phi(n). Si no es coprimer llavors es genera un altre nombre fins que s'en troba un que ho sigui.
Pel que fa a la restricció menor que phi(n). Utilitzant nombres de 1024 bits és fàcil veure que sempre sera menor que phi(n) ja que per trobar aquest nombre s'han utilitzat nombres de com a mínim 1024 bits per tant sempre serà major.

**Generació de l'exponent privat**

Un cop aconseguits N, phi(n) i e trobar d és relativament senzill. Només serà necessari buscar l'invers modular de e a Z/phi(N). Cal observar que aquest invers segur que existeix ja que s'ha buscat un e que fos coprimer amb phi(N).


Així doncs la clau pública será (N,e) i la clau privada (N,d).



__Nota__ : S'han aplicat algunes de les recomenacions per l'eficacacia de RSA pero no totes les comentades a clase. Per exemple no es comprova que e sigui resultat d'una suma encadenada curta.


## Utilitzant RSA per xifrar i desxifrar

Ja s'ha vist com generar les claus, passem a veure com és el funcionament de xifrat i desxifrat de RSA.

[Veure fitxer criptosistema_rsa.py](https://github.com/fxbp/spd-5/blob/master/criptosistema_rsa.py)
[Veure fitxer genera_claus.py](https://github.com/fxbp/spd-5/blob/master/genera_claus.py)
[Veure fitxer funcions.py](https://github.com/fxbp/spd-5/blob/master/funcions.py)


Primer de tot s'ha d'entendre com funciona RSA. Aquest sistema es basa en fer la potencia modular del missatge utilitzant els exponets publics i privats. Si fem la potencia amb e, obtenim un missatge xifrat. Si aquest missatge xifrat el tornem a potenciar amb d, recuperem el missatge original.

**Xifrat**

Es pot veure doncs que necessitem que el missatge es transformi primer en un número per tal que podem realitzar la potencia.

Si s'observa la funcio 'codifica' de 'criptosistema_rsa.py' es pot veure com s'obté aquest nombre des del missatge original. El que es fa és lleguir el fitxer en forma de array de bytes. Un cop tenim els bytes, aplicant la funció int.from_bytes(bytes,byteorder='big') de python podem obtenir l'enter que representa el missatge. Llavors només cal realitzar la potencia modular utilitzant el missatge en forma d'enter com a base, e com a exponent i N com a Z/N.

Finalment es guarda el nou enter que representa el missatge codificat en el fitxer '<fitxer_entrada>_xifrat.txt'

**Desxifrat**

Aquest procés és similar al de xifrat. Comencem recuperant el nombre enter que representa el missatge xifrat. Llavors només hem de realitzar la potencia modular amb: enter xifrat com a base, d com a exponent i N com a Z/N.
Després obtenim l'enter desxifrat en bytes amb la funció enter.to_bytes((enter.bit_length()+7)//8,byteorder='big') de python. Finalment si volem recuperar la cadena de text es fa: str(bytes_descodificats,'utf-8') en aquest cas la codificació era utf-8.


### Aclariments

Primer de tot cal remarcar que RSA només permet codificar missatges mes curts que la mida de N. Per tant les proves realitzades només contenen cadendes d'aqeust tipus. Si es volgués xifrar un missatge més llarg s'hauria de trobar una manera de dividir el missatge en blocs de mida fixa i codificar cada un dels blocs. A més necessitariem separar el nombres resultats amb algun caràcter per saber on acaba un número xifrat i on comença el següent.

D'altra banda existeix una técnica de padding que ajuda a protegir el sistema en missatges curts. Aquesta técnica emplena el nombre xifrat fins que arriba a una mida similar a n. Aquesta tecnica de padding no s'aplica en aquesta pràctica.

### Proves

**Prova 1**

Provem el criptosistema amb un text bastant curt dins del fitxer test.txt: hola que tal

```
python .\criptosistema_rsa.py .\test.txt
S'ha codificat el missatge al fitxer: .\test.txt_xifrat.txt
S'ha descodificat el missatge xifrat a :.\test.txt_desxifrat.txt

Nombre primer p: 76095535491781983826180305558561982807560349454909743840822821486445329525711700902038928215127901570351353347263929731514485526045275942923448775311342714392497531025703107086521911214272853129722548489656729716194768298091025222491961346045699894530292281118212370878169257070895155862484515325020672567779     
Nombre primer q: 4108400452063498407569470835317322961471058183863295892587754797499426304795305574133874451300710449613919864366804491907090387029607785734538847585466228103227890781093668303725460937334275509184954049829560802664244334609594551257819662467900108282793503581294914374553252746794811312352527371190107367318327   
Modul (N): 312630932414451089963810162514980459578768768326901488557612451730138639108566256207961842165452354072782847810975878225144710575831695393758461203945500251448091683681279796147074584964490745712144288398264285541173819587746146852915983295502578105820944203707788501248294837874454169905300934486000785155798338044078235735934379056387673255519071050097645604986946785756125842503133678314149533934826466766727913233644079979825739555874318056927022876261506822082582175383401675578479587238117323051539108795571272931510986683342074894478154296309803733921482269756349704866289287269971703966887771306450364376385733
Exponent public (e): 134822070005038276339018906373028189383132225109109650727361737138302362671488579917519344977541492060786464124438596497393738018007011002798032779695211955726952010179055748592618701009991450378517712320051312541159089494800666356364427369528546007368659142955987299304106126337213506056131428253045260190187
Exponent privat (d): 256658719705730696474387083497498869563090870279885212189425619526992004554401891289052444194543882091086717009238320530255912440059149054744020113466564374213616733747022160720028465882413856580440670935539938208054544353077017895134479221471726002576301075249409216139849640379665647876999189662342604697136300185209456902608880066496877660456700860057359777512073309077074565679892015516243044276615086836601838674816882007617205783903772042592770643885757322188996660281629686077712077649427549629155622471919915455982491286040637084356734646540997495361414304018881709987679782771183356536202650890422651374859839
S'ha xifrat el contingut del fitxer a: .\test.txt_xifrat.txt
b'hola que tal\r\n'
S'ha desxifrat el text xifrat a: .\test.txt_desxifrat.txt
```

Podem trobar el nombre enter que representa el missatge xifrat a test_xifrat.txt

```
157922809626083609040984745595121881402253575346985179626050541711752911072500740445859468049150467169038396015470819263896770720051911216599889756935436338195126457257308368073751907434550108153123794277428884898728366218618516807094869078269898463202255179155556595481866520714067862642377845670926352529303787818445636250982728043750087310982752079916829772823298638700673479617539054166370950522434781882224847684686410167197175259591710251090083440607279990414678891908945894394016988240192908704888260832081835054640364596132497797340027731269533485606393643639952502637295879379786618029747622297435134398170395
```

El fitxer text_dexifrat.txt conté el missatge que s'ha desxifrat a partir del xifrat. Es pot veure el contingut a la penultima linia de l'execució.

**Prova 2**

Es prova el sistema amb un fitxer de text major. Test2.txt: A user of RSA creates and then publishes a public key based on two large prime numbers.

```
python .\criptosistema_rsa.py .\test2.txt
S'ha codificat el missatge al fitxer: .\test2.txt_xifrat.txt
S'ha descodificat el missatge xifrat a :.\test2.txt_desxifrat.txt

Nombre primer p: 32886756799096388927118887677811130551836253329533593946556551883945238718151271151798944665581284688535059441758609901765381476275818516494579339970737588185132858223502133095915616835992201319779243014820815898010679799929858209086746047460933223288806410604087005610674878158140417743636153480304947164211     
Nombre primer q: 13938778063022997934680807238169906921468323509351105127907266242661869125228022618428196582881651953407597362617072618055953835456149822426603307202242735989118365962236798619453413272663410204668064902544942675151861058904035817578609428073812051324070773413859046999608357764963742107313375480978096831459201  
Modul (N): 458401204235217171684570069437377230428189483520427314183605696433760220701117353382927364764719025108549180580613425585342391937731242845940666412828818896803745904931896391644593994552559578308226556355123434755140363155432631896408952896994360883433764046108592704675330088179644198315488246431285027787738596624193858256763480441652644070897550767788227509823206466267597283957383369874230339465001378882316157736755783326579276990713507540129068398344589083116288825560930449063183890430694205277959524670412290272174046532677774610652545756569758453551616805999692323259288282171547600947615995526727758093855411
Exponent public (e): 67986481075884925108910487941830117403405679692424304130874609590225073933481748568437884850926904644979200663651820177530798214567885115301028604692516263797045858205890884459970406167631582601929095551058450073325647067031372939160256001831098189205512165664810894106502832762547484715436972865728356926807 
Exponent privat (d): 122569762417632595368322719527178363919711634473852245734228474351419109527279233313644966354381783525689581472010204610537828250079490749310920004686180564745234744531741097014682045021256413556297500168684519784458114428255982910904417186739796248100983113045316421429384951543984579082107487029465884365375841363077974354299081545294491634958172473941194378654250367263537330757595887393986009252253410180195991029061694293306266045296980884625628272547748021234083518386233687527444622052177476576426100140419690699748307095855104796231637055291461495921433623432883578786923238416591620573112474229809886634563943
S'ha xifrat el contingut del fitxer a: .\test2.txt_xifrat.txt
b'A user of RSA creates and then publishes a public key based on two large prime numbers.\n'
S'ha desxifrat el text xifrat a: .\test2.txt_desxifrat.txt
```

odem trobar el nombre enter que representa el missatge xifrat a test2_xifrat.txt

```
157922809626083609040984745595121881402253575346985179626050541711752911072500740445859468049150467169038396015470819263896770720051911216599889756935436338195126457257308368073751907434550108153123794277428884898728366218618516807094869078269898463202255179155556595481866520714067862642377845670926352529303787818445636250982728043750087310982752079916829772823298638700673479617539054166370950522434781882224847684686410167197175259591710251090083440607279990414678891908945894394016988240192908704888260832081835054640364596132497797340027731269533485606393643639952502637295879379786618029747622297435134398170395
```


