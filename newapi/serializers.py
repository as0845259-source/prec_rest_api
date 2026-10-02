from rest_framework import serializers
from .models import NewForm

class NewFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewForm
        fields = ["id" , "title" , "description" , "published_date"]