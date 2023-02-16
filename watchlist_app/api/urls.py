from django.urls import path 
# from watchlist_app.api.views import movie_list, movie_datails #fuction base url
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-datail'),
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>', movie_datails, name="movie_details")
]