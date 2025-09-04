Besoin d'un client
La facture doit avoir un montant supérieur à 0 lorsqu'elle n'est pas en stade brouillon,


on passe de l'état brouillon à l'état envoyé
on crée une facture en indiquant le client
Besoin d'un taux de TVA
La facture doit contenir une ligne
On ne peut modifier une facture envoyée

Il faut donner un n° à la facture au moment où on l'envoie.
Il faut donner obligatoirement un n° consécutif au précédent


La ligne de facture odit être associé à un produit, avoir une quantité, un prix unitaire
Le contenu intégral de la facture doit être stocké en base de données -> format json autorisé
On doit avoir 4 nombre stockés pour le HT et 2 pour le TTC

A chaque modification de la facture, on doit pouvoir récupérer le contenu (tout + total ttc) de la facture

Les articles ont un prix min et max

- test list
- On crée une facture sur base d'un client en statut brouillon
- On ajoute des lignes à la facture (1, n)
- 


