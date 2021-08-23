#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'index.html')
    #return HttpResponse("hello")
def analyze(request):
    djtext=request.GET.get('mytext','default')
    remove=request.GET.get('remove','off')
    print(remove)
    print(djtext)
    params={'purpose':'modified','analyzed_text':djtext}
    return render(request,'analyze.html', params)
