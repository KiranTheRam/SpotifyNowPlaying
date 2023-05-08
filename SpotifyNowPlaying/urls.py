from django.urls import path, include

urlpatterns = [
    path('', include('now_playing.urls')),
]
