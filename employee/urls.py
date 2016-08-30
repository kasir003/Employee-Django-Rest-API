from django.conf.urls import url
from employee import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^employee/$',views.employee_list),
    url(r'^employee/(?P<pk>[0-9]+)/$',views.employee_detail),
    url(r'^department/$',views.employee_list),
    url(r'^department/(?P<pk>[0-9]+)/$',views.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)