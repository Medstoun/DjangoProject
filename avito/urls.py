"""avito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ads import views
from ads.views import ads as ads_view
from ads.views import category as cat_view
from ads.views import users as users_view
from ads.views import selection as selection_view
from ads.views import locations as location_views
from ads.views.service import root
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.SimpleRouter()
router.register('location', location_views.LocationViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', root),

    path('cat/', cat_view.CategoryListView.as_view()),
    path('cat/<int:pk>/', cat_view.CategoryDetailView.as_view()),
    path('cat/create/', cat_view.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', cat_view.CategoryDetailView.as_view()),
    path('cat/<int:pk>/delete/', cat_view.CategoryDetailView.as_view()),

    path('ad/', ads_view.AdListView.as_view()),
    path('ad/<int:pk>/', ads_view.AdDetailView.as_view()),
    path('ad/create/', ads_view.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', ads_view.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', ads_view.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ads_view.AdUploadImageView.as_view()),

    path('user/', users_view.UserListView.as_view()),
    path('user/<int:pk>', users_view.UserDetailView.as_view()),
    path('user/<int:pk>/update', users_view.UserUpdateView.as_view()),
    path('user/create/', users_view.UserCreateView.as_view()),


    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),

    path('selection/', selection_view.SelectionListView.as_view()),
    path('selection/<int:pk>', selection_view.SelectionDetailView.as_view()),
    path('selection/create/', selection_view.SelectionCreateView.as_view()),
    path('selection/<int:pk>/update', selection_view.SelectionUpdateView.as_view()),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
