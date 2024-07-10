from django.urls import include, path
from images.api import views
from rest_framework.routers import DefaultRouter

app_name = 'images'

router = DefaultRouter()
router.register('images', views.ImagesViewSet)

urlpatterns = [
    # path('images/', views.ImageListView.as_view(), name='images_list'),
    # path('images/<pk>/', views.ImageDetailView.as_view(), name='image_detail'),
    path('', include(router.urls))
]
