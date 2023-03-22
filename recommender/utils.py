# Import the Necessary Packages 🤔🤔🤔
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import os
import pandas as pd

# the plotly package used in most of the dashboard visualization 😊😊
import plotly_express as px
import plotly.graph_objects as go
import plotly.offline as plt1

# -------------------------------------------------------------------------------------------

# draft template of all the plots to show the watermark
draft_template = go.layout.Template()
# Take the format of each plotting watermark and layout and will use in each plot
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="MYN",
        textangle=-30,
        opacity=0.5,
        font=dict(color="lightblue", size=50),
        xref="paper",
        yref="paper",
        showarrow=False,
    )
]
global fig1
fig1=go.Figure()

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️
# system task to set the graph
def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# Function to show the barplot of the total stars in a movie
def stars(data,g,y):
    # take the value_count of the top 15 stars in year and genre basis
    bar = data["first_name"].value_counts()[1:16]
    # taking the bar-plot
    fig = px.bar(bar,
       x = bar.index,
       y = bar.values,
       title="<b> Top 15 Stars Acted in movie in {} genre, {} year</b>".format(g, y),
       text_auto='.2s',
       color = "first_name",
       width=800,
       height=600,
       )
    # update the layout and add the watermark
    fig.update_layout(template = draft_template, paper_bgcolor = "black")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        xaxis_title="Name of Stars",
        yaxis_title="Total no of Movies"
    )

    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# the wordcloud to show the frequency of the directors in movies
def wordcloud(d):
    # taking the required format from system
    mask=np.array(Image.open(r'E:\movies\wordlogo.png'))
    # finding the wordcloud
    wc = WordCloud(mask=mask,min_font_size=10, background_color='black',contour_color='white', contour_width=10, colormap='Paired',width=mask.shape[1],height=mask.shape[0],random_state=42)
    df_wc = wc.generate(d['director'].str.cat(sep=' '))
    figx=plt.figure()
    figx.patch.set_facecolor('black')
    plt.imshow(df_wc,interpolation='None')
    plt.axis('off')
    plt.tight_layout()
    graph=get_graph()
    return graph

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# The function to show the histogram of total certificates in movies
def certificate(data,g,y):
    # plotting the histogram
    fig = px.histogram(data, x = "certificate", title="<b> Year wise Certificates (HistPlot with Boxplot)\t <total count : {}> </b>".format(len(data)), marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
    fig.update_layout(template = draft_template, paper_bgcolor = "black")
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# The function to show the pie-plot of the status/tv-shows
def status(df,g,y):
    # taking the values of the tv-shows in 'pie'
    pie = df["status"].value_counts()
    fig = go.Figure(data=[go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole = 0.3, title = "<b> MYN </b>")])
    fig.update_traces(textposition="inside", textinfo="percent+label")
    # updating the layout according to the 'MYN' requirments
    fig.update_layout(title="<b> Tv-Shows in {} year and {} genre </b>".format(y, g), height=450, width=450, paper_bgcolor = "black")
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        xaxis_title="Name of Stars",
        yaxis_title="Total no of Movies"
    )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# The function to show the scatterplot of the avarage rating
def rating(data,g, y):
    # taking the avarage rating of each year in 'rg'
    rg = data.groupby("start_year")["rating"].mean().reset_index()
    # doing the scatterplot
    fig = px.scatter(rg, x="start_year", y="rating", color="start_year", size='rating')
    # altering the layout according to the requiments
    fig.update_layout(template = draft_template, paper_bgcolor = "black", title="<b> Avarage Rating of Movies in {} year, {} Genre </b>".format(y,g))
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt

# 😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊🍿🍿📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️📽️

# The function to show the lineplot of the total time of the movies
def line_time(data,g,y):
    # taking the total time of movies in each year basis
    line = data.groupby("start_year")["time"].agg("sum").reset_index()
    #  some condition to satisfy the requirmrnts
    if y=='all':
        # doing the lineplot
        fig = px.line(line, x="start_year", y="time")
        fig.update_layout(template = draft_template, paper_bgcolor = "black", title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g))
        # altering the layout according to the requiments
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )
    else:
        # otherwise do the barplot
        fig = px.bar(line, x="start_year", y="time")
        fig.update_layout(template=draft_template, paper_bgcolor="black",
                          title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g))
        # altering the layout according to the requiments
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )

    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt


# -----------------------------------------------------------------------------------------------------------------
