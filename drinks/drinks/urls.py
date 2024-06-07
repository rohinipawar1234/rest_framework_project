"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from drinks_app import views
from drinks_app.views import RegisterUserView
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drinks_app.views import CustomLoginAPI, CustomLogoutView
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Drinks Details Django Rest Framework Project",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("drinks/", views.drink_list),
    path("drinks/<int:pk>/", views.drinks_details),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("api-auth/", include("rest_framework.urls")),  # provide login button
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("__debug__/", include("debug_toolbar.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("login/", CustomLoginAPI.as_view(), name="login-user"),
    path("logout/", CustomLogoutView.as_view(), name="custom_logout_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
