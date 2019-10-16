from rest_framework import serializers
from . models import volunteers

class volunteersSerializer(serializers.ModelSerializer):

    class Meta:
        model = volunteers
        fields ='__all__'