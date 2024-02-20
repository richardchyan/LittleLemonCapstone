from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from restaurant import views as restaurant_views
from LittleLemonAPI import views as LittleLemonAPI_views 

router = DefaultRouter()
# Using a router.registers route, the first argument would be part of the url path, then you would just include the "router" as a variable and use the urls property on it 
router.register(r'tables', restaurant_views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api/', include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

