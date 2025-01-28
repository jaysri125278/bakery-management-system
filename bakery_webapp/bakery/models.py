from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='category_images/', null=True, blank=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    EGG_CHOICES = [
        ('Egg', 'Egg'),
        ('Eggless', 'Eggless'),
    ]
    
    category = models.CharField(max_length=50, null = True)
    product_name = models.CharField(max_length=200, null=True, blank=True) 
    image_url = models.ImageField(upload_to='product_images/', null=True, blank=True) 
    ingredients = models.TextField(null=True, blank=True) 
    difficulty_level = models.CharField(max_length=20, null=True, blank=True)
    time_required = models.PositiveIntegerField(null=True)
    price_inr = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    egg_or_eggless = models.CharField(max_length=10, choices=EGG_CHOICES, null=True, blank=True)
    quantity = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    reviews = models.TextField(null=True)
    ratings = models.PositiveIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.product_name or "Unnamed Product"


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='products')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
