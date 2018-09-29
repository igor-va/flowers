from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.

# Главная страница. Просто отдаем статику

# def affiche(request):
#     return render(request, 'flowers/affiche.html')
#
#
# # Команда
# def guides(request):
#     guides = Guide.objects.all()
#     head = {
#     "title": "Наши гиды"
#     }
#     context = {"guides": guides, 'head': head}
#     return render(request, 'flowers/guides.html', context)
#
#
# def show_guide(request, nick):
#     guide = Guide.objects.get(nick=nick)
#     head = {'title': guide.name}
#     context = {"guide": guide, 'head': head}
#     return render(request, 'flowers/show_guide.html', context)
#
#
# # Отзывы
# def reviews(request):
#     reviews = Review.objects.all()
#     context = {"reviews": reviews}
#     return render(request, 'flowers/reviews.html', context)
#
#
# # Проекты
# def projects(request):
#     events = Event.objects.all()
#     head = {
#     "title": "Наши проекты"
#     }
#     context = {'events': events, "head": head}
#     return render(request, 'flowers/projects.html', context)
#
#
# def show_project(request, permalink):
#     event = Event.objects.get(permalink=permalink)
#     context = {"event":event}
#     return render(request, 'flowers/show_project.html', context)


# Все цветы
def flowers(request):
    flowers = Flower.objects.all()
    head = {
    "title": "Зелёные"
    }
    context = {'flowers': flowers, "head": head}
    return render(request, 'flowers/flowers.html', context)


# Отдельный цветок
def show_flower(request, permalink):
    flower = Flower.objects.get(permalink=permalink)
    context = {"flower": flower}
    return render(request, 'flowers/show_flower.html', context)


# Все статьи обзорно
def articles(request):
    articles = Article.objects.all()
    head = {
    "title": "Блог"
    }
    context = {'articles': articles, "head": head}
    return render(request, 'flowers/articles.html', context)


# Статья подробно
def show_article(request, nick):
    article = Article.objects.get(nick=nick)
    head = {'title': article.name}
    context = {"article": article, 'head': head}
    return render(request, 'flowers/show_article.html', context)


# Информация о нас
def about(request):
    about_all = About.objects.all()
    head = {
    "title": "О нас"
    }
    context = {'about_all': about_all, "head": head}
    return render(request, 'flowers/about.html', context)


# Отзывы
def reviews(request):
    reviews = Review.objects.all()
    head = {
    "title": "О нас"
    }
    context = {"reviews": reviews, "head": head}
    return render(request, 'flowers/feedback.html', context)
