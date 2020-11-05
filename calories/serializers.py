from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name='calories:profile-detail',
                                              source='profile',read_only=True)
    class Meta:
        model = User
        fields = ('id', 'url','username', 'first_name', 'last_name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ('id','url','user','image', 'first_name', 'last_name', 'status','email', 'weight', 'height','birth_field')
    
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

              
class FooditemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Fooditem
        fields =   ('id','url','category', 'carbohydrate', 'fats', 'protein', 'calorie','quantity')

        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields = ('id','url','name')

        
class UserFooditemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= UserFooditem
        fields =  ('id','url','profile', 'fooditem')
                      
