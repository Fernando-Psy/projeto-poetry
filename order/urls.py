from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.viewsets.order_viewset import OrderViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
