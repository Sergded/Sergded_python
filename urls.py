from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_posts,name='posts'),
    path('create',views.create_post),
    path('get',views.get_news),
    path('<int:_id>',views.get_newpost),
    path('union',views.get_with_union),
    path('exist/<int:counter>',views.exist_object),
    path('delete/<int:_id>',views.delete_post),
    path('parse',views.parse_object)
    
]