from django.db import models
from random import choice, shuffle

# Create your models here.



class Origin(models.Model):
    cathegory=models.CharField(max_length=50,blank=False,unique=True)

    class Meta:
        app_label = 'proverbs'

class Tag(models.Model):
    tag=models.CharField(max_length=50,unique=True,blank=False)

class Proverb(models.Model):
    text=models.TextField(blank=False,unique=True)
    origin=models.ManyToManyField(Origin,blank=True,through="OriginConnection")
    tag=models.ManyToManyField(Tag,blank=True,through="TagConnection")
    published=models.DateField(auto_now_add=True)
    good=models.IntegerField(default=0)
    bad=models.IntegerField(default=0)

class OriginConnection(models.Model):
    proverb = models.ForeignKey(Proverb, null=True,on_delete=models.SET_NULL)
    origin = models.ForeignKey(Origin, null=True,on_delete=models.SET_NULL)

class TagConnection(models.Model):
    proverb = models.ForeignKey(Proverb, null=True,on_delete=models.SET_NULL)
    Tag = models.ForeignKey(Tag, null=True,on_delete=models.SET_NULL)

def chooseRandomProverb():
    proverb_ids=Proverb.objects.all().values_list('pk', flat=True)
    chosen=choice(proverb_ids)
    return Proverb.objects.get(pk=chosen)

def chooseRandomTwoProverbs():
    proverb_ids=list(Proverb.objects.all().values_list('pk', flat=True))
    #print(type(proverb_ids))
    #print("before",proverb_ids[:5])
    shuffle(proverb_ids)
    #print("after",proverb_ids[:5])
    #chosen=proverb_ids[:2 ]
    return Proverb.objects.get(pk=proverb_ids[0]),Proverb.objects.get(pk=proverb_ids[1])

def vote(numbers):
    first,second=numbers
    winner=Proverb.objects.get(pk=first)
    winner.good+=1
    winner.save()
    looser=Proverb.objects.get(pk=second)
    looser.bad+=1
    looser.save()

#    2.	Origin  otm
#3.	Tag  mtm
#4.	Published
#style
#5.	For_vote
#6.	Against_vote


