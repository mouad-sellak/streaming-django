
from multiprocessing import context
from pdb import post_mortem
import profile
from pyexpat import model
from urllib import request
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from video.models import Film, Video, Music,Documentaire,Serie, Episode, Favorite
from django.views.generic import ListView , CreateView,DetailView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from video.serializers import VideoSerializer, FilmSerializer, MusicSerializer, EpisodeSerializer, SerieSerializer, DocumentaireSerializer 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
# from video.forms import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView 
from rest_framework import status
from django.forms import *
from django.shortcuts import redirect
from django.urls import reverse

def favorite(request):
    if request.method=='POST':
        # try:
        if request.POST['type'] == 'music':
            music_favorit = Music.objects.get(pk=request.POST['id'])
            videoFavorit = Favorite.objects.filter(music=music_favorit, user=request.user, type=request.POST['type'])
            if not len(videoFavorit):
                videoFavorit = Favorite(music=music_favorit, user=request.user, type=request.POST['type'])
                videoFavorit.save()
            # HttpResponse
            return render(request, 'streaming/index.html', {"videoFavorit":videoFavorit})

        elif request.POST['type'] == 'film':
            film_favorit = Film.objects.get(pk=request.POST['id'])
            videoFavorit = Favorite.objects.filter(film=film_favorit, user=request.user, type=request.POST['type']) 
            if not len(videoFavorit):
                videoFavorit = Favorite(film=film_favorit, user=request.user, type=request.POST['type']) 
                videoFavorit.save()
            return render(request, 'streaming/index.html', {"videoFavorit":videoFavorit})
        elif request.POST['type'] == 'episode':
            episode_favorit = Episode.objects.get(pk=request.POST['id'])
            videoFavorit = Favorite.objects.filter(episode=episode_favorit, user=request.user, type=request.POST['type']) 
            if not len(videoFavorit):
                videoFavorit = Favorite(episode=episode_favorit, user=request.user, type=request.POST['type']) 
                videoFavorit.save()
            return render(request, 'streaming/index.html', {"videoFavorit":videoFavorit})

        elif request.POST['type'] == 'documentaire':
            documentaire_favorit = Documentaire.objects.get(pk=request.POST['id'])
            videoFavorit = Favorite.objects.filter(documentaire=documentaire_favorit, user=request.user, type=request.POST['type']) 
            if not len(videoFavorit):
                videoFavorit = Favorite(documentaire=documentaire_favorit, user=request.user, type=request.POST['type']) 
                videoFavorit.save()
                
            return render(request, 'streaming/index.html', {"videoFavorit":videoFavorit})
        else :
            return render(request, 'streaming/index.html')
        # except Exception as e:
        #     print(e)
        #     return render(request,'streaming/favorite.html')
    messages.success(request, 'add to favorite is succusfully')
    return render(request, 'streaming/index.html',{'messages':messages})


