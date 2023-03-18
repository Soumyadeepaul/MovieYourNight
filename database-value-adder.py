import mysql.connector
import pandas as pd
dataBase=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='Soumyadeep@7',
    database='movies'  #step after creating database
)
cursor=dataBase.cursor()
#cursor.execute('CREATE DATABASE MOVIES')
cursor.execute('ALTER TABLE recommender_details AUTO_INCREMENT=1')
df=pd.read_csv(r'C:\Users\Lenovo\Cleaned_with_genre.csv')
for i,j in df.iterrows():
    print(j[0])
    sql="INSERT INTO recommender_details (imdb_link, image_link, rating, metascore, description, votes, movie_name, start_year, end_year, gross, certificate, time, genre, director, stars, status, certificate_meaning,comedy, sci_fi, horror, romance, action, thriller, drama, mystery, crime, animation, adventure, fantasy, family, biography, docum, film_noir, history, music, musical, short, sport,superhero, war, western, tag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41], j[42], j[43])
    cursor.execute(sql,val)


dataBase.commit()
