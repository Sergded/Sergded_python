from django.urls import path
from .views import New_views, WalletsView, WalletsTemp, DetailWallet, Posts_get,Posts_APIList,Posts_APIUpdate,Posts_APIDetailView,Posts_APIfilter
from . import view

urlpatterns = [
    path('get_all', view.get_posts,name='posts'),
    path('create',view.create_post),
    path('get',view.get_news),
    path('<int:_id>',view.get_newpost),
    path('union',view.get_with_union),
    path('exist/<int:counter>',view.exist_object),
    path('delete/<int:_id>',view.delete_post),
    path('parse',view.parse_object),
    path('comments/',view.create_comment, name = 'create_comment'),
    path('get_comments/<int:post_id>',view.get_comments, name = 'get_comments'),
    path('transaction/', view.Transaction.as_view(), name='transaction'),
    path('',New_views.as_view()),
    path('change_status/<int:post_id>/<slug:status>',view.change_status, name = 'change_comments'),
    path('wallet/',WalletsView.as_view()),
    path('wallets/',WalletsTemp.as_view()),
    path('wallets/<int:_id>/',DetailWallet.as_view()),
    path('posts_drf/',Posts_get.as_view()),
    path('posts_drf/<int:pk>/',Posts_get.as_view()),
    path('posts_apilist/',Posts_APIList.as_view()),
    path('posts_apilist/<int:pk>/',Posts_APIUpdate.as_view()),
    path('posts_detailview/<int:pk>/',Posts_APIDetailView.as_view()),
    path('posts_filter/',Posts_APIfilter.as_view()),
]