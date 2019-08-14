import re

from rest_framework import serializers
from stuapp.models import *


class ActorSerializer(serializers.Serializer):

    Gender_ID = (
        ('男', '男'),
        ('女', '女'),
    )
    aid = serializers.IntegerField(label='编号', read_only=True)
    aname = serializers.CharField(label='姓名', max_length=32, help_text='请输入演员信息')
    age = serializers.IntegerField(label='年龄', required=False)
    agender = serializers.ChoiceField(choices=Gender_ID, label='性别', required=False)
    birth_date = serializers.DateField(label='出生年月', required=False)
    photo = serializers.ImageField(label='头像', required=False)

    def validate(self, attrs):
        aname = attrs['aname']
        age = attrs['age']

        if 'hello' in aname:
            return serializers.ValidationError('aname不能包含hello')

        reg = r'^[123]\d{1}$'
        v = str(age)
        if not re.match(reg, v):
            raise serializers.ValidationError('age 字段值必须在10-40之间')

        return attrs

#create方法重写，用于保存新建的对象
    def create(self, validated_data):
        """
        creat:
        保存演员信息
        """
        instance = Actor.objects.create(**validated_data)
        return instance

    """updata方法重写，用于数据的修改"""
    def update(self, instance, validated_data):
        instance.aid = validated_data.get('aid', instance.aid)
        instance.aname = validated_data.get('aname', instance.aname)
        instance.age = validated_data.get('age', instance.age)
        instance.agender = validated_data.get('agender', instance.agender)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号', read_only=True)
    mname = serializers.CharField(label='影片名称', max_length=30)
    m_pub_date = serializers.DateField(label='上映日期', required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论', max_length=356, required=False, allow_null=True)
    mimage = serializers.ImageField(label='图片', required=False)
    actors = serializers.PrimaryKeyRelatedField(label='演员', read_only=True)
    actors_id = serializers.IntegerField()
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


    #使用序列化器
    #actors = ActorSerializer()
    #
    #actors = StringRelatedField()

# from stuapp.serializers import *
# from stuapp.models import *
# data = {'aname':'nezha','age':33, 'agender':'男', 'birth_date':'1986-02-25'}
# a = ActorSerializer(data=data)