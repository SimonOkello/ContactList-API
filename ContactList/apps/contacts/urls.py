from django.urls import path
from .views import (
    ContactAPIView,
    ContactDetailView
)

urlpatterns = [
path('contacts', ContactAPIView.as_view(), name='contacts'),
path('contacts/<str:pk>', ContactDetailView.as_view(), name='contact-detail'),
]
