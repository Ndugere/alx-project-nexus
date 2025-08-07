from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Product

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_picture_url',
        ]
        read_only_fields = ['id']
        

class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'image',
            'created_by',
        ]
        read_only_fields = ['id', 'created_by']




class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    created_by = UserSerializer(read_only=True) 

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'slug',
            'image',
            'category',
            'category_id',
            'created_by', 
        ]
        read_only_fields = ['id', 'slug', 'created_by']
