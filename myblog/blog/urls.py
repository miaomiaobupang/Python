from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('index',views.index),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/<int:article_id>/',views.article_edit,name='article_edit'),
    path('add',views.add_page,name='add_page'),
    path('create',views.create_page,name='add_action'),
]
