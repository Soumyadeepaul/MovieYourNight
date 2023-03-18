from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import details,form
from .utils import get_plot, get_plot1, get_plot2, status,time,line_time
import pandas as pd
from .ml import recommend
from json import dumps
from .scrap import image
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
        movie=request.POST.get('movie')
        data=form(age=age,year=year,genre=genre,movie=movie)
        data.save()
        movies_list=recommend(year,genre,movie)
        d1=dict(movies_list[0])
        print(d1)
        id=d1['id']
        print(id)
        imdb_link1=d1['imdb_link']
        print(imdb_link1)
        image_link=image(id,imdb_link1)
        print(image_link)



        movie1=d1['movie_name']
        image1=image_link
        rating1=d1['rating']
        gross1=d1['gross']
        votes1=d1['votes']
        metascore1=d1['metascore']
        certificate1=d1['certificate']
        certificate_meaning1=d1['certificate_meaning']
        director1=d1['director']
        stars1=d1['stars']
        time1=d1['time']
        description1=d1['description']
        genre1=d1['genre']
        d2 = dict(movies_list[1])

        id = d2['id']
        print(id)
        imdb_link2 = d2['imdb_link']
        print(imdb_link2)
        image_link = image(id, imdb_link2)
        print(image_link)

        movie2=d2['movie_name']
        image2=image_link
        rating2=d2['rating']
        gross2=d2['gross']
        votes2=d2['votes']
        metascore2=d2['metascore']
        certificate2=d2['certificate']
        certificate_meaning2=d2['certificate_meaning']
        director2=d2['director']
        stars2=d2['stars']
        time2=d2['time']
        description2=d2['description']
        genre2=d2['genre']
        d3 = dict(movies_list[2])
        id = d3['id']
        print(id)
        imdb_link3 = d3['imdb_link']
        print(imdb_link3)
        image_link = image(id, imdb_link3)
        print(image_link)
        movie3 = d3['movie_name']
        image3 = image_link
        rating3 = d3['rating']
        gross3 = d3['gross']
        votes3 = d3['votes']
        metascore3 = d3['metascore']
        certificate3 = d3['certificate']
        certificate_meaning3 = d3['certificate_meaning']
        director3 = d3['director']
        stars3 = d3['stars']
        time3 = d3['time']
        description3 = d3['description']
        genre3 = d3['genre']
        d4 = dict(movies_list[3])
        id = d4['id']
        print(id)
        imdb_link4 = d4['imdb_link']
        print(imdb_link4)
        image_link = image(id, imdb_link4)
        print(image_link)
        movie4 = d4['movie_name']
        image4 = image_link
        rating4 = d4['rating']
        gross4 = d4['gross']
        votes4 = d4['votes']
        metascore4 = d4['metascore']
        certificate4 = d4['certificate']
        certificate_meaning4 = d4['certificate_meaning']
        director4 = d4['director']
        stars4 = d4['stars']
        time4 = d4['time']
        description4 = d4['description']
        genre4 = d4['genre']
        print('Hello')
        success=[image1,movie1,genre1,str(rating1),stars1,director1,str(time1),description1,certificate1,certificate_meaning1,str(metascore1),str(gross1),str(votes1),image2,movie2,genre2,str(rating2),stars2,director2,str(time2),description2,certificate2,certificate_meaning2,str(metascore2),str(gross2),str(votes2),image3,movie3,genre3,str(rating3),stars3,director3,str(time3),description3,certificate3,certificate_meaning3,str(metascore3),str(gross3),str(votes3),image4,movie4,genre4,str(rating4),stars4,director4,str(time4),description4,certificate4,certificate_meaning4,str(metascore4),str(gross4),str(votes4),imdb_link1,imdb_link2,imdb_link3,imdb_link4]
        success=dumps(success)
        return HttpResponse(success)
    global df
    df = pd.DataFrame(list(details.objects.all().values()))
    d=df.copy()
    d['movie_name'] = d['movie_name'].str.replace("'", '')
    d['movie_name'] = df['movie_name'].str.replace('"', '')
    s = df['movie_name'].to_list()
    s = sorted(s)
    s = str(s)
    s = s.replace("'", '')
    return render(request, 'main.html',{'movie': s})
def home(request):
    return render(request,'Home.html')


def dashboard(request,year,genre):
    if year==0:
        year='all'
    print('aefsdg')


    df = pd.DataFrame(list(details.objects.all().values()))
    if year!='all':
        df=df[df['start_year']==year]
    if genre!='all':
        df=df[df[genre]==1]
    if year=='all':
        df=df[df['start_year']>1700]
    total_movie = len(df)
    total_time=df['time'].sum()
    avg_rating=df['rating'].mean()
    cop=df.copy()
    cop=cop[cop['director']=='NoDirector']
    no_director=len(cop)
    cop=df.copy()
    cop = cop[cop['stars'] == 'NoStars']
    no_stars = len(cop)
    avg_vote=df['votes'].mean()
    print(total_movie,total_time,avg_rating,no_director,no_stars,avg_vote)

    main=df.copy()

    d=main.copy()
    print('111')
    l = d["stars"].str.split(",")
    d["first_name"] = l.str[:1]
    d["first_name"] = d["first_name"].str[:].str[0]
    global chart
    chart=get_plot(d,genre,year)
    print(1)

    df1 = main.copy()
    #df1 = df1.dropna().reset_index()

    df1=df1[df1['director']!='NoDirector']
    global chart1
    chart1=get_plot1(df1)
    print(2)

    df2 = main.copy()
    df2 = df2.dropna().reset_index()
    global chart2
    chart2 = get_plot2(df2,genre,year)
    print(3)

    global chart3
    chart3= status(df2,genre,year)
    print(4)
    global chart4
    df3=main.copy()
    chart4=time(df3,genre,year)
    print(5)

    df4=main.copy()
    global chart5
    chart5=line_time(df4,genre,year)
    print(6)
    return render(request,'dashboard.html',{'chart':chart,'chart1':chart1, 'chart2': chart2 , 'total_movie':total_movie,'year':year ,'chart3':chart3,'chart4':chart4, 'chart5': chart5,'total_time':total_time,'avg_rating':avg_rating,'avg_vote':avg_vote,'no_stars':no_stars,'no_director':no_director})

def graph(request,pos):
    if pos=='1':
        return render(request, 'graph.html', {'chart': chart})
    elif pos=='2':
        return render(request, 'graph.html', {'chart': chart5})
    elif pos=='3':
        return render(request, 'graph.html', {'chart': chart3})
    elif pos=='4':
        return render(request, 'graph.html', {'chart': chart4})
    elif pos=='5':
        return render(request, 'graph.html', {'chart': chart1})
    elif pos=='6':
        return render(request,'graph.html',{'chart':chart2})

def aboutus(request):
    return render(request,'aboutus.html')

