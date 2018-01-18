"""定义learning_logs的URL模式"""
from django.conf.urls import url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    url('^$', views.index, name='index'),

    # 显示所有主题
    url('^topics/$', views.topics, name='topics'),

    # 详情页面
    url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 添加新主题
    url('^new_topic/$', views.new_topic, name='new_topic'),

    # 添加新条目
    url('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 编辑条目
    url('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')

]
