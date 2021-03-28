from rest_framework import routers

from drugs.views import DrugViewSet

router = routers.DefaultRouter()

router.register('drugs',DrugViewSet )

urlpatterns = []
urlpatterns += router.urls