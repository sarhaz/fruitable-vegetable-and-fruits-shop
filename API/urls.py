from django.urls import path, include
from .views import HomeAPIView, CategoryAPIView, ProfileAPIView, ProductAPIView, ClientAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router = DefaultRouter()
router.register("product", viewset=ProductAPIView)
router.register("category", viewset=CategoryAPIView)
router.register("profile", viewset=ProfileAPIView)
router.register("client", viewset=ClientAPIView)

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
