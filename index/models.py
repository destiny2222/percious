from django.db import models
from django.utils.text import slugify


# Create your models here.

class home(models.Model):
          CATEGORY_CHOICES = (
              ('CL', 'classes'),
              ('AP', 'About'),
              ('ST', 'Staff'),
              ('GA', 'Gallery'),
              ('SL', 'Silder'),
          ) 
          title = models.CharField(max_length=100)
          category = models.CharField(choices=CATEGORY_CHOICES, max_length=10 )
          slug = models.SlugField(default='', blank=True)
          description = models.TextField()
          image = models.FileField(default="")
          date = models.DateTimeField(default="")

          def save(self,*args,**kwargs):
              self.slug = slugify(self.title)
              super(home,self) .save(*args,**kwargs)
           
          def __str__(self):
              return self.title                        

                        