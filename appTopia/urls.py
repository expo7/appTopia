import imp
from django.urls import path, include
from django.contrib.auth.models import User
import lines

urlpatterns = [
    # path('', include('api.urls')),
    path('', include('lines.urls'))

    # path('api-auth/', include('rest_framework.urls', namespace='api_auth'))
]
