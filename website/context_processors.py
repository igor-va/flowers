from website.slogans import slogans
import random
from django.urls import reverse


def slogans_gen(request):
    slogan = random.choice(slogans)
    return {'slogan': slogan}


def main_menu(request):
    main_menu = [
    {
    "url":"/",
    "title": "Зелёные",
    },
    {
    "url": '/blog/',
    "title": "Блог",
    },
    {
    "url": '/about/',
    "title": "О нас",
    },
    {
    "url":"/feedback/",
    "title":"Отзывы",
    },
    # {
    # "url":"/feedback/",
    # "title":"Купить",
    # },
    ]
    return {'main_menu': main_menu}
