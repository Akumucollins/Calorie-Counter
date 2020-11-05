from  django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Profile', views.ProfileView)
router.register('Category', views.CategoryView)
router.register('Fooditem', views.FooditemView)
router.register('UserFooditem', views.UserFooditemView)


urlpatterns=[
path('', include(router.urls))
]    