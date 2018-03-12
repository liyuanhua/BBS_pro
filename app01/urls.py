from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^sub_comment/', views.sub_comment)
]
