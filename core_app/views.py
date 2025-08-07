from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Category, Product
from .serializers import UserSerializer, CategorySerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()

# ✅ Anyone can view product list and detail
class ProductListAPIView(generics.ListCreateAPIView):  # Added Create functionality
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



# 🔒 Only authenticated users can view and edit their user profile
class UserListAPIView(generics.ListAPIView):  # Only viewable by authenticated users
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailAPIView(generics.RetrieveUpdateAPIView):  # Added update capability
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
