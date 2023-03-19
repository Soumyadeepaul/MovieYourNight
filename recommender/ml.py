from .models import details
import pandas as pd
#Vectorization with 30000 words
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=30000,stop_words='english')
#sklean cosine_similarity is to find the angle between every movies
from sklearn.metrics.pairwise import cosine_similarity
import random

def recommend(y,g,m):
    #get the model details
    df = pd.DataFrame(list(details.objects.all().values()))
    #latest 2022 if all year
    if y==0:
        y='2022'
    #if all genre select specfic one genre
    if g=='all':
        k = ['comedy','romance', 'action', 'thriller','crime','adventure']
        g=random.choice(k)
    #copy the main df
    d = df.copy()
    #filter accorinh to year
    df = df[df['start_year'] == int(y)]
    #filter according to genre
    df = df[df[g] == 1]
    #only movie
    df = df[df['status'] == 'Movie']
    df = df.head(5000)

    df = df.dropna()
    #use tag  column mixed of all important columns
    fit = cv.fit_transform(df['tag']).toarray()
    #angle fit
    similarity = cosine_similarity(fit)

    df=df.reset_index()
    def recommend():
        #random any one
        mi = random.randint(0,len(df))
        #get that specific vectorized array
        dis = similarity[mi]
        #sort acording to the movie name
        mov_lis = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[:20]
        #random 2
        mov_lis = random.sample(mov_lis, 2)
        l = []
        # append in list all the value of both the movies
        for i in mov_lis:
            l.append(df.iloc[i[0]])
        return l
    #calling the function

    l=recommend()
    #get all value of inserted movie name
    stat = d[d['movie_name'] == m]
    mov=stat['status'].tolist()
    cer=stat['certificate'].tolist()
    rat=stat['rating'].tolist()
    #filtering with rating status and certificate
    d=d[(d['rating']==rat[0]) | (d['rating']>=8.5)]
    d=d[d['status']==mov[0]]
    d= d[d['certificate'] == cer[0]]
    #if still more then 8000 filter more
    if len(d)>8000:
        d = d[(d['rating'] == rat[0]) | (d['rating'] >= 9.0)]
    #fit with tag
    fit = cv.fit_transform(d['tag']).toarray()
    #angle of every movie
    similarity = cosine_similarity(fit)
    d=d.reset_index()
    def recommend1(m):
        #get the index of the movie inserted
        mi = d[d['movie_name'] == m].index[0]
        #get the vectorized value
        dis = similarity[mi]
        mov_lis = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[1:21]
        #random 2 from 20
        mov_lis = random.sample(mov_lis, 2)
        #append into the same list
        for i in mov_lis:
            l.append(d.iloc[i[0]])
        return l
    # return the list of 4 elements
    return recommend1(m)