class FavouriteVideo(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'streaming/favorite_list.html'

    


def watch_later(request):
    if request.method=='POST':
        # try:
        if request.POST['type'] == 'music':
            music_watch_later = Music.objects.get(pk=request.POST['id'])
            videoWatchLater = WatchLater.objects.filter(music=music_watch_later, user=request.user, type=request.POST['type']) 
            if not len(videoWatchLater):
                videoWatchLater = WatchLater(music=music_watch_later, user=request.user, type=request.POST['type']) 
                videoWatchLater.save()
            # if(videoWatchLater.objects.filter(music=music_watch_later).count()==0): 
            return render(request, 'streaming/index.html', {"videoWatchLater":videoWatchLater})
        elif request.POST['type'] == 'film':
            film_watch_later = Film.objects.get(pk=request.POST['id'])
            videoWatchLater = WatchLater.objects.filter(film=film_watch_later, user=request.user, type=request.POST['type']) 
            if not len(videoWatchLater):
                videoWatchLater = WatchLater(film=film_watch_later, user=request.user, type=request.POST['type']) 
                videoWatchLater.save()
            return render(request, 'streaming/index.html', {"videoWatchLater":videoWatchLater})
        elif request.POST['type'] == 'episode':
            episode_watch_later = Episode.objects.get(pk=request.POST['id'])
            videoWatchLater = WatchLater.objects.filter(episode=episode_watch_later, user=request.user, type=request.POST['type']) 
            if not len(videoWatchLater):
                videoWatchLater = WatchLater(episode=episode_watch_later, user=request.user, type=request.POST['type']) 
                videoWatchLater.save()
            return render(request, 'streaming/index.html', {"videoWatchLater":videoWatchLater})
        elif request.POST['type'] == 'documentaire':
            documentaire_watch_later = Documentaire.objects.get(pk=request.POST['id'])
            videoWatchLater = WatchLater.objects.filter(documentaire=documentaire_watch_later, user=request.user, type=request.POST['type']) 
            if not len(videoWatchLater):    
                videoWatchLater = WatchLater(documentaire=documentaire_watch_later, user=request.user, type=request.POST['type']) 
                videoWatchLater.save()
            return render(request, 'streaming/index.html', {"videoWatchLater":videoWatchLater})
        else :
            return render(request, 'streaming/index.html',)
        # except Exception as e:
        #     print(e)
        #     return render(request,'streaming/favorite.html')
        
    return render(request, 'streaming/index.html')

class watchLaterVideo(LoginRequiredMixin, ListView):
    model = WatchLater
    template_name = 'streaming/watchLater_list.html'



    
    



    # def get_queryset(self):
    #     qs= Favorite.objects.filter(user=self.request.user)

    #     return qs

    # def get_context_data(self, **kwargs):
        
    #     return super().get_context_data(**kwargs)




def testbar(request):
    return render(request, 'streaming/bar.html')


class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email']
# Create your views here

# class VideoView(generics.ListAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ('title')

class MusicView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('title')

class FilmView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('title')

class EpisodeView(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('title')

class DocumentaireView(generics.ListAPIView):
    queryset = Documentaire.objects.all()
    serializer_class = DocumentaireSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('title')


def search_video(request):
    if request.method == 'GET': # this will be GET now
        video_name =  request.GET.get('q') # do some research what it does 
        musics = Music.objects.filter(Q(title__icontains=video_name) | Q(chanteur__icontains=video_name))
        # serie = Serie.objects.filter(Q(acteur__icontains=video_name))
        episodes = Episode.objects.filter(Q(title__icontains=video_name) | Q(serie__acteur__icontains=video_name))
        films = Film.objects.filter(title__icontains=video_name)
        # episode.serie__acteur
        documentaires = Documentaire.objects.filter(title__icontains=video_name)
        # context = {
        #     "musics": musics,
        #     "episodes": episodes,
        #     "films": films,
        # }
        
        videos = [q for q in musics] + [q for q in episodes] + [q for q in films] + [q for q in documentaires] 
        print(videos)
        return render(request,"streaming/search.html",{"videos":videos})
    else:
        return render(request,"streaming/search.html")



# def search(request):        
#     if request.method == 'GET': # this will be GET now      
#         book_name =  request.GET.get('search') # do some research what it does       
#         try:
#             status = Add_prod.objects.filter(bookname__icontains=book_name) # filter returns a list so you might consider skip except part
#         return render(request,"search.html",{"books":status})
#     else:
#         return render(request,"search.html",{})

@api_view(['GET'])
def listvideo(request):
    results = Video.objects.all()
    serialize = VideoSerializer(results, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def listmusic(request):
    results = Music.objects.all()
    serialize = MusicSerializer(results, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def listfilm(request):
    results = Film.objects.all()
    serialize = FilmSerializer(results, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def listdocumentaire(request):
    results = Documentaire.objects.all()
    serialize = DocumentaireSerializer(results, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def listepisode(request):
    results = Episode.objects.all()
    serialize = EpisodeSerializer(results, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def listserie(request):
    results = Serie.objects.all()
    serialize = SerieSerializer(results, many=True)
    return Response(serialize.data)

@login_required
def homepage(request):
    return render(request, 'streaming/index.html')

def home(request):
    return render(request, 'streaming/home.html')



@api_view(['GET'])
def musicdetail(request, pk):
    results = Music.objects.get(pk=pk)
    serialize = MusicSerializer(results, many=False)
    return Response(serialize.data)

@api_view(['GET'])
def filmdetail(request, pk):
    results = Film.objects.get(pk=pk)
    serialize = FilmSerializer(results, many=False)
    return Response(serialize.data)


@api_view(['GET'])
def documentairedetail(request, pk):
    results = Documentaire.objects.get(pk=pk)
    serialize = DocumentaireSerializer(results, many=False)
    return Response(serialize.data)


@api_view(['GET'])
def episodedetail(request, pk):
    results = Episode.objects.get(pk=pk)
    serialize = EpisodeSerializer(results, many=False)
    return Response(serialize.data)

@api_view(['GET'])
def seriedetail(request, pk):
    results = Serie.objects.get(pk=pk)
    serialize = SerieSerializer(results, many=False)
    return Response(serialize.data)



def showmusic(request, pk):
    music = Music.objects.get(pk=pk)
    if request.method == 'GET' :
        music.view_count+=1
        music.save()
        print('nombre de vue')
        print(music.view_count)
        music_views = music.view_count
        print('test nombre de vue')
        print(music_views)
    if request.user.is_authenticated:
        user = request.user
        # like
        if request.method == 'POST' :
            if music.likes.filter(id=user.id).exists():
                print('Try to dislike')
                music.likes.remove(user)
            else :
                print('Try to like')
                music.likes.add(user)
        user_like_this_video = music.likes.filter(id=user.id).exists()
 
        # dislike
        if request.method == 'POST' :
            if music.dislike.filter(id=user.id).exists():
                print('Try to dislike')
                music.dislike.remove(user)
            else :
                print('Try to like')
                music.dislike.add(user)
        user_dislike_this_video = music.dislike.filter(id=user.id).exists()
    
    
    form = CommentForm()
    comments = music.commentsMusic.all()
    reviews = music.reviewMusic.all()

    return render(request, 'streaming/show_music.html', {'music': music, 'form':form, 'comments': comments, 'user_like_this_video':user_like_this_video,'user_dislike_this_video':user_dislike_this_video, 'reviews':reviews, 'music_views':music_views})

def commentMusic(request, pk):
    music = Music.objects.get(pk=pk)
    comments = music.commentsMusic.all()
    new_comment = None
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        print('-------------')
        print(form.errors)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.music = music
            new_comment.save()
    else:
        form = CommentForm()

    return redirect("music", pk=music.pk)



def submit_review_music(request, id):
    music = Music.objects.get(id=id)
    if request.method =='POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, music__id=id)
            data={}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data=data, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, 'thank you, your rating has been updated.')
            return redirect(reverse("music",kwargs={"pk":music.id}))
        except ReviewRating.DoesNotExist:
            data = {}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data)
            
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.music_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'thank you, your rating has been submited')
                return redirect(reverse("music",kwargs={"pk":music.id}))
                
    return redirect(reverse("music",kwargs={"pk":music.id}))
    



def showfilm(request, pk):
    film = Film.objects.get(pk=pk)
    genre = film.genre
    related_films = Film.objects.filter(genre=genre).exclude(pk=pk)
    if request.method == 'GET' :
        film.view_count+=1
        film.save()
        print('nombre de vue')
        print(film.view_count)
        film_views = film.view_count
        print('test nombre de vue')
        print(film_views)
    if request.user.is_authenticated:
        user = request.user
        # like
        if request.method == 'POST' :
            if film.likes.filter(id=user.id).exists():
                print('Try to dislike')
                film.likes.remove(user)
            else :
                print('Try to like')
                film.likes.add(user)
        user_like_this_video = film.likes.filter(id=user.id).exists()
 
        # dislike
        if request.method == 'POST' :
            if film.dislike.filter(id=user.id).exists():
                print('Try to dislike')
                film.dislike.remove(user)
            else :
                print('Try to like')
                film.dislike.add(user)
        user_dislike_this_video = film.dislike.filter(id=user.id).exists()
    
    
    form = CommentForm()
    comments = film.commentsFilm.all()
    reviews = film.reviewFilm.all()

    # film_views = ViewCount.objects.filter(film=film).count()

    return render(request, 'streaming/show_film.html', {'film': film,'related_films': related_films, 'form':form, 'comments': comments, 'user_like_this_video':user_like_this_video,'user_dislike_this_video':user_dislike_this_video,'reviews':reviews})
    # 'film_views':film_views



def commentFilm(request, pk):
    film = Film.objects.get(pk=pk)
    comments = film.commentsFilm.all()
    new_comment = None
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        print('-------------')
        print(form.errors)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.film = film
            new_comment.save()
    else:
        form = CommentForm()

    return redirect("film", pk=film.pk)
    #return render(request, 'streaming/show_film.html', {'film': film,
    #'form': form,'comments': comments,'new_comment': new_comment, })



def submit_review_film(request, id):
    film = Film.objects.get(id=id)
    if request.method =='POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, film__id=id)
            data={}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data=data, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, 'thank you, your rating has been updated.')
            return redirect(reverse("film",kwargs={"pk":film.id}))
        except ReviewRating.DoesNotExist:
            data = {}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.film_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'thank you, your rating has been submited')
                return redirect(reverse("film",kwargs={"pk":film.id}))
    return redirect(reverse("film",kwargs={"pk":film.id}))




# def CountView(request, pk ):
#     film = Film.objects.get(pk=pk)
#     ip=request.META['REMOTE_ADDR']
#     if not ViewCount.object.filter(film=film, session=request.session.session_key):
#         view = ViewCount(film=film, ip_address=ip, session=request.session.session_key)
#         view.save()
#     film_views = ViewCount.objects.filter(film=film).count()
    
#     context = {
#         "view_count":film_views,
#     }
    
#     return redirect("film", pk=film.pk,)




def showepisode(request, pk):
    episode = Episode.objects.get(pk=pk)
    serie_id=episode.serie
    related_episodes = Episode.objects.filter(serie_id=serie_id).exclude(pk=pk)
    if request.method == 'GET' :
        episode.view_count+=1
        episode.save()
        print('nombre de vue')
        print(episode.view_count)
        episode_views = episode.view_count
        print('test nombre de vue')
        print(episode_views)
    if request.user.is_authenticated:
        user = request.user
        # like
        if request.method == 'POST' :
            if episode.likes.filter(id=user.id).exists():
                print('Try to dislike')
                episode.likes.remove(user)
            else :
                print('Try to like')
                episode.likes.add(user)
        user_like_this_video = episode.likes.filter(id=user.id).exists()
 
        # dislike
        if request.method == 'POST' :
            if episode.dislike.filter(id=user.id).exists():
                print('Try to dislike')
                episode.dislike.remove(user)
            else :
                print('Try to like')
                episode.dislike.add(user)
        user_dislike_this_video = episode.dislike.filter(id=user.id).exists()
    
    
    form = CommentForm()
    comments = episode.commentsEpisode.all()
    reviews = episode.reviewEpisode.all()

    return render(request, 'streaming/show_episode.html',{'episode': episode,'related_episodes': related_episodes,'form':form, 'comments': comments, 'user_like_this_video':user_like_this_video,'user_dislike_this_video':user_dislike_this_video, 'reviews':reviews,'episode_views':episode_views})

def commentEpisode(request, pk):
    episode = Episode.objects.get(pk=pk)
    comments = episode.commentsEpisode.all()
    new_comment = None
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        print('-------------')
        print(form.errors)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.episode = episode
            new_comment.save()
    else:
        form = CommentForm()

    return redirect("episode", pk=episode.pk)



def submit_review_episode(request, id):
    episode = Episode.objects.get(id=id)
    if request.method =='POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, episode__id=id)
            data={}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data=data, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, 'thank you, your rating has been updated.')
            return redirect(reverse("music",kwargs={"pk":episode.id}))
        except ReviewRating.DoesNotExist:
            data = {}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data)
            
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.episode_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'thank you, your rating has been submited')
                return redirect(reverse("episode",kwargs={"pk":episode.id}))
                
    return redirect(reverse("episode",kwargs={"pk":episode.id}))
    



