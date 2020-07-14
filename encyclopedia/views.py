from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    markdown = Markdown()
    mark_to_html = markdown.convert(util.get_entry(name))
    return render(request, "encyclopedia/page.html", {
        "mark_to_html": mark_to_html,
        "name": name
    })