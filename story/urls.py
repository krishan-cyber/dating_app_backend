from rest_framework.urls import urlpatterns,path
from .views import stories,like_story
urlpatterns=[
    path('post/',stories.as_view(),name='post_story'),
    path('stories/',stories.as_view(),name='get_story'),
    path('like/<int:story_id>/',like_story.as_view(),name='like_story'),
]