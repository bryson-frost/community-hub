from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventsView.as_view(), name='events_list'),
    path('create/', views.CreateEventView.as_view(), name='create_event'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event_details')
]