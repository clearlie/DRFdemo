from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from stuapp.models import Actor, Movie
from stuapp.serializers1 import *


class ActorListView(APIView):
    def get(self, request):
        actorlists = Actor.objects.all()
        aserializer = ActorSerializer(instance=actorlists, many=True)

        return Response(data=aserializer.data)


class ActorListView1(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, pk):
        #获取序列化对象
        actor = self.get_object()
        #序列化数据
        actorser = self.get_serializer(instance=actor)

        return Response(actorser.data)

class MovieListView(APIView):
    def get(self, request):
        movielists = Movie.objects.all()
        mvserializer = MovieSerializer(instance=movielists, many=True)

        return Response(mvserializer.data)