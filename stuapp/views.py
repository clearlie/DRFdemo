from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from jsonpickle import json
from rest_framework.viewsets import ModelViewSet
from stuapp.serializers1 import ActorSerializer, MovieSerializer
from stuapp.models import Actor, Movie


class ActorListView(View):
    def get(self, requset):
        actors = Actor.objects.all()

        actorlist = []

        for actor in actors:
            actorlist.append({
                'aid': actor.aid,
                'aname': actor.aname,
                'age': actor.age,
                'agender': actor.agender,
                'birth_date': actor.birth_date,
                'photo': actor.photo.url if actor.photo else ""
            })

            return JsonResponse(actorlist,safe=False)

    def post(self, request):
        # b'aid=8$aname=zhangsan'
        bytes_str = request.body
        # 'aid=8$aname=zhangsan'
        str1 = bytes_str.decode()
        actor_dict = json.loads(str1)

        # 将请求参数存入数据库
        actor = Actor.objects.create(aname=actor_dict.get('aname'),
                                     age=actor_dict.get('age'),
                                     agender=actor_dict.get('agender'),
                                     birth_date=actor_dict.get('birth_date'),
                                     )

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo.url if actor.photo else ""
        }, status=201)




class ActorDetilView(View):
    def get(self, request, pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo.url if actor.photo else ""
        })

    def put(self, request, pk):
        """修改演员信息"""
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        bytes_str = request.body
        str1 = bytes_str.decode()
        actor_dict = json.loads(str1)

        actor.aname = actor_dict.get("aname")
        actor.age = actor_dict.get("age")
        actor.save()

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo.url if actor.photo else ""
        })

    def delete(self, request, pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        actor.delete()

        return JsonResponse({'message': "删除成功"})


class ActorListView2(ModelViewSet):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer