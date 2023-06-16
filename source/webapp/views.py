from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.articles_db import ArticlesDb


def articles_list_view(request):
    articles = ArticlesDb.articles
    context = {"articles": articles, "img_path": ArticlesDb.img_path}
    # print(request.GET.getlist("test"))
    return render(request, "index.html", context)


def article_create_view(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    else:
        print(request.POST)
        new_article = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
            "author": request.POST.get("author")
        }
        ArticlesDb.articles.append(new_article)
        return HttpResponseRedirect("/")
        # return render(request, "article.html", context)
