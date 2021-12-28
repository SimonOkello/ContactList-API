from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from .serializers.serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from ContactList.apps.contacts.models import Contact


class ContactAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    query_set = Contact.objects.select_related('owner').all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.select_related('owner').filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    query_set = Contact.objects.select_related('owner').all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Contact.objects.select_related('owner').filter(owner=self.request.user)
