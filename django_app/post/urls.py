from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from post import views

app_name = 'css'  # reverse 하는 모든 namespace URL에 앱네임을 지정해줘야 한다.(redirect할때 주의) 단 render함수는 제외
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),

]