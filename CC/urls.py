from . import views
from django.urls import path

urlpatterns=[
    path('',views.Homepage ,name='home'),
    path('MaleWears/',views.MaleWears,name='MaleWears'),
    path('FemaleWears/',views.FemaleWears,name='FemaleWears'),
    path('T_Shirts/',views.T_Shirts,name='T_Shirts'),
    path('Joggers/',views.Joggers,name='Joggers'),
    path('Trousers/',views.Trousers,name='Trousers'),
    path('Gowns/',views.Gowns,name='Gowns'),
    path('Hoods/',views.Hoods,name='Hoods'),
    path('Vintages/',views.Vintages,name='Vintages'),
    path('FootWears/',views.FootWears,name='FootWears'),
    path('<slug:slug>/',views.PostDetail,name='post_detail'),
]

