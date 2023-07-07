from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import markdown2
from random import choice
from . import util, forms


def index(request):
    is_search = False
    search_list = []
    entries = util.list_entries()
    substr = request.GET.get('q')

    if substr in entries:
        return HttpResponseRedirect(reverse("article", kwargs={'title': substr}))

    if substr:
        is_search = True
        for entry in entries:
            if substr in entry:
                search_list.append(entry)

    context = {
        "issearch": is_search,
        "searchlist": search_list,
        "entries": entries
    }
    return render(request, "encyclopedia/index.html", context)


def add_article(request):
    if request.method == "POST":
        form = forms.CreateArticleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            markdown = form.cleaned_data['markdown']

            if name in util.list_entries():
                messages.add_message(request, messages.ERROR, "The article already exists")
            else:
                util.save_entry(name, markdown)
                return HttpResponseRedirect(reverse("article", kwargs={'title': name}))

    else:
        form = forms.CreateArticleForm()
    context = {
        'form': form
    }
    return render(request, "encyclopedia/add_article.html", context)


def view_page(request, title):
    articles = util.list_entries()

    if title not in articles:
        return render(request, "encyclopedia/404.html", status=404)

    entry = util.get_entry(title)
    context = {
        'entry': markdown2.markdown(entry),
        'title': title
    }
    return render(request, "encyclopedia/article.html", context)


def edit_article(request, title):
    if title not in util.list_entries():
        return render(request, "encyclopedia/404.html", status=404)

    if request.method == "POST":
        markdown = request.POST.get('markdown')
        util.save_entry(title, markdown)
        return HttpResponseRedirect(reverse("article", kwargs={'title': title}))

    entry = util.get_entry(title)
    context = {
        'entry': entry,
        'title': title
    }
    return render(request, "encyclopedia/edit_article.html", context)


def random_page(request):
    entries = util.list_entries()
    title = choice(entries)
    return HttpResponseRedirect(reverse("article", kwargs={'title': title}))
