from django.db import models

# Custom imports : - 

from django.urls import reverse

# Models : 

class Category(models.Model):
    
    category_name = models.CharField(max_length=50, unique=True)
    
    # Slug is the url of Category
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField(max_length=300, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories' , blank=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        
    
    def __str__(self):
        return self.category_name