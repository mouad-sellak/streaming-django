from django import views
from django.urls import path
from rest_framework import routers
from django.contrib.auth import views as auth_views
from .views import *
# from .views import index, VideoViewFilm, VideoViewMusic,VideoViewSerie,VideoViewDocumentaire, VideoDetail, VideoSearch 
# from serializers import MusicViewSerializer

# router = routers.DefaultRouter()
# router.register('music', MusicView)
# router.register('film', FilmView)
# router.register('episode', EpisodeView)
# router.register('documantaire', DocumentaireView)
# router.register('serie', SerieView)

urlpatterns = [
    path('', homepage, name='home'),
    path('home/', home, name='homepage'),
    path('bar/', testbar, name='testbar'),
    path('add-favourite/', favorite, name='favourite'),
    path('favouriteList/', FavouriteVideo.as_view(), name='list_favourite'),

    path('add-watch-later/', watch_later, name='watch_later'),
    path('watchLaterList/', watchLaterVideo.as_view(), name='list_watchLater'),
    
    path('submit_review_film/<int:id>/', submit_review_film, name='submit_review_film'),
    path('submit_review_music/<int:id>/', submit_review_music, name='submit_review_music'),
    path('submit_review_episode/<int:id>/', submit_review_episode, name='submit_review_episode'),
    path('submit_review_documentaire/<int:id>/', submit_review_documentaire, name='submit_review_documentaire'),

    
    # path('register/', register, name='register'),
    path('inscription/', inscription, name='inscription'),
    path('profile/', profile_detail, name='profil_detail'),
    path('update_profile/',update_profile , name='update_user_profile'),
    path('update/',UserUpdateView.as_view() , name='profil_update'),



    # path('password/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name='change_password'),
    path('password/', change_password, name='change_password'),
    path('password_success/', password_success, name='password_success'),
    
    path('search/', search_video, name='search_video'),
    path('listvideo/', listvideo, name='video_list'),
    path('listmusic/', listmusic, name='music_list'),
    path('listfilm/', listfilm, name='film_list'),
    path('listdocumentaire/', listdocumentaire, name='documentaire_list'),
    path('listepisode/', listepisode, name='episode_list'),
    path('listserie/', listserie, name='serie_list'),

    path('musicdetail/<int:pk>', musicdetail, name='music_detail'),
    path('filmdetail/<int:pk>', filmdetail, name='film_detail'),
    path('documentairedetail/<int:pk>', documentairedetail, name='documentaire_detail'),
    path('episodedetail/<int:pk>', episodedetail, name='episode_detail'),
    path('seriedetail/<int:pk>', seriedetail, name='serie_detail'),

    # path('views/', CountView, name='Number_Visite'),

    path('music/<int:pk>', showmusic, name='music'),
    path('film/<int:pk>/', showfilm, name='film'),
    path('episode/<int:pk>', showepisode, name='episode'),
    path('documentaire/<int:pk>', showdocumentaire, name='documentaire'),
    
    path('film/commentaire/<int:pk>/', commentFilm, name='comment_film'),
    path('music/commentaire/<int:pk>/', commentMusic, name='comment_music'),
    path('episode/commentaire/<int:pk>/', commentEpisode, name='comment_episode'),
    path('documentaire/commentaire/<int:pk>/',commentDocumentaire, name='comment_documentaire'),

    
     ]

    
    # path('', index, name='index'),
    # path('film/<int:id>', FilmView.as_view, name='film_view'),
    # path('music/<int:id>', MusicView.as_view, name='video_view_music'),
    # path('serie/<int:id>', EpisodeView.as_view, name='episode_View'),
    # path('documentaire/<int:Documentaire_id>', DocumentaireView.as_view, name='documentaire_View'),
    # path('search/<str:query>', SerieView.as_view, name='video_search'),


# urlpatterns = [
#     path('', index, name='index'),
#     #path('Film /detail/<int:pk>', views.VideoView.as_view(), name='video'),
#     path('film/<int:id>', VideoViewFilm, name='video_view_film'),
#     path('music/<int:id>', VideoViewMusic, name='video_view_music'),
#     path('serie/<int:id>', VideoViewSerie, name='video_view_serie'),
#     path('documentaire/<int:Documentaire_id>', VideoViewDocumentaire, name='video_view_documentaire'),
#     path('search/<str:query>', VideoSearch.as_view, name='video_search'),
#     path('<int:pk>', VideoDetail.as_view(), name='video_detail'),

# ]
