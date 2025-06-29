"""
URL configuration for pydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# --- drf-yasg --- #
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Toss Payments API", # 프로젝트 이름
        default_version='v1', # 프로젝트 버전
        description="토스페이먼츠 연동 샘플 프로젝트 API 문서", # 설명
        terms_of_service="https://www.google.com/policies/terms/", # 관련 링크
        # contact=openapi.Contact(email="contact@snippets.local"), # 담당자 정보
        # license=openapi.License(name="BSD License"), # 라이선스 정보
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# --- drf-yasg --- #

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("payments.urls")),

    # --- drf-yasg --- #
    # Swagger UI: /swagger/
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc UI: /redoc/
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # --- drf-yasg --- #
]
