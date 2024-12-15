from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Products.views import ProductViews

router = DefaultRouter()
router.register("products", ProductViews, basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
