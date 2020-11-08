from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import TagViewSet, UserViewSet, CommentViewSet
from library.views import LibraryViewSet, CrawlingAPIView, HistoryViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crawl/", CrawlingAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register(r'libraries', LibraryViewSet)
router.register(r'tags', TagViewSet, basename="tag")
router.register(r'users', UserViewSet, basename="user")
router.register(r'histories', HistoryViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns += router.urls
