from calendar import c
from distutils.command.upload import upload
from ipaddress import ip_address
from tkinter import CASCADE
from turtle import update
from polymorphic.models import PolymorphicModel
from django.core.validators import MaxValueValidator 
from django.db.models import IntegerField
# from typing import Type
from django.db import models
import uuid
from django.contrib.auth.models import User 

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  


from django.db.models.signals import post_save
from django.dispatch import receiver
#?--------------------------------------
#? adding a custom queryset for video :
#?--------------------------------------
# from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.db.models.query import QuerySet

# class SubclassingQuerySet(QuerySet):
#     def __getitem__(self, k):
#         result = super(SubclassingQuerySet, self).__getitem__(k)
#         if isinstance(result, models.Model) :
#             return result.as_leaf_class()
#         else :
#             return result
#     def __iter__(self):
#         for item in super(SubclassingQuerySet, self).__iter__():
#             yield item.as_leaf_class()

# class VideoManager(models.Manager):
#     def get_query_set(self):
#         return SubclassingQuerySet(self.model)

# class Video (models.Model) :
#     name = models.TextField(max_length=100)
#     content_type = models.ForeignKey(ContentType,editable=False,null=True)
#     
    
#     def save(self, *args, **kwargs):
#         if(not self.content_type):
#             self.content_type = ContentType.objects.get_for_model(self.__class__)
#             super(Video, self).save(*args, **kwargs)

#     def as_leaf_class(self):
#         content_type = self.content_type
#         model = content_type.model_class()
#         if (model == Video):
#             return self
#         return model.objects.get(id=self.id)
    
# class Salad (Video) :
#     too_leafy = models.BooleanField(default=False)
#     

# from polymorphic.models import PolymorphicModel

# class Project(PolymorphicModel):
#     topic = models.CharField(max_length=30)

# class ArtProject(Project):
#     artist = models.CharField(max_length=30)

# class ResearchProject(Project):
#     supervisor = models.CharField(max_length=30)

#?-----------------------------------------------------


class Profile(models.Model):
    villes = [ 
        ('Nouakchott ','Nouakchott '),
        ('Trarza  ','Trarza  '),
        ('Hodh_Chargui','Hodh_Chargui'),
        ('Gorgol ','Gorgol '),
        ('Assaba ','Assaba '),
        ('Brakna  ','Brakna  '),
        ('Hodh_Gharbi  ','Hodh_Gharbi '),
        ('Guidimaka  ','Guidimaka  '),
        ('Nouadhibou ','Nouadhibou '),
        ('Adrar ','Adrar '),
        ('Zouerate','Zouerate'),
        ('Inchiri ','Inchiri '),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Telephone = models.CharField(max_length=500, blank=True)
    ville = models.CharField(choices=villes,max_length=100, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# Create your models here.
class Video(models.Model):
    Type_video = [ 
        ('serie','Serie'),
        ('documentaire','Documentaire'),
        ('film','Film'),
        ('music','Music'),
    ]

    title = models.CharField(max_length=100,  null=True)
    description = models.TextField(max_length=100, null=True, default='', blank=True)
    date_creation = models.DateField(null=True)
    date_ajout = models.DateField(null=True)
    date_modification = models.DateField(null=True)
    type = models.CharField(choices=Type_video,max_length=100, default='serie', null=True)
    duree = models.CharField(max_length=100, null=True) 
    Chaine = models.CharField(max_length=100, null=True)
    resolution = models.CharField(max_length=100, null=True)
    Url = models.URLField(max_length=100, null=True)
    taille = models.CharField(max_length=100, null=True)
    vdeo = models.FileField(upload_to = "video/%y", null=True, verbose_name="video")
    image = models.ImageField(upload_to = "image/%y", null=True, verbose_name="Image")
    uuid=models.UUIDField(default = uuid.uuid4, editable=False)
    likes = models.ManyToManyField(User, blank=True,related_name='%(class)s_like')
    dislike = models.ManyToManyField(User,blank=True,related_name='%(class)s_dislike')
    view_count = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0)
    
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.title 

    # def save(self, *args, **kwargs):
    #     if(not self.content_type):
    #         self.content_type = ContentType.objects.get_for_model(self.__class__)
    #         super(Video, self).save(*args, **kwargs)

    # def as_leaf_class(self):
    #     content_type = self.content_type
    #     model = content_type.model_class()
    #     if (model == Video):
    #         return self
    #     return model.objects.get(id=self.id)



class Film(Video):
    
    Genre = [ 
    ('action','Action'),
    ('comedie','comedie'),
    ('histoire','Histoire'),
    ('drame','Drame'),
    ('aventure','aventure'),
    ]
    #video=models.ForeignKey(Video,null=True,on_delete=callable)
    realisateur = models.CharField(max_length=50, null=True)
    producteur = models.CharField(max_length=50, null=True)
    acteur = models.CharField(max_length=50, null=True)
    genre = models.CharField(choices=Genre, max_length=200, null=True)


class Serie(models.Model):
    title = models.CharField(max_length=100, null=True)
    Genre = [ 
    ('action','Action'),
    ('comedie','comedie'),
    ('histoire','Histoire'),
    ('drame','Drame'),
    ('aventure','aventure'),
    ]
    # video=models.ForeignKey(Video,null=True,on_delete=callable)
    realisateur = models.CharField(max_length=50, null=True)
    producteur = models.CharField(max_length=50, null=True)
    genre = models.CharField(choices=Genre, max_length=200, null=True)
    acteur = models.CharField(max_length=50, null=True)
    nombre_video : models.IntegerField() 

    def __str__(self):
        return self.title

class Episode(Video):
    
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE, related_name="episodes", null=True)

