from django.conf.urls import url, include
from .views import contact, contact_message, send_email
from home.views import index, home


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^send/', send_email, name='send_email'),
    url(r'^contact_message/$', contact_message, name='contact_message'),
]
