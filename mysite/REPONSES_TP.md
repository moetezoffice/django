# Reponses - Atelier 03 Django

## Question 1 - Trier les livres

La vue `livre_list` trie les livres du plus recent au plus ancien avec :

```python
Book.objects.filter(price__lt=50).order_by("-publication_date")
```

## Question 2 - Filtrer les livres

La meme vue affiche uniquement les livres dont le prix est inferieur a 50 TND grace au filtre :

```python
price__lt=50
```

## Question 3 - Afficher le nombre de livres

La vue `auteur_detail` calcule le nombre de livres avec `livres.count()` et l'envoie au template dans la variable `nombre_livres`.

## Question 4 - Ameliorer le detail d'un livre

Le template `livre_detail.html` contient un lien vers la page de detail de l'auteur :

```django
{% url 'catalogue:auteur_detail' livre.author.pk %}
```

## Question 5 - Gerer les donnees manquantes

Les templates utilisent des conditions `{% if %}` et `{% empty %}` pour afficher des messages lorsque la bibliotheque ne contient aucun livre, lorsqu'aucun auteur n'est enregistre, ou lorsqu'une categorie ou un auteur ne possede pas encore de livre.

## Verification

Les pages suivantes ont ete testees :

- `/catalogue/livres/` : `200`
- `/catalogue/auteurs/` : `200`
- `/catalogue/categories/` : `200`
- `/catalogue/livres/1/` : `200`
- `/catalogue/auteurs/1/` : `200`
- `/catalogue/livres/99999/` : `404`
