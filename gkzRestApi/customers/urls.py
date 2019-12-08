from django.conf.urls import url
from .views import  *
urlpatterns = [
    url(r'^customers/$', customer_list),
    url(r'^customers/', customer_detail),
    url(r'^customers/age/', customer_list_age),
]