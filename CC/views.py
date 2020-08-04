from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import CrownsPost
# Create your views here.

class PostHome(generic.ListView):
    queryset=CrownsPost.objects.all().order_by('-Created_on')
    template_name='homepage.html'

class PostDetails(generic.DetailView):
    model = CrownsPost
    template_name = 'detailpage.html'

def PostDetail(request,slug):
    template_name = 'detailpage.html'
    post=get_object_or_404(CrownsPost, Slug=slug)

    return render(request,template_name,{'blog':post})

class MaleWears(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=2).order_by('-Created_on')
    template_name='MaleWearspage.html'

class FemaleWears(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=3).order_by('-Created_on')
    template_name='FemaleWearspage.html'

class T_Shirts(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=4).order_by('-Created_on')
    template_name='T_Shirtspage.html'

class Joggers(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=5).order_by('-Created_on')
    template_name='Joggerspage.html'

class Trousers(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=6).order_by('-Created_on')
    template_name='Trouserspage.html'

class Gowns(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=7).order_by('-Created_on')
    template_name='Gownspage.html'

class Hoods(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=8).order_by('-Created_on')
    template_name='Hoodspage.html'

class Vintages(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=9).order_by('-Created_on')
    template_name='Vintagespage.html'

class FootWears(generic.ListView):
    queryset=CrownsPost.objects.filter(Status=10).order_by('-Created_on')
    template_name='FootWearspage.html'

