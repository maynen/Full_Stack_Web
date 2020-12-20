from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randrange

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entry = util.get_entry(title)
    if( entry is not None):
        entry = markdown2.markdown(entry)
        context = {
            "entry":entry,
            "title":title
        }
        return render(request, "encyclopedia/page.html", context)

def random(request):
    entries = util.list_entries()
    index = randrange(len(entries))
    return redirect('page', title=entries[index])

def search(request):
    term = request.GET.get('q')
    entries = util.search_entry(term)

    return render(request, "encyclopedia/results.html", {
        "entries": entries
    })

def edit(request, title):
    # Get the entry to be edited
    context = {
        "title":title,
        "content":util.get_entry(title=title)
    }
    return render(request, "encyclopedia/create.html", context)
    
def create(request):
    return render(request, "encyclopedia/create.html")

def create_post(request):
    # Get the inputs
    title = request.GET.get('title')
    content = request.GET.get('content')

    # Create the new entry
    util.save_entry(title=title, content=content)

    return redirect('index')
