`vannerie.py` est un script permettant d'exporter un csv contenant une quantité non-exhaustive
de motifs de vannerie sur fond plat en se focalisant sur le montant de départ de chaque brin.

## Usage

```
./vannerie.py output.csv
```

## Concept et explications

Lorsqu'on fabrique un fond de panier plat, ou n'importe quelle structure plate, il est souvent
intéressant d'avoir un motif répétitif dans la position de départ des brins.
Souvent, un motif efficace est découvert empiriquement et ne fonctionnera que sur une situation donnée
avec des variables difficiles à maîtriser (nombre d'enfonçures, longueur des brins).

L'idée est donc de modéliser un maximum de motifs pour faciliter le choix du vannier.

Pour chaque motif, on se base sur les variables suivantes :

### Le nombre d'enfonçures

La dimension de la pièce va déterminer le nombre d'enfonçures. On choisit souvent un nombre pair,
mais ce n'est pas obligatoire.

Ici, on ne compte pas les rives (les montants à l'extrémité) dans le compte.
Elles sont numérotées comme suit (exemple avec 6 enfonçures) :

```
 I | | | | | | I

(0)1 2 3 4 5 6(7)

| : Enfonçure
I : Rive
```

### La longueur des brins

Les brins sont mesurés en intervalle entre les enfonçures. On ne parle pas ici de la longueur jusqu'à la 
cime mais la longueur utile que l'on veut utiliser dans la pièce. On va pouvoir également choisir une longueur 
plus faible dans le cas où on veut obtenir un autre motif.

Pour simplifier le calcul, la longueur supplémentaire utilisée lors d'un tour autour d'une rive est ignoré.

La longueur des brins est toujours paire, puisqu'on commence et on finit un brin derrière une enfonçure.

### Numéro d'enfonçure de départ

L'enfonçure à laquelle on démarre pour le premier brin.

### Résultats

Pour chacune de ces 3 données de départ, on obtient un motif avec les enfonçures de départ de chaque brin, 
jusqu'à ce que le motif revienne à son point de départ. On a également une colonne avec le nombre de bris par 
cycle, pour faciliter le tri.
