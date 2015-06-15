from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested import routers

from .views import HomeView
from .viewSets import BookViewSet, FavouriteViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'libros', BookViewSet)
router.register(r'favoritos', FavouriteViewSet)

comments_router = routers.NestedSimpleRouter(router, r'libros', lookup='book')
comments_router.register(r'comentarios', CommentViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^api/', include(comments_router.urls)),
    url(r'^$', HomeView.as_view(), name="home"),
]
