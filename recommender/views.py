from django.shortcuts import render
from django.http import HttpResponse
#database in model named as movies
from .models import details,form,data
#all the plots
from .utils import stars, wordcloud, certificate, status,rating,line_time
import pandas as pd
#recommender system
from .ml import recommend
from json import dumps
#scrap images
from .scrap import image
import random
# Create your views here.


#Main page
def movies(request):
    if request.method=='POST':
        #get the age
        age=request.POST.get('age')
        #get the year
        year=request.POST.get('year')
        #if year is SinceBeginning convert to 0 and year is INTEGER
        if year=='SinceBeginning':
            year=0
        #get the genre
        genre=request.POST.get('genre')
        #get the movie
        movie=request.POST.get('movie')
        #update the model form with new data
        data=form(age=age,year=year,genre=genre,movie=movie)
        #save the model form
        data.save()
        #calling the function recommend for movie recommendation passing year genre and movie name
        movies_list=recommend(year,genre,movie)
        #movies_list is a list of 4 element
        #the 1st movie
        d1=dict(movies_list[0])
        #store the id for the image scraping
        id=d1['id']
        #store the imdb link for showing in web page and opening the imdb page in web scraping
        imdb_link1=d1['imdb_link']
        #calling the image function from scrap and passing id and imdblink
        image1=image(id,imdb_link1)
        #store the movie name of movie 1
        movie1=d1['movie_name']
        #store the rating of movie 1
        rating1=d1['rating']
        # store the gross of movie 1
        gross1=d1['gross']
        # store the votes of movie 1
        votes1=d1['votes']
        # store the metascore of movie 1
        metascore1=d1['metascore']
        # store the certificate of movie 1
        certificate1=d1['certificate']
        # store the certificate meaning of movie 1
        certificate_meaning1=d1['certificate_meaning']
        # store the director of movie 1
        director1=d1['director']
        # store the stars of movie 1
        stars1=d1['stars']
        # store the time of movie 1
        time1=d1['time']
        # store the description of movie 1
        description1=d1['description']
        # store the genre of movie 1
        genre1=d1['genre']

        #the 2nd movie
        d2 = dict(movies_list[1])
        #same process as 1st movie
        id = d2['id']
        imdb_link2 = d2['imdb_link']
        image2 = image(id, imdb_link2)
        movie2=d2['movie_name']
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
        if len(movies_list)==4:
            #the 3rd movie
            d3 = dict(movies_list[2])
            id = d3['id']
            imdb_link3 = d3['imdb_link']
            image3 = image(id, imdb_link3)
            movie3 = d3['movie_name']
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

            #the 4th movie
            d4 = dict(movies_list[3])
            id = d4['id']
            imdb_link4 = d4['imdb_link']
            image4 = image(id, imdb_link4)
            movie4 = d4['movie_name']
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
            #putting everthing stored in the list named as success
            success=[image1,movie1,genre1,str(rating1),stars1,director1,str(time1),description1,certificate1,certificate_meaning1,str(metascore1),str(gross1),str(votes1),image2,movie2,genre2,str(rating2),stars2,director2,str(time2),description2,certificate2,certificate_meaning2,str(metascore2),str(gross2),str(votes2),image3,movie3,genre3,str(rating3),stars3,director3,str(time3),description3,certificate3,certificate_meaning3,str(metascore3),str(gross3),str(votes3),image4,movie4,genre4,str(rating4),stars4,director4,str(time4),description4,certificate4,certificate_meaning4,str(metascore4),str(gross4),str(votes4),imdb_link1,imdb_link2,imdb_link3,imdb_link4]
            #converting list into JSON using dumps
            success=dumps(success)
            #pass the JSON to the main.html as it uses ajax
            return HttpResponse(success)
        # putting everthing stored in the list named as success
        success = [image1, movie1, genre1, str(rating1), stars1, director1, str(time1), description1, certificate1,
                   certificate_meaning1, str(metascore1), str(gross1), str(votes1), image2, movie2, genre2,
                   str(rating2), stars2, director2, str(time2), description2, certificate2, certificate_meaning2,
                   str(metascore2), str(gross2), str(votes2), 'https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png', 'empty', 'empty', 'empty', 'empty',
                   'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                   'empty', 'empty', 'https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                   'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                   imdb_link1, imdb_link2, 'https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png', 'https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png']
        # converting list into JSON using dumps
        success = dumps(success)
        # pass the JSON to the main.html as it uses ajax
        return HttpResponse(success)

    #declaring dataframe as global so that dashboard dont have to load it again
    # model details to dataframe

    df = pd.DataFrame(list(details.objects.all().values()))
    #copy of dataframe so that no change in main dataset
    d=df.copy()
    #replace ' and " to   in movie name
    d['movie_name'] = d['movie_name'].str.replace("'", '')
    d['movie_name'] = df['movie_name'].str.replace('"', '')
    #converting into list
    s = df['movie_name'].to_list()
    #sorting the list
    s = sorted(s)
    #converting the list to string
    s = str(s)
    #replacing extra ' to
    s = s.replace("'", '')
    #rendering main.html and passing movie name as movie
    return render(request, 'main.html',{'movie': s})

#home.html or the ad page
def home(request):
    return render(request,'Home.html')

#dashboard.html
def dashboard(request,year,genre):
    #if page is refreshed dataframe will be lost so we have to call it again
    df = pd.DataFrame(list(details.objects.all().values()))
    #if year not all then filter
    if year!=0:
        df=df[df['start_year']==year]
    #if genre not all filter genre's column like comedy value with 1
    if genre!='all':
        df=df[df[genre]==1]
    #if year is all then remove 0 that is rumoured
    if year==0:
        df=df[df['start_year']>1700]
        year='all'
    #total dataset length
    total_movie = len(df)
    #total time present in dataset
    total_time=df['time'].sum()
    #average rating of the dataset
    avg_rating=df['rating'].mean()
    #copy the dataset not to change the main dataset
    cop=df.copy()
    #count of director not present
    cop=cop[cop['director']=='NoDirector']
    no_director=len(cop)
    # copy the dataset not to change the main dataset
    cop=df.copy()
    # count of stars not present
    cop = cop[cop['stars'] == 'NoStars']
    no_stars = len(cop)
    avg_vote=df['votes'].mean()
    # copy the dataset not to change the main dataset
    main=df.copy()
    # copy the dataset not to change the main dataset
    d=main.copy()
    #stars name and make a new column with the 1st star present in the list
    l = d["stars"].str.split(",")
    d["first_name"] = l.str[:1]
    d["first_name"] = d["first_name"].str[:].str[0]
    #globalize the graph 1 the stars bar plot
    global chart1
    chart1=stars(d,genre,year)
    #copy of main dataset
    df1 = main.copy()
    #remove no director
    df1=df1[df1['director']!='NoDirector']
    #globalize the graph 2 word cloud of director
    global chart2
    chart2=wordcloud(df1)
    #copy the main dataset
    df2 = main.copy()
    #globalize graph 3 certificate histogram
    global chart3
    chart3 = certificate(df2,genre,year)
    # globalize the graph 4 movie/series pie chart
    global chart4
    chart4= status(df2,genre,year)
    # globalize the graph 5 average rating bubble
    global chart5
    df3=main.copy()
    chart5=rating(df3,genre,year)

    df4=main.copy()
    # globalize the graph 6 total time line chart
    global chart6
    chart6=line_time(df4,genre,year)

    #rendering dashboard.html and passing all graphs and informations
    return render(request,'dashboard.html',{'chart1':chart1,'chart2':chart2, 'chart3': chart3 , 'total_movie':total_movie,'year':year ,'chart4':chart4,'chart5':chart5, 'chart6': chart6,'total_time':total_time,'avg_rating':avg_rating,'avg_vote':avg_vote,'no_stars':no_stars,'no_director':no_director})

#graph.html for open the graph
def graph(request,pos):
    #reuse graph.html
    if pos=='1':
        return render(request, 'graph.html', {'chart': chart1})
    elif pos=='2':
        return render(request, 'graph.html', {'chart': chart2})
    elif pos=='3':
        return render(request, 'graph.html', {'chart': chart3})
    elif pos=='4':
        return render(request, 'graph.html', {'chart': chart4})
    elif pos=='5':
        return render(request, 'graph.html', {'chart': chart5})
    elif pos=='6':
        return render(request,'graph.html',{'chart':chart6})
#Aboutus.html
def aboutus(request):
    return render(request,'aboutus.html')






def survey(request):
    if request.method=='POST':
        #get the genre
        genre=request.POST.get('genre')

        global movie1
        global movie2
        global movie3
        global movie4
        global id1,id2,id3,id4
        global df
        try:
            name=request.POST.get('name1')
            rate1=request.POST.get('rate1')
            rate2 = request.POST.get('rate2')
            rate3 = request.POST.get('rate3')
            rate4 = request.POST.get('rate4')
            data1 = data(name=name, movie1=movie1,rate1=int(rate1),movie2=movie2,rate2=int(rate2),movie3=movie3,rate3=int(rate3),movie4=movie4,rate4=int(rate4))

            data1.save()

            
            df1=df[df.id==id1]
            df1 = df1.append(df[df.id == id2])
            df1 = df1.append(df[df.id == id3])
            df1 = df1.append(df[df.id == id4])

            rates=[rate4,rate3,rate2,rate1]
            
            k = pd.DataFrame(columns=['comedy', 'sci_fi', 'horror', 'romance',
                                      'action', 'thriller', 'drama', 'mystery', 'crime', 'animation',
                                      'adventure', 'fantasy', 'family', 'biography', 'docum', 'film_noir',
                                      'history', 'music', 'musical', 'short', 'sport', 'superhero', 'war',
                                      'western'])
            
            
            for i in range(4):
                s = rates.pop()
                print(s)
                k.loc[len(k.index)] = df1.iloc[i, 18:42] * s


           
            k = k.replace('', 0)
            def type_conv(a):
                k[a]=k[a].astype('int')
            col=['comedy', 'sci_fi', 'horror', 'romance',
                                      'action', 'thriller', 'drama', 'mystery', 'crime', 'animation',
                                      'adventure', 'fantasy', 'family', 'biography', 'docum', 'film_noir',
                                      'history', 'music', 'musical', 'short', 'sport', 'superhero', 'war',
                                      'western']
            for i in col:
                type_conv(i)
            
            k = k.sum()
            
            ma = k.max()
            mi = k.min()
            p = -1
            
            for i in k:
                p += 1

                k[p] = (i - mi) / (ma - mi)
            
            #future warning pd.concat
            df = df[df['movie_name'] != movie1]
            df = df.append(df[df['movie_name'] != movie2])
            df = df.append(df[df['movie_name'] != movie2])
            df = df.append(df[df['movie_name'] != movie3])
            
            d = df.iloc[:, 18:42] * k
            
            d = pd.DataFrame(d.sum(axis=1))

            d=d.join(df.loc[:, 'movie_name']).sort_values(by=0)
            d=d.drop_duplicates()
            d=d.tail(4)
            print(d)



            movie1 = ''
            movie2 = ''
            movie3 = ''
            movie4 = ''

            #recomendation
            nums = [d.index[0], d.index[1], d.index[2], d.index[3]]
            print(nums)
            d1 = df[df.index==nums[0]]
            print('hiii')
            d1 = d1.drop_duplicates()
            d1=d1.iloc[:,:]
            # store the id for the image scraping
            id = d1['id']
            # store the imdb link for showing in web page and opening the imdb page in web scraping
            imdb_link1 = d1['imdb_link']
            imdb_link1=imdb_link1.values[0]
            # calling the image function from scrap and passing id and imdblink
            image1 = image(id, imdb_link1)
            # store the movie name of movie 1

            movie1 = d1['movie_name'].values[0]
            # store the rating of movie 1
            rating1 = d1['rating'].values[0]
            # store the gross of movie 1
            gross1 = d1['gross'].values[0]
            # store the votes of movie 1
            votes1 = d1['votes'].values[0]
            # store the metascore of movie 1
            metascore1 = d1['metascore'].values[0]
            # store the certificate of movie 1
            certificate1 = d1['certificate'].values[0]
            # store the certificate meaning of movie 1
            certificate_meaning1 = d1['certificate_meaning'].values[0]
            # store the director of movie 1
            director1 = d1['director'].values[0]
            # store the stars of movie 1
            stars1 = d1['stars'].values[0]
            # store the time of movie 1
            time1 = d1['time'].values[0]
            # store the description of movie 1
            description1 = d1['description'].values[0]
            # store the genre of movie 1
            genre1 = d1['genre'].values[0]
            
            d2 = df[df.index == nums[1]]
            d2 = d2.drop_duplicates()
            # same process as 1st movie
            id = d2['id']
            imdb_link2 = d2['imdb_link']
            imdb_link2 = imdb_link2.values[0]
            image2 = image(id, imdb_link2)
            movie2 = d2['movie_name'].values[0]
            rating2 = d2['rating'].values[0]
            gross2 = d2['gross'].values[0]
            votes2 = d2['votes'].values[0]
            metascore2 = d2['metascore'].values[0]
            certificate2 = d2['certificate'].values[0]
            certificate_meaning2 = d2['certificate_meaning'].values[0]
            director2 = d2['director'].values[0]
            stars2 = d2['stars'].values[0]
            time2 = d2['time'].values[0]
            description2 = d2['description'].values[0]
            genre2 = d2['genre'].values[0]
            
            d3 = df[df.index == nums[2]]
            d3 = d3.drop_duplicates()
            id = d3['id']

            imdb_link3 = d3['imdb_link']
            imdb_link3 = imdb_link3.values[0]
            image3 = image(id, imdb_link3)
            movie3 = d3['movie_name'].values[0]
            rating3 = d3['rating'].values[0]
            gross3 = d3['gross'].values[0]
            votes3 = d3['votes'].values[0]
            metascore3 = d3['metascore'].values[0]
            certificate3 = d3['certificate'].values[0]
            certificate_meaning3 = d3['certificate_meaning'].values[0]
            director3 = d3['director'].values[0]
            stars3 = d3['stars'].values[0]
            time3 = d3['time'].values[0]
            description3 = d3['description'].values[0]
            genre3 = d3['genre'].values[0]
            
            # the 4th movie
            d4 = df[df.index == nums[3]]
            d4 = d4.drop_duplicates()
            id = d4['id']
            imdb_link4 = d4['imdb_link']
            imdb_link4 = imdb_link4.values[0]
            image4 = image(id, imdb_link4)
            movie4 = d4['movie_name'].values[0]
            rating4 = d4['rating'].values[0]
            gross4 = d4['gross'].values[0]
            votes4 = d4['votes'].values[0]
            metascore4 = d4['metascore'].values[0]
            certificate4 = d4['certificate'].values[0]
            certificate_meaning4 = d4['certificate_meaning'].values[0]
            director4 = d4['director'].values[0]
            stars4 = d4['stars'].values[0]
            time4 = d4['time'].values[0]
            description4 = d4['description'].values[0]
            genre4 = d4['genre'].values[0]
            
            success = [image1, movie1, genre1, str(rating1), stars1, director1, str(time1), description1, certificate1,
                       certificate_meaning1, str(metascore1), str(gross1), str(votes1), imdb_link1, image2, movie2, genre2,
                       str(rating2), stars2, director2, str(time2), description2, certificate2, certificate_meaning2,
                       str(metascore2), str(gross2), str(votes2), imdb_link2, image3, movie3, genre3, str(rating3), stars3,
                       director3, str(time3), description3, certificate3, certificate_meaning3, str(metascore3),
                       str(gross3), str(votes3), imdb_link3, image4, movie4, genre4, str(rating4), stars4, director4,
                       str(time4), description4, certificate4, certificate_meaning4, str(metascore4), str(gross4),
                       str(votes4), imdb_link4, 'second']
            print(success)
            success = dumps(success)
            
            return HttpResponse(success)



























        except:
            
            genre=genre.replace('&','')
            genre=genre.replace('gen=',' ')
            genre=genre[1:].split(' ')
            

            df = pd.DataFrame(list(details.objects.filter(status='Movie').values()))
            for gen in genre:
                df=df[df[gen]==1]

            nums=random.sample(range(0,len(df)-1),4)
            

            d1=df.iloc[nums[0],:]
            # store the id for the image scraping
            id1 = d1['id']

            # store the imdb link for showing in web page and opening the imdb page in web scraping
            imdb_link1 = d1['imdb_link']
            # calling the image function from scrap and passing id and imdblink
            image1 = image(id1, imdb_link1)
            # store the movie name of movie 1

            movie1 = d1['movie_name']
            # store the rating of movie 1
            rating1 = d1['rating']
            # store the gross of movie 1
            gross1 = d1['gross']
            # store the votes of movie 1
            votes1 = d1['votes']
            # store the metascore of movie 1
            metascore1 = d1['metascore']
            # store the certificate of movie 1
            certificate1 = d1['certificate']
            # store the certificate meaning of movie 1
            certificate_meaning1 = d1['certificate_meaning']
            # store the director of movie 1
            director1 = d1['director']
            # store the stars of movie 1
            stars1 = d1['stars']
            # store the time of movie 1
            time1 = d1['time']
            # store the description of movie 1
            description1 = d1['description']
            # store the genre of movie 1
            genre1 = d1['genre']

            d2 = df.iloc[nums[1],:]
            # same process as 1st movie
            id2 = d2['id']
            imdb_link2 = d2['imdb_link']
            image2 = image(id2, imdb_link2)
            movie2 = d2['movie_name']
            rating2 = d2['rating']
            gross2 = d2['gross']
            votes2 = d2['votes']
            metascore2 = d2['metascore']
            certificate2 = d2['certificate']
            certificate_meaning2 = d2['certificate_meaning']
            director2 = d2['director']
            stars2 = d2['stars']
            time2 = d2['time']
            description2 = d2['description']
            genre2 = d2['genre']

            d3=df.iloc[nums[2], :]
            id3 = d3['id']
            imdb_link3 = d3['imdb_link']
            image3 = image(id3, imdb_link3)
            movie3 = d3['movie_name']
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

            # the 4th movie
            d4 = df.iloc[nums[3], :]
            id4 = d4['id']
            imdb_link4 = d4['imdb_link']
            image4 = image(id4, imdb_link4)
            movie4 = d4['movie_name']
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


            success = [image1, movie1, genre1, str(rating1), stars1, director1, str(time1), description1, certificate1,
                       certificate_meaning1, str(metascore1), str(gross1), str(votes1),imdb_link1,image2,movie2,genre2,str(rating2),stars2,director2,str(time2),description2,certificate2,certificate_meaning2,str(metascore2),str(gross2),str(votes2),imdb_link2,image3,movie3,genre3,str(rating3),stars3,director3,str(time3),description3,certificate3,certificate_meaning3,str(metascore3),str(gross3),str(votes3),imdb_link3,image4,movie4,genre4,str(rating4),stars4,director4,str(time4),description4,certificate4,certificate_meaning4,str(metascore4),str(gross4),str(votes4),imdb_link4,'first']
            success = dumps(success)
            return HttpResponse(success)
    return render(request,'survey.html')