def showdocumentaire(request, pk):
    documentaire = Documentaire.objects.get(pk=pk)
    if request.method == 'GET' :
        documentaire.view_count+=1
        documentaire.save()
        print('nombre de vue')
        print(documentaire.view_count)
        documentaire_views = documentaire.view_count
        print('test nombre de vue')
        print(documentaire_views)
    if request.user.is_authenticated:
        user = request.user
        # like
        if request.method == 'POST' :
            if documentaire.likes.filter(id=user.id).exists():
                print('Try to dislike')
                documentaire.likes.remove(user)
            else :
                print('Try to like')
                documentaire.likes.add(user)
        user_like_this_video = documentaire.likes.filter(id=user.id).exists()
 
        # dislike
        if request.method == 'POST' :
            if documentaire.dislike.filter(id=user.id).exists():
                print('Try to dislike')
                documentaire.dislike.remove(user)
            else :
                print('Try to like')
                documentaire.dislike.add(user)
        user_dislike_this_video = documentaire.dislike.filter(id=user.id).exists()
    
    
    form = CommentForm()
    comments = documentaire.commentsDocumentaire.all()
    reviews = documentaire.reviewDocumentaire.all()

    return render(request, 'streaming/show_documentaire.html', {'documentaire': documentaire,'form':form, 'comments': comments, 'user_like_this_video':user_like_this_video,'user_dislike_this_video':user_dislike_this_video, 'reviews':reviews,'documentaire_views':documentaire_views})

