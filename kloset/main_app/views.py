from django.http import HttpResponse

def home(request):
    return HttpResponse('this is home')

def cost(request):
    return HttpResponse('this is cost')