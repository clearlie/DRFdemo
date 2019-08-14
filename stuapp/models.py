from django.db import models


class Actor(models.Model):
    agender = (
        ('男', "男"),
        ('女', "女"),
    )
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32, unique=True, help_text='请输入演员信息')
    age = models.PositiveIntegerField()
    agender = models.CharField(max_length=2, choices=agender, default='男')
    birth_date = models.DateField()
    photo = models.ImageField(default='', upload_to='actor/')

    def __str__(self):
        return self.aname

    class Meta:
        db_table = 't_actor'
        verbose_name_plural = "演员"


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30)
    m_pub_date = models.DateField()
    mread = models.PositiveIntegerField()
    mcomment = models.TextField()
    mimage = models.ImageField(upload_to='movies/')
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 't_movie'
        verbose_name_plural = '电影'