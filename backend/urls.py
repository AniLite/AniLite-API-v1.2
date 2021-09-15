from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view('AniLite API')
API_TITLE = 'AniLite API'
API_DESCRIPTION = 'An API that steals data from another API and provides it to the frontend xD'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('anime.api.urls'), name='api-urls'),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('schema/', schema_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
