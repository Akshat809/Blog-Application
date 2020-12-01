from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('article/<int:pk>', views.article,name = 'get_article'),
    path('author/<int:pk>', views.author,name = 'get_author'),
    path('article',views.create_article,name = 'create_article'),
    path('author',views.create_author,name = 'create_author'),
    path('',views.home,name = 'home'),
    path('view_authors',views.view_authors,name = 'view_authors')
]
