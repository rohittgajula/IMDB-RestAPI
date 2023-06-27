from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import (WatchList, WatchListDetail, 
                       StreamPlatform, StreamPlatformDetail, 
                       ReviewList, ReviewDetail, ReviewCreate,
                       StreamPlatformVS, UserReview, WatchList_Filtering,
                       WatchList_Searching, WatchList_Ordering)

# router = DefaultRouter()
# router.register('stream/', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchList.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetail.as_view(), name='movie-detail'),

    # this are using django-filter 
    path('movie-filter/', WatchList_Filtering.as_view(), name='movie-filter'),
    path('movie-search/', WatchList_Searching.as_view(), name='movie-search'),
    path('movie-ordering/', WatchList_Ordering.as_view(), name='movie-ordering'),

    path('stream/', StreamPlatform.as_view(), name='streamplatform'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='streamplatform-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),


    path('reviews/', UserReview.as_view(), name='user-reviews-detail'),     # fetching using parameters
    # this is without using django-filter

    path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),   # fetching using username
    # this is without using django-filter



    # path('', include(router.urls)),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
