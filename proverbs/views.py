from django.shortcuts import render

from django.http import HttpResponse, HtttpResponseRedirect
from proverbs.models import Proverb, chooseRandomProverb, chooseRandomTwoProverbs, vote
from django.urls import reverse


app_name="proverbs"

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def proverb(request,number):
    text=chooseRandomProverb().text
    return render(request,"proverbs\one_proverb.html",{'text':text,"num":10})

def proverb2(request,number):
    first,second=chooseRandomTwoProverbs()
    return render(request,r"proverbs\two_proverbs.html",{'text1':first.text,'text2':second.text ,"num":10})

def voteGoodBad(request,numbers):
    vote(numbers)
    return HtttpResponseRedirect(reverse("proverbs:proverb2"),args=(1,)) 