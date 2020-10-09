from django.contrib import admin
from django.urls import path, include
from wallet.urls import urlpatterns as api_urls
from rest_framework_swagger.views import get_swagger_view

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_swagger_view(title='BBDD2 Smart Wallet API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('', schema_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
