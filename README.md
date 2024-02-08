# Practica_PDDL

## OBJECTIU

En l'actualitat, amb l'abundància de llibres disponibles, és difícil decidir què llegir. Desenvoluparem una eina que, basant-se en els llibres ja llegits i els desitjats per al pròxim any, elabori un pla de lectura mensual. Aquest pla recomanarà l'ordre de lectura dels llibres i intentarà equilibrar el nombre de pàgines per mes, tenint en compte les dependències entre ells.

## 1. MODELAT DEL DOMINI

### 1. 1. VARIABLES
Per a resoldre aquest problema, farem servir quatre variables, de les quals dues seran del
tipus 'libros_catalog' anomenades 'l1' i 'l2', les quals representen dos llibres diferents. Les
dues restants seran del tipus 'mes' anomenades 'm1' i 'm2', que faràn referència a dos
mesos. Tant 'libros_catalog' com 'mes' hereten de 'object'.

### 1. 2. PREDICATS
Per abordar aquest problema, hem utilitzat diferents predicats per a poder guiar el planificador a una solució:

1. quiere_leer: Predicat amb una variable del tipus 'libros_catalog' per saber quins llibres vol llegir l'usuari.
1. leido: Predicat que utilitza una variable del tipus 'libros_catalog' i ens indica si un llibre ha estat llegit.
1. mes_anterior: Predicat que opera amb dues variables de tipus 'mes'; la primera variable 'm1' representa el mes anterior a la segona variable 'm2'. Aquests tres predicats són essencials per el desenvolupament del nostre modelat del problema.
1. predecesor: Predicat que utilitza dues variables del tipus 'libros_catalog' i ens indica que el primer llibre 'l1' és predecessor del segon llibre 'l2'. Essencial per a implementar tant el nivell bàsic com l'extensió 1.
1. mes_lectura: Predicat que fa servir dues variables per assegurar-nos que els llibres es llegeixin en un mes posterior. Utilitzat també per l'extensió dos.
1. paralelos: Predicat que té dues variables del tipus 'libros_catalog', 'l1' i 'l2', les quals indiquen que aquests dos llibres són paral·lels.
1. paginas_libro: Funció amb una variable del tipus 'libros_catalog' que conté la informació sobre les pàgines de cada llibre del catàleg.
1. paginas_mes: Funció amb una variable del tipus 'mes' que conté el nombre de pàgines llegides en el mes corresponent. Utilitzada per assegurar-nos que no ens passem del límit de 800 pàgines de cada mes.

### 1. 3. ACCIONS
Per a trobar una solució al nostre problema, només hem utilitzat una acció anomenada 'leer'.

1. leer: Aquesta acció agafa tres variables. La primera d'aquestes variables és 'l1', de tipus 'libros_catalog', i aquest serà el llibre que es llegirà en cas que es donin les precondicions que explicarem seguidament. Les dues altres variables són de tipus 'mes'. El primer objecte 'mes', 'm1', indica el mes en el qual es llegirà el llibre, i el segon objecte de tipus 'mes', 'm2', s'usa per a situar el mes anterior.

* Precondicions:
  * El llibre no està llegit.
  * 'm2' és el mes anterior a 'm1'.
  * La suma de les pàgines del llibre i les pàgines llegides en el mes no supera les 800 pàgines.
  * Si el llibre té predecessor, aquest ha d'estar llegit al mes anterior 'm2'.
  * Si el llibre té un paral·lel, aquest ha d'estar llegit al mateix mes 'm1' o al mes anterior 'm2'.

* Efectes:
  * El llibre 'l1' passa a estar llegit amb el predicat 'leido'.
  * El llibre 'l1' ha estat llegit en el mes 'm1'.
  * Les pàgines del llibre 'l1' es sumen a les pàgines llegides en el mes 'm1'.


## 2. MODELAT DEL PROBLEMA

### 2. 1. OBJECTES
Per abordar l'enunciat del problema relatiu a un planificador per llegir llibres, farem ús de
dos tipus d'objectes: 'llibres_catalog' que inclou tots els llibres disponibles en un catàleg, i
'mes' que conté cada mes de l'any, ja que el planificador s'estén a tot el període anual.

### 2. 2. ESTAT INICIAL
Per iniciar la planificació dels llibres que l'usuari haurà de llegir durant l'any, és necessari
definir un estat inicial. Aquest estat inicial s'ha de configurar mitjançant els predicats
explicats anteriorment, els quals determinaran quins llibres vol llegir l'usuari i quins estan
disponibles al catàleg. A més a més, aquest estat inicial incorporarà informació sobre la
quantitat de pàgines de cada llibre del catàleg i les relacions entre els llibres, ja siguin
predecessors o paral·lels, depenent de l'extensió que estiguem considerant.