class Music(Video):
    
    #video=models.ForeignKey(Video,null=True,on_delete=callable)
    chanteur = models.CharField(max_length=50, null=True)
    producteur = models.CharField(max_length=50, null=True)


class Documentaire(Video):
    
    #video=models.ForeignKey(Video,null=True,on_delete=callable)
    producteur = models.CharField(max_length=50, null=True)



# a reviser (A retirer)  -- A remplacer par un nouveau mecanism de recherche.
# class Order(models.Model):
#     music = models.ForeignKey(Music, null=True, on_delete=models.CASCADE)
#     serie = models.ForeignKey(Serie, null=True, on_delete=models.CASCADE)
#     film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
#     documentaire = models.ForeignKey(Documentaire, null=True, on_delete=models.CASCADE)
    

# class listSeeFavorite(Video):
#     video=models.ForeignKey(Video,null=True,on_delete=callable);

class FavoriteVideo(models.Model):
    music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True)
    film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True)
    episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True)
    documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # type=models.CharField(max_length=255)

class Favorite(models.Model):
    music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True)
    film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True)
    episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True)
    documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=255, default="")



class WatchLater(models.Model):
    music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True)
    film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True)
    episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True)
    documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=255, default="")


class Comment(models.Model):
    commenter = models.CharField(max_length = 50,null=True,blank=True)
    body = models.TextField()
    music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True, related_name='commentsMusic')
    film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True, related_name='commentsFilm')
    episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True, related_name='commentsEpisode')
    documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True, related_name='commentsDocumentaire')
    user = models.ManyToManyField(User,blank=True, related_name='user_comment')

    def __str__(self):
        return self.body 


class ReviewRating(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True,blank=True, related_name='reviewMusic')
    film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True,blank=True, related_name='reviewFilm')
    episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True,blank=True, related_name='reviewEpisode')
    documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True,blank=True, related_name='reviewDocumentaire')
    rating = models.IntegerField(default=0)
    review = models.TextField(default="",blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.__str__()


# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField(max_length=1000)
#     rating = models.FloatField(default=0)

#     def __str__(self):
#         return self.user.username




# class ViewCount(models.Model):
#     music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True, related_name='ViewMusic')
#     film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True, related_name='ViewFilm')
#     episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True, related_name='ViewEpisode')
#     documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True, related_name='ViewDocumentaire')
#     ip_address = models.CharField(max_length=50)
#     session = models.CharField(max_length=50)

#     def __str__(self) :
#         return f"{self.ip_address}"






# class Comments(models.Model):
#     ''' Main comment model'''
#     user =  models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
#     comment = models.TextField()
#     music=models.ForeignKey(Music,on_delete=models.CASCADE, null=True, related_name='commentsMusic')
#     film=models.ForeignKey(Film,on_delete=models.CASCADE, null=True, related_name='commentsFilm')
#     episode=models.ForeignKey(Episode,on_delete=models.CASCADE, null=True, related_name='commentEpisode')
#     documentaire=models.ForeignKey(Documentaire,on_delete=models.CASCADE, null=True, related_name='commentsDocumentaire')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def get_total_likes(self):
#         return self.likes.users.count()

#     def get_total_dis_likes(self):
#         return self.dis_likes.users.count()

#     def __str__(self):
#         return str(self.comment)[:30]

# class Like(models.Model):
#     ''' like  comment '''

#     comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
#     users = models.ManyToManyField(User, related_name='requirement_comment_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.comment.comment)[:30]

# class DisLike(models.Model):
#     ''' Dislike  comment '''

#     comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
#     users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.comment.comment)[:30]