from rest_framework import routers

from stores.views import StoreViewSet

router = routers.DefaultRouter()

router.register('stores', StoreViewSet)

urlpatterns = []
urlpatterns += router.urls
