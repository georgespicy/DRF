from django.urls import path 
# from watchlist_app.api.views import movie_list, movie_datails #fuction base url
from watchlist_app.api.views import (StreamListAV, StreamDetailAV, WatchlistAV,
                                      WatchDetailAV, ReviewList, ReviewDetail)

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamListAV.as_view(), name='stream_list'),
    path('stream/<int:pk>/', StreamDetailAV.as_view(), name='stream-detail'),
    path('review/',  ReviewList.as_view(), name='review'),
    path('review/<int:pk>/',  ReviewDetail.as_view(), name='review_Detail'),
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>', movie_datails, name="movie_details")
]