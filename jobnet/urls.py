from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import os
from pathlib import Path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from accounts.api.views import CustomTokenObtainPairView
from jobnet import settings
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home , name='home'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/company/', include('company.api.urls')),
    path('api/resume/', include('resume.api.urls')),
    path('api/address/', include('address.api.urls')),
    path('api/job/', include('job.api.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # --------- swagger --------- #
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # --------- swagger --------- #
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
