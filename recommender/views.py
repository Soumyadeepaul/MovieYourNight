from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import details,certificate,form
from .utils import get_plot, get_plot1, get_plot2, status
import pandas as pd

# Create your views here.

def movies(request):
    if request.method=='POST':
        #global age
        age=request.POST.get('age')
        #global year
        year=request.POST.get('year')
        if year=='SinceBeginning':
            year=0
        #global genre
        genre=request.POST.get('genre')
        data=form(age=age,year=year,genre=genre)
        data.save()
    return render(request, 'main.html')

def home(request):
    return render(request,'Home.html')


def dashboard(request,year,genre):
    if year==0:
        year='all'
    df=pd.DataFrame(list(details.objects.all().values()))
    l = df["stars"].str.split(",")
    df["first_name"] = l.str[:1]
    df["first_name"] = df["first_name"].str[:].str[0]
    global chart
    chart=get_plot(df,genre,year)
    print(1)


    df1 = pd.DataFrame(list(details.objects.all().values()))
    df1 = df1.dropna().reset_index()
    total = len(df1)
    df1=df1[df1['director']!='NoDirector']
    global chart1
    chart1=get_plot1(df1,genre,year)
    print(2)

    df2 = pd.DataFrame(list(details.objects.all().values()))
    df2 = df2.dropna().reset_index()
    global chart2
    chart2 = get_plot2(df2,genre,year)
    print(3)

    global chart3
    chart3= status(df2,genre,year)
    return render(request,'dashboard.html',{'chart':chart,'chart1':chart1, 'chart2': chart2 , 'total_movie':total,'year':year ,'chart3':chart3})

def graph(request,pos):
    if pos=='1':
        return render(request, 'graph.html', {'chart': chart})
    elif pos=='2':
        pass
    elif pos=='3':
        return render(request, 'graph.html', {'chart': chart3})
    elif pos=='4':
        pass
    elif pos=='5':
        return render(request, 'graph.html', {'chart': chart1})
    elif pos=='6':
        return render(request,'graph.html',{'chart':chart2})