def commentDocumentaire(request, pk):
    documentaire = Documentaire.objects.get(pk=pk)
    comments = documentaire.commentsDocumentaire.all()
    new_comment = None
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        print('-------------')
        print(form.errors)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.documentaire = documentaire
            new_comment.save()
    else:
        form = CommentForm()

    return redirect("documentaire", pk=documentaire.pk)



def submit_review_documentaire(request, id):
    documentaire = Documentaire.objects.get(id=id)
    if request.method =='POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, documentaire__id=id)
            data={}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data=data, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, 'thank you, your rating has been updated.')
            return redirect(reverse("documentaire",kwargs={"pk":documentaire.id}))
        except ReviewRating.DoesNotExist:
            data = {}
            data['user']=request.user
            data['rating'] = request.POST['rating']
            data['review'] = request.POST['review']
            form = RateForm(data)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.documentaire_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'thank you, your rating has been submited')
                return redirect(reverse("documentaire",kwargs={"pk":documentaire.id}))
                
    return redirect(reverse("documentaire",kwargs={"pk":documentaire.id}))
    





def profile_detail(request):
    # model = profile
    if request.user.is_authenticated==False:
        return render(request, 'account/login.html')
    user=request.user
    # context = {
    #     # "user": User.objects.get(id = request.session['user_id']),
        
    #     "profile":Profile.objects.get(user=request.user)
    # }
    return render(request, "account/profile.html")
  



