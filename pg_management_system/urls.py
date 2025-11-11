from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *

# Create a router and register your viewsets
router = DefaultRouter()    
router.register(r'pgs', PgsViewSet, basename='pgs')
router.register(r'rooms', RoomsViewSet, basename='rooms')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'tenants', TenantsViewSet, basename='tenants')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]
