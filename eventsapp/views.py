from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Event
from .forms import EventForm

# Create your views here.
class EventsView(ListView):
    model = Event
    template_name = "eventsapp/events.html"
    context_object_name = "events"

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class EventDetailView(DetailView):
    model = Event
    template_name = "eventsapp/eventdetail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "eventsapp/uploadevent.html"
    success_url = reverse_lazy('events_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)