from django.db import models
from django.shortcuts import reverse
import uuid
class shortURL(models.Model):
    key = models.CharField(max_length = 8, primary_key=True, unique = True, blank=True, editable=False, default = str(uuid.uuid4().hex[:7])[:6])
    url = models.TextField(unique=True)

    def get_url(self):
        return reverse('redirect',args=[self.key])
    
    
    
# Create your models here.
