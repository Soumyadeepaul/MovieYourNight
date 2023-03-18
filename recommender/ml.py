from .models import details
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=30000,stop_words='english')
from sklearn.metrics.pairwise import cosine_similarity
import random


def recommend(y,g,m):
    df = pd.DataFrame(list(details.objects.all().values()))
    print(1)
    if y==0:
        y='2022'
    if g=='all':
        k = ['comedy','romance', 'action', 'thriller','crime','adventure']
        g=random.choice(k)
    print(g)

    d = df.copy()
    df = df[df['start_year'] == int(y)]
    df = df[df[g] == 1]
    df = df[df['status'] == 'Movie']
    df = df.head(1000)

    print(3)
    df = df.dropna()
    print('dsfvsd')
    fit = cv.fit_transform(df['tag']).toarray()
    print(4)
    similarity = cosine_similarity(fit)
    print(5)
    df=df.reset_index()
    print(df)
    def recommend():
        print(len(df))
        mi = random.randint(0,len(df))
        print(mi)
        dis = similarity[mi]
        mov_lis = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[:20]
        mov_lis = random.sample(mov_lis, 2)
        l = []
        for i in mov_lis:
            l.append(df.iloc[i[0]])
        return l
    print(6)
    l=recommend()
    stat = d[d['movie_name'] == m]
    mov=stat['status'].tolist()
    cer=stat['certificate'].tolist()
    rat=stat['rating'].tolist()
    d=d[(d['rating']==rat[0]) | (d['rating']>=8.5)]
    d=d[d['status']==mov[0]]
    d= d[d['certificate'] == cer[0]]
    print(len(d))
    if len(d)>8000:
        d = d[(d['rating'] == rat[0]) | (d['rating'] >= 9.0)]
    print(3)
    print('dsfvsd')
    fit = cv.fit_transform(d['tag']).toarray()
    print(4)
    print(d)
    similarity = cosine_similarity(fit)
    print(5)
    d=d.reset_index()
    def recommend1(m):
        print(m)
        mi = d[d['movie_name'] == m].index[0]
        print(mi)
        dis = similarity[mi]
        mov_lis = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[1:21]
        mov_lis = random.sample(mov_lis, 2)
        for i in mov_lis:
            l.append(d.iloc[i[0]])
        return l
    print(6)
    return recommend1(m)
