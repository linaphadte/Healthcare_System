from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Device(models.Model):
    Name= models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    Company= models.CharField(max_length=50)
    Category= models.CharField(max_length=50)
    Content= models.TextField()
    Author= models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Name

       

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

    def get_absolute_url(self):
        return reverse('Device-detail', kwargs = {'pk': self.pk})  

       
         

