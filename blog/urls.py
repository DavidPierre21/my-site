# -*- coding: utf-8 -*-
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PostViewSet, base_name='posts')

urlpatterns = router.urls
