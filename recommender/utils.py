import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import os
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import plotly.offline as plt1

draft_template = go.layout.Template()
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


def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(data,g,y):
    bar = data["first_name"].value_counts()[1:16]
    fig = px.bar(bar,
       x = bar.index,
       y = bar.values,
       title="<b> Top 15 Stars Acted in movie in {} genre, {} year</b>".format(g, y),
       text_auto='.2s',
       color = "first_name",
       width=800,
       height=600,
       )
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

def get_plot1(d):
    mask=np.array(Image.open(r'E:\movies\wordlogo.png'))
    wc = WordCloud(mask=mask,min_font_size=10, background_color='black',contour_color='white', contour_width=10, colormap='Paired',width=mask.shape[1],height=mask.shape[0],random_state=42)
    df_wc = wc.generate(d['director'].str.cat(sep=' '))
    figx=plt.figure()
    figx.patch.set_facecolor('black')
    plt.imshow(df_wc,interpolation='None')
    plt.axis('off')
    plt.tight_layout()
    graph=get_graph()
    return graph



def get_plot2(data,g,y):
    fig = px.histogram(data, x = "certificate", title="<b> Year wise Certificates (HistPlot with Boxplot)\t <total count : {}> </b>".format(len(data)), marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
    fig.update_layout(template = draft_template, paper_bgcolor = "black")
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt


def status(df,g,y):
    pie = df["status"].value_counts()
    fig = go.Figure(data=[go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole = 0.3, title = "<b> MYN </b>")])
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(title="<b> Tv-Shows in {} year and {} genre </b>".format(y, g), height=450, width=450, paper_bgcolor = "black")
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        xaxis_title="Name of Stars",
        yaxis_title="Total no of Movies"
    )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt






def time(data,g, y):
    rg = data.groupby("start_year")["rating"].mean().reset_index()
    fig = px.scatter(rg, x="start_year", y="rating", color="start_year", size='rating')
    fig.update_layout(template = draft_template, paper_bgcolor = "black", title="<b> Avarage Rating of Movies in {} year, {} Genre </b>".format(y,g))
    fig.update_layout(
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white"
    )
    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt
def line_time(data,g,y):
    line = data.groupby("start_year")["time"].agg("sum").reset_index()
    if y=='all':
        fig = px.line(line, x="start_year", y="time")
        fig.update_layout(template = draft_template, paper_bgcolor = "black", title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g))
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )
    else:
        fig = px.bar(line, x="start_year", y="time")
        fig.update_layout(template=draft_template, paper_bgcolor="black",
                          title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g))
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )

    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt

