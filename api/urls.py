from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, obtain_token,
                    send_confirmation_code)

router = DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='Review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='Comment'
)

auth_patterns = [
    path('email/', send_confirmation_code),
    path('token/', obtain_token)
]

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(auth_patterns))
]
