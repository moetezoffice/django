from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Category


def livre_list(request):
    livres = Book.objects.filter(price__lt=50).order_by("-publication_date")
    context = {
        "livres": livres,
        "titre_page": "Catalogue des livres",
    }
    return render(request, "catalogue/livre_list.html", context)


def livre_detail(request, pk):
    livre = get_object_or_404(Book, pk=pk)
    context = {"livre": livre}
    return render(request, "catalogue/livre_detail.html", context)


def auteur_list(request):
    auteurs = Author.objects.all().order_by("last_name", "first_name")
    context = {"auteurs": auteurs}
    return render(request, "catalogue/auteur_list.html", context)


def auteur_detail(request, pk):
    auteur = get_object_or_404(Author, pk=pk)
    livres = auteur.books.all().order_by("title")
    context = {
        "auteur": auteur,
        "livres": livres,
        "nombre_livres": livres.count(),
    }
    return render(request, "catalogue/auteur_detail.html", context)


def categorie_list(request):
    categories = Category.objects.all().order_by("name")
    context = {"categories": categories}
    return render(request, "catalogue/categorie_list.html", context)
