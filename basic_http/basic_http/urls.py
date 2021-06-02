from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from demo import views
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_swagger_view(title='Demo API for CISCO')

urlpatterns = [
    path('', include('demo.urls')),
    path('apidoc/', schema_view),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
