from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groupchat/<int:groupchat_id>', views.group_chat, name='group_chat'),
    path('privatechat/<int:profile_id>', views.private_chat, name='private_chat'),
    path('privatechatid/<int:privatechat_id>', views.private_chat_by_id, name='private_chat_by_id'),
    path('login/', auth_views.LoginView.as_view(), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
