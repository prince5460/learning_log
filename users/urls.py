'''为应用程序users定义URL模式'''

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    url('^login/$', login, {'template_name': 'users/login.html'},
        name='login'),

    # 注销
    url('^logout/$', views.logout_view, name='logout'),

    # 注册
    url('^register/$', views.register, name='register'),
]
