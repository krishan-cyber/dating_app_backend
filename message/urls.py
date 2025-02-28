from rest_framework.urls import urlpatterns,path
from .views import message_handle,message_user
urlpatterns=[
    path('send/',message_handle.as_view(),name='send_message'),
    path('chats/<int:pk>/',message_handle.as_view(),name='load_chats'),
    path('chats/all/',message_user.as_view(),name='all-chats'),
]