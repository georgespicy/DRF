from django.urls import path 
from watchlist_app.api.views import movie_list, movie_datails

urlpatterns = [
    path('list/', movie_list, name="movie_list"),
    path('<int:pk>', movie_datails, name="movie_details")
]