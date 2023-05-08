from django.urls import path
from .views import playing, update_playing

urlpatterns = [
    path('playing/', playing, name='playing'),
    path('update/', update_playing, name='update'),
]
