Ecritures
=========

Saisie d'une écriture
---------------------

	**Cas général**

Plaçons nous dans le menu *Comptabilité/Gestion comptable/Écritures comptables*.

    .. image:: entity_list.png

Depuis cet écran, nous avons la possibilité de visualiser les écritures
précédemment saisies ainsi que d'en ajouter de nouvelles.

Comme vous pouvez le voir dans cet écran, vous pouvez consulter les écritures
par journaux ou par état. 5 filtres d'état vous sont proposés:

* Tout: aucun filtrage n'est appliqué
* En cours (Brouillard): seulement les écritures non encore validées
* Validé: seulement les écritures déjé validées
* Lettré: seulement les écritures rapprochées ou lettrées avecd'autres
* Non lettré: seulement les écritures non encore lettrées

Ainsi que 5 journaux par défaut:
* Journal des achats
* Journal des ventes
* Journal des encaissements
* Journal des opérations diverses
* Journal de report à nouveaux

Pour ajouter une écriture, commençons d'abord par sélectionner sur quel
journal nous souhaitons réaliser notre nouvelle écriture, puis cliquons
sur le bouton *Ajouter*.

Aprés avoir précisé les dates de votre écriture, il vous faut
ajouter les différentes lignes correspondant à votre opération financiére.

Pour ajouter une ligne d'écriture, saisissez son code comptable
si vous le connaissez dans la zone d'ajout ou laissez-vous guider par
l'assistant en cliquant sur le bouton correspondant au type de compte désiré.

    .. image:: entity_add.png

L'outil ne vous permettra pas de valider votre écriture si elle est déséquilibrée.

Quand on débute en comptabilité, on a parfois du mal pour savoir si une ligne est en débit ou en crédit. Pour vous aider, un message
vous avertit si vous avez saisi un remboursement ou un avoir et un bouton vous permettez d'inverser trés facilement votre écriture si besoin.

	**Réaliser un encaissement**

Une écriture d'encaissement peut se saisir manuellement comme précédemment mais bien souvent, un réglement vient compléter un achat ou une vente effectué quelques jours plus tét.

Pour simplifier votre saisie, ré-ouvrez l'écriture d'achat ou de vente dont vous souhaitez saisir le réglement, cliquez sur le bouton "Encaissement": l'application vous propose alors une nouvelle écriture
partiellement remplie. Il ne vous reste plus qu'é préciser sur quel compte financier (caisse, banque...) vous voulez réaliser cette opération.

Une fois un encaissement validé via ce mécanisme, les deux écritures (celle d'achat ou de vente et celle d'encaissement) sont automatiquement lettrées.

	**Ecriture de report à nouveau**

Le journal de report à nouveau n'est modifiable que dans la phase d'initialisation de votre exercice.

A ce moment, vous pouvez étre amené à réaliser des opérations spécifiques comme par exemple la ventilation des bénéfices de l'année
précédente suivant plusieurs comptes.

Par contre, dans ce journal, il n'est pas possible d'ajouter des lignes d'écritures de charges ou de produits.

Lettrage d'écritures
--------------------

Comme nous l'avons évoqué dans un précédent chapitre, il est régulier
qu'un ensemble d'écritures se référent à une ou plusieurs opérations
communes. Dans ce cas, vous pouvez marquer ces écritures comme étant
liées: vous allez alors les lettrer.

Le plus souvent, le lettrage
se réalise entre écritures de valeur de tiers complémentaires: entre
une écriture d'achat (ou de vente) et son encaissement associé.

Mais, il peut arriver que nous souhaitions lettrer plus de deux
écritures. Par exemple, vous pouvez vouloir régler 3 factures d'un
fournisseur en une seule fois. Dans ce cas, comme vous ne faites qu'un
seul chéque d'un montant égal à la somme des factures, vous n'aurez
qu'une écriture d'encaissement que vous allez lettrer avec les 3
écritures d'achats. A la relecture de votre comptabilité, il deviendra
alors simple de comprendre qu'il s'agissait d'un réglement multiple.

Pour réaliser cette action, sélectionnez les lignes d'écritures que vous désirez
lier et cliquez sur le bouton "Lettrer": Si l'outil les considére comme
étant cohérentes, il réalisera le lettrage symbolisé par un numéro
commun à ces écritures en derniére colonne du journal.

Voilà les règles pour qu'un lettrage soit accepté:
 * Les lignes d'écritures doivent être des lignes de tiers (code comptable 4xx).
 * Les lignes d'écritures doivent appartenir au même exercice.
 * Les lignes d'écritures doivent être associée au même code de tiers et au même tiers
 * Les lignes d'écritures doivent d’équilibrée.

Si vous cliquez à nouveau sur ce bouton, vous avez la possibilité de supprimer
le lettrage de cette ligne d'écriture ainsi que celui des écritures associées.

Validation d'écritures
----------------------

Par défaut, une écriture est saisie au brouillard, c'est à dire dans un
état où elle reste modifiable ou supprimable.

Par contre, il est nécessaire, pour finaliser votre comptabilité, de valider cette
écriture pour entériner votre saisie.

Pour réaliser cette action, sélectionnez les écritures contrôlées et
cliquez sur le bouton "Valider": L'application affectera alors un
numéro à vos écritures ainsi que la date de validation.

Une fois validée, une écriture devient non modifiable: ce mécanisme assure le
caractére intangible et irréversible de votre comptabilité. 
Comme l'erreur est humaine, au lieu de supprimer un écriture valider, il vous faudra
créer une écriture inverse de pour l'annuler.

Cela est utile pour un responsable comptable pour préciser que cette
écriture est vérifiée par rapport au justificatif associé.
Cela sert aussi, dans le cas des écritures d'encaissements, de contrôler que
cette recette ou dépense figure bien sur un relevé de banque.

Pour clôturer un exercice, l'ensemble des écritures doivent étre validées.

Recherche d'écriture
--------------------

Depuis la liste des écritures, le bouton "Recherche" vous permet
de définir des critères de recherche d'écritures comptables.

    .. image:: entity_search.png

En cliquant sur 'Rechercher", l'outil va rechercher dans la base
toutes les écritures correspondantes à ces critères. Vous pourrez alors
imprimer cette liste ou éditer/modifier une écriture.

Import d'écritures
------------------

Depuis la liste des écritures, le bouton *Import* vous permet d'importer des écritures comptables depuis un fichier CSV.

Une fois avoir sélectionné l'exercice d'import, le journal et les information de format de votre fichier CSV,
vous serez ammené à associer les champs des écritures aux colonnes de votre documents (la première ligne de votre document doit décrire la nature de chaque colonne).

    .. image:: entity_import.png
    
Vous pouvez alors contrôler vos données avant de les validés.

Une fois l'import réalisé, l'outil vous présentera le résultat des écritures réellement importées.

**Notez que les lignes d'écritures ne seront pas importé si:**

 * Si le code comptable précisé n'existe pas dans le plan comptable de l'exercice.
 * La date n'est pas inclu dans l'exercice.
 * L'ensemble des lignes comprenant même date et même intitulé ne s'équilibre pas.

Bien que cela ne bloque pas l'import, le tiers et le code analytique seront laissé vide si ceux indiqué ne sont pas connus dans le logiciel.
 
 
