# from django.urls import path
from django.conf.urls import url
# from django.contrib import admin

# from django.views.generic import TemplateView
# from . import views

from .views import (
    EventoList,
    EventoDetail,
    EventoCreation,
    EventoUpdate,
    EventoDelete
)

app_name = 'webapp'
urlpatterns = [

    url(r'^$', EventoList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', EventoDetail.as_view(), name='detail'),
    url(r'^nuevo$', EventoCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', EventoUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', EventoDelete.as_view(), name='delete'),

    # ex: /polls/
    # path('kk/', AboutView.as_view()),
    # path('kk/', TemplateView.as_view(template_name="about.html")),
    # path('kk/', TemplateView.as_view(template_name='index.html')),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results')

    # path('', TemplateView.as_view(template_name='index.html')),

    # url(r'^$', views.index, name='index'),
    # path(r'^$', TemplateView.as_view(template_name='index.html')),

    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
