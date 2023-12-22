from django.urls.conf import re_path, include
from tastypie.api import Api
from .models import UserResourse

v1_api = Api(api_name='v1')
v1_api.register(UserResourse())

urlpatterns = [
      re_path(r'^api/', include(v1_api.urls))
]

