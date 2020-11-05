from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    id  = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    first_name = models.CharField(max_length=20,default='collins')
    last_name = models.CharField(max_length=20,default='akumu')
    status = models.TextField(max_length=100)
    email = models.CharField(max_length=200,null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2,default='80')
    height = models.DecimalField(max_digits=6, decimal_places=2,default='120')
    birth_field = models.DateField(default='2005-12-24') 
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Category(models.Model):
    options=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks'),
    )
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,choices=options)
    
    def __str__(self):
        return self.name
    
class Fooditem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fats = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    protein = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    calorie = models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
class UserFooditem(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ManyToManyField(Profile,blank=True,related_name='user_diet')
    fooditem = models.ManyToManyField(Fooditem)    
    
    def __str__(self):
        return str(self.profile)