#模型类序列化器

from  stuapp.models import *
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'      #表示所有对应的Actor模块所有字段
        #fields = ('aid', 'aname', 'age', 'agender') #表示只对括号内的字段进行序列化
        #read_only_field = ('aid')  #指定字段为只读模式
        # extra_kwargs = {
        #     'age': {'min_value': 0, 'required': False},
        #     'agender': {'default': "女"},
        # }