class UserUpdateView(UpdateView,LoginRequiredMixin):
    model = User
    template_name = 'account/profile_update.html'
    form_class = UserForm

    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
    def get_success_url(self):
        return "/profile"

# ------------test extend user------------
@login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        # user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/user_profile_update.html', {
        # 'user_form': user_form,
        'profile_form': profile_form
    })
    # ------------fin test -----------

def inscription(request):
    if request.method == 'POST':
        form_extend_user = ProfileForm(request.POST)
        if form_extend_user.is_valid():
            
            form_extend_user.save()
    else :
        form_extend_user = ProfileForm()
    context = {'form_extend_user':form_extend_user}
    return render(request, 'account/register.html',context)



def change_password(request):
    if request.method=='GET':
        # import pdb;pdb.set_trace()
        form_pass=PasswordChangingForm()
        return render(request, 'account/password_change.html',{'form':form_pass})
    if request.method=='POST':
        if request.user.is_authenticated==False:
            return render(request, 'account/login.html')
        user=request.user
        form_pass=PasswordChangingForm()
        if not user.check_password(request.POST['old_password']):
            return render(request,'account/password_change.html',{'form':form_pass,'error':'Ancien mot de passe incorrect'})
        if request.POST['new_password1']!=request.POST['new_password2']:
            return render(request,'account/password_change.html',{'form':form_pass,'error':'Mot de passes non similaire'})
        user.set_password(request.POST['new_password1'])
        user.save()
        return render(request,'streaming/index.html')




