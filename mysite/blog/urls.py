from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('r<int:year>/<int:month>/<int:day>/<post>/', views.post_detail, name='post_detail')
]