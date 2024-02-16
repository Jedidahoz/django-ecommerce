from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    
    path('shop/', views.shop, name = 'shop'),
    path('shop/product/<pid>/', views.product, name = 'product'),
    path('category/<cid>/', views.categoryProduct, name = 'categoryProduct'),
    path('tag/<slug:tag_slug>/', views.tagList, name = 'tagList'),

    path('vendors/', views.vendors, name = 'vendors'),
    path('vendors/<vid>', views.vendorView, name = 'vendorView'),

    path('compare/', views.compare, name = 'compare'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('wishlist/', views.wishlist, name = 'wishlist'),
    path('cart/', views.cart, name = 'cart'),
    path('order-tracking/', views.orderTracking, name = 'orderTracking'),

    path('user/', include('userauths.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)