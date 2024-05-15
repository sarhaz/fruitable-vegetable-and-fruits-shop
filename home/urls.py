from django.urls import path
from .views import HomeView, ShopView, ShopDetailView, CartView, CheckoutView, ProfileView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('shop/shop_detail/cart/', CartView.as_view(), name='cart'),
    path('shop/shop_detail/cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/shop_detail/<int:id>', ShopDetailView.as_view(), name='shop_detail'),
]
