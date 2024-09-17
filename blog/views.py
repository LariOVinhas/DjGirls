from django. shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("voce chegou ao portão da casa")

def sala(request):
    return HttpResponse(' voce chepou na sala. Senta no sofa')

def quarto(request):
    return HttpResponse("Agora está no quarto, pode se deitar")

def post_list(request):
    return render(request, 'blog/post_list.html', {})