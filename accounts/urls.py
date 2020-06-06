from django.conf.urls import url, include
from . import url_reset
from .views import index, register, profile, logout, login, home


"""urls that manages the account pages"""
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]