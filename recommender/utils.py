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

def get_plot(rg,g,y):
    if g == 'all' and y == 'all':
        bar = rg["first_name"].value_counts()[1:16]
        fig = px.bar(bar,
               x = bar.index,
               y = bar.values,
               title="<b> Top 15 Stars Acted in movie in All genre, All Year </b>",
               color_discrete_sequence=["#de5216"],
               color = "first_name",
               )
        fig.update_layout(template = draft_template, paper_bgcolor = "black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            xaxis_title="Name of Stars",
            yaxis_title="Total no of Movies",
            autosize=False,
            width=800,
            height=500
        )

    elif g == "all" and y != "all":
        data = rg[rg["start_year"] == y]
        bar = data["first_name"].value_counts()[1:16]
        fig = px.bar(bar,
               x = bar.index,
               y = bar.values,
               title="<b> Top 15 Stars Acted in movie in All genre, Year - {} </b>".format(y),
               color_discrete_sequence=["#AB63FA"],
               color = "first_name"
               )
        fig.update_layout(template = draft_template, paper_bgcolor = "black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            xaxis_title="Name of Stars",
            yaxis_title="Total no of Movies",
            width = 800,
            height = 500
        )

    elif g != "all" and y == "all":
        data = rg[rg[g] == 1]
        bar = data["first_name"].value_counts()[1:16]
        fig = px.bar(bar,
               x = bar.index,
               y = bar.values,
               title="<b> Top 15 Stars Acted in movie in {} genre, All Year </b>".format(g),
               color_discrete_sequence=["#AB63FA"],
               color = "first_name"
               )
        fig.update_layout(template = draft_template, paper_bgcolor = "black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            xaxis_title="Name of Stars",
            yaxis_title="Total no of Movies",
            width=800,
            height=500
        )

    else:
        data = rg[rg["start_year"] == y]
        data = data[data[g] == 1]
        bar = data["first_name"].value_counts()[1:16]
        fig = px.bar(bar,
                     x=bar.index,
                     y=bar.values,
                     title="<b> Top 15 Stars Acted in movie in {} genre, {} Year </b>".format(g, y),
                     color_discrete_sequence=["#AB63FA"],
                     color="first_name",

                     )
        fig.update_layout(template=draft_template, paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            xaxis_title="Name of Stars",
            yaxis_title="Total no of Movies",
            width=800,
            height=500
        )

    gantt_plt = plt1.plot(fig, output_type='div')
    return gantt_plt

def get_plot1(d,g,y):
    mask=np.array(Image.open(r'E:\movies\wordlogo.png'))
    wc = WordCloud(mask=mask,min_font_size=10, background_color='black',contour_color='white', contour_width=10, colormap='Paired',width=mask.shape[1],height=mask.shape[0],random_state=42)
    if g == 'all' and y == 'all':
        df_wc = wc.generate(d['director'].str.cat(sep=' '))
    elif g == "all" and y != "all":
        d = d[d["start_year"] == y]
        df_wc = wc.generate(d['director'].str.cat(sep=' '))
    elif g != "all" and y == "all":
        d= d[d[g] == 1]
        df_wc = wc.generate(d['director'].str.cat(sep=' '))
    else:
        d = d[d["start_year"] == y]
        d = d[d[g] == 1]
        df_wc = wc.generate(d['director'].str.cat(sep=' '))
    figx=plt.figure()
    figx.patch.set_facecolor('black')
    plt.imshow(df_wc,interpolation='None')
    plt.axis('off')
    plt.tight_layout()
    graph=get_graph()
    return graph



def get_plot2(rg,g,y):

    if g == "all" and y == "all":
        #plt.figure(figsize=(5, 6))
        data = rg[rg["certificate"] != "Not Certified"]
        data = data[data["certificate"] != "Not Rated"]
        fig = px.histogram(data, x="certificate",
                           title="<b> Year wise Certificates (HistPlot with Boxplot) [total count : {}] </b>".format(
                               len(data)), marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
        fig.update_layout(template=draft_template, paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )


    elif g == "all" and y != "all":
        #plt.figure(figsize=(5, 6))
        data = rg[rg["start_year"] == y]
        data = data[data["certificate"] != "Not Certified"]
        data = data[data["certificate"] != "Not Rated"]
        fig = px.histogram(data, x="certificate",
                           title="<b> Year wise Certificates (HistPlot with Boxplot)\t <total count : {}> </b>".format(
                               len(data)), color="start_year", marginal="box", template="ggplot2",
                           color_discrete_sequence=["#AB63FA"])
        fig.update_layout(template=draft_template, paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )

    elif g != "all" and y == "all":
        #plt.figure(figsize=(5, 6))
        data = rg[rg[g] == 1]
        data = data[data["certificate"] != "Not Certified"]
        data = data[data["certificate"] != "Not Rated"]
        fig = px.histogram(data, x="certificate",
                           title="<b> Year wise Certificates (HistPlot with Boxplot)\t <{} count : {}> </b>".format(
                               g, len(data)), color="start_year", marginal="box", template="ggplot2",
                           color_discrete_sequence=["#AB63FA"])
        fig.update_layout(template=draft_template, paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )

    else:
        #plt.figure(figsize=(5, 6))
        data = rg[rg["start_year"] == y]
        data = data[data[g] == 1]
        data = data[data["certificate"] != "Not Certified"]
        data = data[data["certificate"] != "Not Rated"]
        fig = px.histogram(data, x="certificate",
                           title="<b> Year wise Certificates (HistPlot with Boxplot)\t <{} count : {}> </b>".format(
                               g, len(data)), color="start_year", marginal="box", template="ggplot2",
                           color_discrete_sequence=["#AB63FA"])
        fig.update_layout(template=draft_template, paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt


def status(d,g,y):
    if g == "all" and y == "all":
        pie = d["status"].value_counts()
        fig = go.Figure(data=[
            go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole=0.3, title="<b>MYN</b>")])
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(title="<b> M/S in All year </b>", height=450, width=450)
        fig.update_layout(paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )



    elif g == "all" and y != "all" and y != 0:
        rg = d[d["start_year"] == y]
        pie = rg["status"].value_counts()
        fig = go.Figure(
            data=[go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole=0.3, title="<b>MYN</b>")])
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(title="<b> M/S in {} year </b>".format(y), height=450, width=450)
        fig.update_layout(paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )


    elif g != "all" and y != "all" and y != 0:
        d = d[d[g] == 1]
        rg = d[d["start_year"] == y]
        pie = rg["status"].value_counts()
        fig = go.Figure(
            data=[go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole=0.3, title="<b>MYN</b>")])
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(title="<b> M/S in {} genre {} year </b>".format(g,y), height=450, width=450)
        fig.update_layout(paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )
    elif g != "all" and y == "all":
        rg = d[d[g] == 1]
        pie = rg["status"].value_counts()
        fig = go.Figure(
            data=[go.Pie(labels=pie.index, values=pie, pull=[0, 0.2], hole=0.3, title="<b>MYN</b>")])
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(title="<b> M/S in {} genre </b>".format(g), height=450, width=450)
        fig.update_layout(paper_bgcolor="black")
        fig.update_layout(
            font_color="white",
            title_font_color="white",
            legend_title_font_color="white"
        )
    gantt_plt=plt1.plot(fig,output_type='div')
    return gantt_plt