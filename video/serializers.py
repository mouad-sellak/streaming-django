from rest_framework import serializers
from .models import Film, Music, Serie, Documentaire, Video, Episode

class VideoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Video
        fields ="__all__"


class SearchAllSerializer(serializers.ModelSerializer):
    realisateur = serializers.CharField(required=False, allow_blank=True)
    producteur = serializers.CharField(required=False, allow_blank=True)
    acteur = serializers.CharField(required=False, allow_blank=True)
    genre = serializers.CharField(required=False, allow_blank=True)
    chanteur = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Video
        fields =["realisateur","producteur","acteur","genre","chanteur",
        "title","date_création","date_ajout","date_modification","type",
        "duree","Chaine","resolution","Url","taille","vdeo","image","uuid"]



class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = "__all__"



class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = "__all__"



class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = "__all__"



class SerieSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Serie
        fields = "__all__"



class DocumentaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documentaire
        fields = "__all__"
