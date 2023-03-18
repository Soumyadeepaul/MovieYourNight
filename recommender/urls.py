from django.urls import path
from . import views
urlpatterns=[
    path('',views.movies,name='movies'),
    path('home/',views.home,name='home'),
    path('<str:pos>',views.graph,name='graph'),
    path('dashboard/<int:year><str:genre>',views.dashboard,name='dashboard'),
    path('aboutus/',views.aboutus,name='abouutus'),
]