from . import views
from django.urls import path

urlpatterns=[
    path('',views.PostHome.as_view(),name='home'),
    path('MaleWears/',views.MaleWears.as_view(),name='MaleWears'),
    path('FemaleWears/',views.FemaleWears.as_view(),name='FemaleWears'),
    path('T_Shirts/',views.T_Shirts.as_view(),name='T_Shirts'),
    path('Joggers/',views.Joggers.as_view(),name='Joggers'),
    path('Trousers/',views.Trousers.as_view(),name='Trousers'),
    path('Gowns/',views.Gowns.as_view(),name='Gowns'),
    path('Hoods/',views.Hoods.as_view(),name='Hoods'),
    path('Vintages/',views.Vintages.as_view(),name='Vintages'),
    path('FootWears/',views.FootWears.as_view(),name='FootWears'),
    path('<slug:slug>/',views.PostDetail,name='post_detail'),
]

