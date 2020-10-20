from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import TagViewSet, UserViewSet
from library.views import LibraryViewSet, CrawlingAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crawl/", CrawlingAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register(r'libraries', LibraryViewSet)
router.register(r'tags', TagViewSet, basename="tag")
router.register(r'users', UserViewSet, basename="user")
urlpatterns += router.urls
