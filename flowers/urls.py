from django.conf.urls import url

from . import views
from pages import views as pages
from flowers.models import *
from pprint import pprint

try:
    flowers_list=Flower.objects.values_list('permalink', flat=True)
    flowers_list=list(flowers_list)
    flowers_list='|'.join(flowers_list)

except:
    flowers_list='test'


# Это основное приложение проекта

urlpatterns = [
        # Цветы
        url(r'^$', views.flowers, name='flowers'),
        # Перехватываем только соответствующие тэгам проектов
        url(r'^(?P<permalink>' + flowers_list + ')/', views.show_flower, name='show_flower'),
        # Все записи блога
        url(r'blog/$', views.articles, name='articles'),
        # Отдельная статья
        url(r'blog/(?P<nick>\w+)/$', views.show_article, name='show_article'),
        # О нас
        url(r'about/$', views.about, name='about'),
        # Фидбэк
        url(r'feedback/$', views.reviews, name='index'),

        # # Проекты
        # url(r'projects/$', events.projects, name='projects'),
        # # Перехватываем только соответствующие тэгам проектов
        # url(r'^(?P<permalink>' + events_list + ')/', events.show_project, name='show_project'),
        # # Команда
        # url(r'team/$', events.guides, name='guides'),
        # # Отдельный человек
        # url(r'team/(?P<nick>\w+)/$', events.show_guide, name='show_guide'),
        # # Фидбэк
        # url(r'feedback/$', events.reviews, name='index'),
        # # Ну и контакты
        # url(r'contacts/$', pages.page, {"page": "contacts"}),
        ]