També s'especificaran els llibres que l'usuari ja ha llegit. Hem assumit que l'usuari ha llegit
aquests llibres en un any anterior. Per tant, hi ha mesos que corresponen a l'any anterior
(mesos previs) a tots els mesos del nostre any actual. Aquesta configuració garanteix que la
planificació assigni llibres als mesos de l'any actual. No tindria molt sentit que l'usuari llegís
aquests llibres declarats com a llegits en l'any que estem planificant.

Finalment, l'estat inicial també indicarà la relació temporal entre els diferents mesos,
especificant quin mes és anterior a l'altre. Aquesta informació temporal és crucial per
garantir una planificació coherent i efectiva.

#### 2. 2. 1. COM REPRESENTAR ELS PARAL·LELS
Per a la representació de paral·lels i el correcte funcionament del planificador, es pot establir
que les relacions paral·leles segueixen un conjunt de normes específiques. En primer lloc,
en la formulació del predicat 'paralelos', si existeix un llibre que es desitja llegir i aquest és
paral·lel a un altre, el llibre que es vol llegir ha de ser la segona variable en el predicat.
A més a més, per mantenir la coherència, si un llibre és la primera variable en el predicat
'paralelos' com a paral·lel d’un llibre que vol llegir, aquest llibre que vol llegir o que és
paral·lel d’un llibre que vol llegir ha de ser la segona variable en el predicat ‘paralelos’ si
aquest llibre té un paral·lel. Aquesta correspondència posicional ha de ser mantinguda de
manera successiva per a tots els llibres paral·lels.
Aquesta estructura de representació garantirà que el sistema de planificació sigui capaç de
processar correctament les relacions paral·leles entre els llibres i prendre decisions
informades basades en aquesta informació. És crucial seguir aquestes normes per
assegurar una representació coherent i l'èxit del planificador en la gestió d'aquest tipus de
dades.

### 2. 3. ESTAT FINAL
Per arribar a una solució, és necessari definir un estat final. En aquest context, l'estat final
no és excessivament complex, ja que l'objectiu fonamental del planificador és assegurar que
l'usuari hagi llegit els llibres desitjats. Per tant, l'estat final s'aconsegueix quan l'usuari ha
completat la lectura de tots els llibres que volia llegir. Aconseguim això usant un ‘forall’ el
qual mira que per a tot llibre ‘l’ del tipus ‘libros_catalog’ els quals vol llegir, ‘quiere_leer’,
siguin llegits, ‘leidos’.


## 3. GENERADOR
En el generador de jocs de prova, requerim a l'usuari que triï una llavor, ja que així podem
replicar els resultats. En el codi, es genera de manera aleatòria els llibres que es volen llegir
i els llibres que, en principi, no es volen llegir, a més del nombre de pàgines que té cada
llibre. A continuació assignem els llibres que s'han llegit i els llibres que són predecessors a
l'atzar. Després, generem els llibres paral·lels també de manera aleatòria, amb la condició
que dos llibres paral·lels no siguin ja predecessors entre ells o que no estiguin en la mateixa
cadena de predecessors. Per verificar això, hem implementat una funció recursiva
dissenyada per buscar si hi ha algun tipus de relació "predecessor" entre dos llibres.
A més a més, per representar adequadament la relació de paral·lels en el fitxer PDDL,
ordenem els paral·lels en una llista en la qual els llibres que es volen llegir estan al principi.
D'aquesta manera, quan recorrem la llista, podem crear la seqüència de paral·lels com ho
demana el 'problema.pddl'. Iterem sobre els elements de 'paralels_ordenados' i ajustem la
seqüència de llibres segons les condicions establertes pel problema. Això implica
assegurar-nos que, si el segon llibre ja està a 'libros_quiere_leer' o té un predecessor en
aquesta llista, el primer llibre també s'afegeixi a 'libros_quiere_leer'. A més, si el primer llibre
ja està a 'libros_quiere_leer' però el segon no, intercanviem les posicions dels llibres per
mantenir la coherència en la relació "paralelos".
Seguidament, assignem els mesos anteriors per a cada mes, mantenint la coherència amb
els mesos de l'any i inicialitzem també les pàgines llegides en cada mes a 0. Finalment,
generem el fitxer 'random_problem.pddl'.
