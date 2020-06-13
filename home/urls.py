from .views import index, home
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', index, name="index"),
]
