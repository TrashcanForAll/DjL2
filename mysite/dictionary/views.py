from django.http import HttpResponse
from django.shortcuts import render
from .models import Dict
from .forms import WordForm

dict = 12

def home(request):
    context = {
        'PageTitle': 'Dictionary',
        'active':"Home",
    }
    return render(request, 'dictionary/home.html', context)

def wordsList(request):
    context = {
        'PageTitle': 'Dictionary',
        'active': "WordsList",
        'words': Dict.objects.all()
    }
    return render(request, 'dictionary/wordsList.html', context)

def addWord(request):
    context = {
        'PageTitle': 'Dictionary',
        'active': "AddWord",
        'form': WordForm,
    }

    if request.method == "GET":
        return render(request, 'dictionary/addWord.html', context)
    else:
        try:
            word = Dict.objects.create(originalW = request.POST.get('originalW'), translationW = request.POST.get('translationW'))
            word.save()
            context["success"] = 'success'
        except Exception as ex:
            context["error"] = ex
            # print(ex)
        return render(request, 'dictionary/addWord.html', context)
