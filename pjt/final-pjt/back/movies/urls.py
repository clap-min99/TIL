from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movies/', views.movie_all),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('beverages/', views.beverage_main),
    path('beers/', views.beer_list),
    # login, comment 관련
    path('movies/<int:movie_pk>/comments/', views.comment_list),
    path('movies/<int:movie_pk>/comments/<int:comment_id>/', views.comment_delete),
    path('movies/<int:movie_pk>/comments/<int:comment_id>/update/', views.comment_update),

    # search 관련
    path('movies/search/', views.search_movies),
    
    # Movie 관련
    path('movies/', views.movie_all, name='movie_all'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    
      # MovieGenre 관련
    path('genres/', views.movie_genre_list, name='movie_genre_list'),
    path('genres/<int:genre_id>/', views.movie_genre_detail, name='movie_genre_detail'),

    # Beverage 관련
    path('beverages/', views.beverage_main, name='beverage_main'),

    # Beer 관련
    path('beers/', views.beer_list, name='beer_list'),
    path('beers/<int:beer_id>/', views.beer_detail, name='beer_detail'),

    # Whiskey 관련
    path('whiskeys/', views.whiskey_list, name='whiskey_list'),
    path('whiskeys/<int:whiskey_id>/', views.whiskey_detail, name='whiskey_detail'),

    # Wine 관련
    path('wines/', views.wine_list, name='wine_list'),
    path('wines/<int:wine_id>/', views.wine_detail, name='wine_detail'),

    # NonAlcohol 관련
    path('nonalcohols/', views.non_alcohol_list, name='nonalcohol_list'),
    path('nonalcohols/<int:non_alcohol_id>/', views.non_alcohol_detail, name='nonalcohol_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

