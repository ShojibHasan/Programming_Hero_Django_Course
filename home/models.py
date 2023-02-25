from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(blank=True,null=True,max_length=200)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='product')
    price = models.IntegerField()
    is_approve = models.BooleanField(default=False)
    

class Slider(models.Model):
    title = models.CharField(blank=True,null=True,max_length=250)
    image = models.ImageField(upload_to='slider')
    date_added = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     ordering = ('-date_added')
    
    def __str__(self):
        return self.title
    