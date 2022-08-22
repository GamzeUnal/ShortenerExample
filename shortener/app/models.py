from django.db import models

class Shortener(models.Model):
    original_url = models.CharField(max_length=200, blank=False, default='')
    shorten_url = models.CharField(max_length=200,blank=False, null=True, default='')
    visit_count = models.IntegerField(null=True)