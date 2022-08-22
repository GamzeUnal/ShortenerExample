from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from app.models import Shortener
from app.serializers import ShortenerSerializer
from rest_framework.decorators import api_view

from django.urls import reverse

import random
import string
from django.utils import timezone



@api_view(['POST'])
def post_shortener(request):
    data = request.data
    
    short_data = Shortener.objects.filter(original_url=data.get('original_url')).first()
    if short_data is not None :
        return JsonResponse({'message': 'The shortener already exist'}, status=status.HTTP_404_NOT_FOUND) 

    data['shorten_url'] = shorten_hash(request, data.get('original_url'))
        
    short_serializer = ShortenerSerializer(data=data)
    if short_serializer.is_valid():
        short_serializer.save()
        return JsonResponse(short_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(short_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def shorten_hash(request, url):
    shortened_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    return shortened_url

@api_view(['GET'])
def shortener_detail(request, pk):
    try: 
        short_data = Shortener.objects.get(pk=pk) 
    except Shortener.DoesNotExist: 
        return JsonResponse({'message': 'The shortener does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    short_data.shorten_url = request.build_absolute_uri(reverse('redirect', args=[short_data.shorten_url]))
    short_serializer = ShortenerSerializer(short_data)
    return JsonResponse(short_serializer.data)

@api_view(['GET'])
def redirect(request, url):
    try: 
        short_data = Shortener.objects.filter(shorten_url=url).first() 
    except Shortener.DoesNotExist: 
        return JsonResponse({'message': 'The shortener does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if short_data.visit_count is None:
        short_data.visit_count
    else:
        short_data.visit_count += 1

    short_serializer = ShortenerSerializer(short_data, data={'visit_count': short_data.visit_count}, partial=True)
    if short_serializer.is_valid():
        updated_short = short_serializer.save() 
    
    return redirect(short_data.original_url)