def password_success(request):
    return render(request, 'account/password_success.html')

    
 






# def index(request):
#     films = Film.objects.all()
#     musics = Music.objects.all()
#     documentaires = Documentaire.objects.all()
#     series = Serie.objects.all() 
    
#     #context = {'films':films, 'musics':musics,'documentaires':documentaires}
#     return render(request, 'streaming/index.html',{'films':films, 'musics':musics,
#     'documentaires':documentaires,'series':series, })


# class MusicView(viewsets.ModelViewSet):

#     queryset = Music.objects.all()
#     SerieSerializer_class = MusicSerializer

#     def get(self, request, pk):
#         music = Music.objects.get(pk=pk)
#         serializer = 

#         return response


# class FilmView(viewsets.ModelViewSet):

#     queryset = Film.objects.all()
#     SerieSerializer_class = FilmSerializer


# class EpisodeView(viewsets.ModelViewSet):

#     queryset = Episode.objects.all()
#     SerieSerializer_class = EpisodeSerializer


# class DocumentaireView(viewsets.ModelViewSet):

#     queryset = Documentaire.objects.all()
#     SerieSerializer_class = DocumentaireSerializer


# class SerieView(viewsets.ModelViewSet):

#     queryset = Serie.objects.all()
#     SerieSerializer_class = SerieSerializer




# class MusicView(APIView):
#     def get(self,request,pk):
#         song = Music.objects.get(pk=pk)


# class VideoSearch(ListView):
#     model = Music
#     template_name = 'streaming/index.html'
#     paginate_by = 1

#     def get_queryset(self):
#         query = self.request.Get('q')
#         if query:
#             object_list = self.model.filter(title=query)
#             print(query)
#             print(object_list)
#             return object_list

#         else : 
#             object_list = self.model.objects.none()
#         return object_list




# def index(request):
#     films = Film.objects.all()
#     musics = Music.objects.all()
#     documentaires = Documentaire.objects.all()
#     series = Serie.objects.all() 
    
#     #context = {'films':films, 'musics':musics,'documentaires':documentaires}
#     return render(request, 'streaming/index.html',{'films':films, 'musics':musics,
#     'documentaires':documentaires,'series':series, })

# def VideoViewFilm(request,id,*args, **kwargs):
#     f = Film.objects.get(id=id)

#     # basic vues count
#     f.number_of_vues += 1
#     f.save()

#     # TODO: Count number of seconds; 
#     ## request.recuperer_adress_machine 
#     return render(request, 'streaming/show_film.html',{'f':f})

    

# def VideoViewMusic(request,id,*args, **kwargs):
#     m = Music.objects.get(id=id)
#     return render(request, 'streaming/show_music.html',{'m':m})

# def VideoViewSerie(request,id,*args, **kwargs):
#     s = Serie.objects.get(id=id)
#     return render(request, 'streaming/video.html', {'s':s})

# def VideoViewDocumentaire(request,Documentaire_id,*args, **kwargs):
#     d = Documentaire.objects.get(id=Documentaire_id)
#     return render(request, 'streaming/video.html',{'d':d})


# class VideoList(ListView):
#     model = Video


# class VideoDetail(ListView):
#     model = Video
#     template='streaming/detail.html'
    
