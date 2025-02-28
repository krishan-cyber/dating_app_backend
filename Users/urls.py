"""
PATCH /user/photo/add/ → Uploads a new profile picture.
DELETE /user/photo/delete/ → Deletes a profile picture.
PATCH /user/verify-account/ → Runs an ML model for verification."""

from django.urls import path
from .views import send_otp,verify_otp,CreateUserProfileView,delete_account,ShowUserDetails,UpdateUserDetails,UserGoOffline

urlpatterns = [
    path('auth/send-otp/',send_otp,name='send_otp'),
    path('auth/verify-otp/',verify_otp,name='verify_otp'),
    path('auth/signup/', CreateUserProfileView.as_view(), name='create-profile'),
    path('account/delete/',delete_account,name='delete-account'),
    path('profile/<str:number>/',ShowUserDetails.as_view(),name='show-user-detail'),
    path('profile/update/<str:number>/',UpdateUserDetails.as_view(),name='update-user-detail'),
    path('go_offline/<str:number>/',UserGoOffline.as_view(),name='go-offline'),

]
