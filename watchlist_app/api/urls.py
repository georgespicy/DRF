from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_datails #fuction base url
from watchlist_app.api.views import StreamList, WatchDetailAV, WatchlistAV, ReviewCreate, ReviewList, ReviewDetail



router = DefaultRouter()
router.register('stream', StreamList, basename='streamlist')


urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view, name='movie-detail'),

    path('', include(router.urls)),

    # path('stream/', StreamListAV.as_view(), name='stream_list'),
    # path('stream/<int:pk>/', StreamDetailAV.as_view(), name='stream-detail'),

    # path('review/',  ReviewList.as_view(), name='review'),
    # path('review/<int:pk>/',  ReviewDetail.as_view(), name='review_Detail'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-list'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>', movie_datails, name="movie_details")
]