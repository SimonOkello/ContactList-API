from rest_framework import serializers
from ContactList.apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id',
                  'country_code',
                  'first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'is_favorite']
        write_only_fields = ['owner']
