from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class UserDetail(models.Model):
    Uid = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()
    #TODO : DP

    def __str__(self):
        return str(self.Email)


class Quiz(models.Model):
    Qid = models.AutoField(primary_key=True)
    Qname = models.CharField(max_length=100)
    Privacy = models.BooleanField()
    #Tags = models.CharField(max_length=100)
    Uid = models.ForeignKey(UserDetail)

    def __str__(self):
        return str(self.Qid)


class Questions(models.Model):
    Qsid = models.AutoField(primary_key=True)
    Answer = models.IntegerField()
    QuesDetail = models.TextField()
    Opt1 = models.CharField(max_length=100)
    Opt2 = models.CharField(max_length=100)
    Opt3 = models.CharField(max_length=100)
    Opt4 = models.CharField(max_length=100)
    Hint = models.CharField(max_length=100,blank=True)
    Time = models.FloatField()
    Qid = models.ForeignKey(Quiz)

    def __str__(self):
        return str(self.Qsid)

class Tags(models.Model):
    Tid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Qid = models.ForeignKey(Quiz)


class Attend(models.Model):
    Uid = models.ForeignKey(UserDetail)
    Aid = models.OneToOneField(User)
    Qid = models.ForeignKey(Quiz)
    Score = models.FloatField()

    class Meta:
        unique_together = (("Uid","Aid","Qid"))
