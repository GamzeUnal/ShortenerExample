from rest_framework import serializers 
from app.models import Shortener
 
 
class ShortenerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Shortener
        fields = ('id',
                  'original_url',
                  'shorten_url',
                  'visit_count')