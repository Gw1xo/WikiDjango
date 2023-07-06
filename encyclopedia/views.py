from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        	"entries": entries,
            "form": form
    }
    return render(request, "encyclopedia/index.html", context)

def add_article(request):
    form = forms.CreateArticleForm()
    context = {
        'form': form
    }
    return render(request, "encyclopedia/add_article")

def view_page(request, title):
    articles = util.list_entries()

    if title in articles:
        entry = util.get_entry(title)

        context = {
            'entry': entry,
            'title': title,
            'form': form
        }

        return render(request, "encyclopedia/article.html", context)
    else:
        return render(request, "encyclopedia/404.html", status=404)
