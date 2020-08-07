from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import CrownsPost
# Create your views here.

class PostHome(generic.ListView):
    queryset=CrownsPost.objects.all().order_by('-Created_on')
    template_name='homepage.html'

def Homepage (request):
    Home = CrownsPost.objects.all()
    MaleWears = CrownsPost.objects.filter(Status=2)
    FemaleWears = CrownsPost.objects.filter(Status=3)
    T_Shirts = CrownsPost.objects.filter(Status=4)
    Joggers = CrownsPost.objects.filter(Status=5)
    Trousers = CrownsPost.objects.filter(Status=6)
    Gowns = CrownsPost.objects.filter(Status=7)
    Hoods = CrownsPost.objects.filter(Status=8)
    Vintages = CrownsPost.objects.filter(Status=9)
    Foot_wears = CrownsPost.objects.filter(Status=10)
    Special_offers = CrownsPost.objects.filter(Status=11)

    context = {'Home': Home, 'Special_offers': Special_offers}
    return render(request, 'homepage.html', context=context)

def PostDetail(request,slug):
    template_name = 'detailpage.html'
    post=get_object_or_404(CrownsPost, Slug=slug)
    avaliable=CrownsPost.objects.all().order_by('Created_on')
    context = {'avaliable': avaliable,'details':post}

    return render(request,template_name, context=context)

def MaleWears(request):
    MaleWears = CrownsPost.objects.filter(Status=2)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'MaleWears': MaleWears}
    return render(request, 'MaleWearspage.html', context=context)

def FemaleWears(request):
    FemaleWears = CrownsPost.objects.filter(Status=3)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'FemaleWears': FemaleWears}
    return render(request, 'FemaleWearspage.html', context=context)

def T_Shirts(request):
    T_Shirts = CrownsPost.objects.filter(Status=4)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'T_Shirts': T_Shirts}
    return render(request, 'T_Shirtspage.html', context=context)

def Joggers(request):
    Joggers = CrownsPost.objects.filter(Status=5)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'Joggers': Joggers}
    return render(request, 'Joggerspage.html', context=context)

def Trousers(request):
    Trousers = CrownsPost.objects.filter(Status=6)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'Trousers': Trousers}
    return render(request, 'Trouserspage.html', context=context)

def Gowns(request):
    Gowns = CrownsPost.objects.filter(Status=7)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'Gowns': Gowns}
    return render(request, 'Gownspage.html', context=context)

def Hoods(request):
    Hoods = CrownsPost.objects.filter(Status=8)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'Hoods': Hoods}
    return render(request, 'Hoodspage.html', context=context)

def Vintages(request):
    Vintages = CrownsPost.objects.filter(Status=9)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'Vintages': Vintages}
    return render(request, 'Vintagespage.html', context=context)

def FootWears(request):
    FootWears = CrownsPost.objects.filter(Status=10)
    Home = CrownsPost.objects.all()
    context = {'Home': Home, 'FootWears': FootWears}
    return render(request, 'FootWearspage.html', context=context)

