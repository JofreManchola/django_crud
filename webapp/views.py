from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# from django.views.generic import TemplateView

# Create your views here.

from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .models import Evento
from .serializers import UserSerializer, GroupSerializer, EventoSerializer

##########################
# Vistas para CRUD Evento
##########################
class EventoList(ListView):
    # template_name = 'webapp/index.html'
    # context_object_name = 'latest_question_list'
    model = Evento

class EventoDetail(DetailView):
    model = Evento

class EventoCreation(CreateView):
    model = Evento
    success_url = reverse_lazy('webapp:list')
    fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_fin', 'tipo']

class EventoUpdate(UpdateView):
    model = Evento
    success_url = reverse_lazy('webapp:list')
    fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_fin', 'tipo']

class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('webapp:list')
##########################
# FIN - Vistas para CRUD Evento
##########################

##########################
# Vistas para API REST
##########################
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Eventos to be viewed or edited.
    """
    queryset = Evento.objects.all()  # .order_by('-date_joined')
    serializer_class = EventoSerializer
##########################
# FIN - Vistas para API REST
##########################

# DEMO para otro tipo de vistas

# def index(request):
#     context = {
#         'days': Evento.objects.all(),
#     }
#     return render(request, 'webapp/index.html', context)
