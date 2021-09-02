import streamlit as st

#pacotes utilizados
import requests
import numpy as np
from datetime import date
import matplotlib.ticker as ticker
import json
#feito para traduzir o nome dos gráficos 
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator

#import plotly
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from dbnomics import fetch_series, fetch_series_by_api_link

################################ main functions for aplication ############################################################################3
def df_enxuto(df):
    nome = df.series_name.values[1]
    df = df.query("value != 'NaN'")[['period','value']]
    df['period'] = pd.to_datetime(df['period'])
    #df.columns  =  [['date', nome ]]
    df = df.set_index(['period'])
    df =df.rename(columns={'value': nome})
    #df.set_index(['date'], inplace=True)
    #df.index = pd.DatetimeIndex(df.index.values, dtype='datetime64[ns]', name='datetime', freq=None)
    return df


def line_plotly(series):
    
    df  = fetch_series(series)
    print(df)
    nome = df.series_name[1]
    nome_2 = df['Data Element'][1] + '-' + df['Industry'][1]
    #freq = df.FREQUENCY[1]
    df = df_enxuto(df)
    p1_fig = go.Figure()
    colors = ['#E0D253', '#0A3254', '#7AADD4', '#336094', '#B2292E']
    config = dict({'scrollZoom': True,'displayModeBar': False})

    p1_fig.add_trace(go.Scatter(x=df.index, y=df[nome],
                                   fill=None,
                                   mode=None,
                                   line_color='#B2292E'
                                   ))



    p1_fig.update_layout(title={ 'text': '<b>'+nome_2+'<b>','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},
                             title_font_size=14,
                             xaxis_title='Semana',
                             yaxis_title='', 
                             template='plotly_dark',
                             font_family="Verdana", 
                             images=[dict(source='Downloads/stonex.png',
                                 xref="paper", yref="paper",
                                 x=0, y=0,
                                 sizex=0.4, sizey=0.5,
                                 opacity=0.2,
                                 xanchor="center",
                                 yanchor="middle",
                                 sizing="stretch",
                                 layer="below")],
                             legend=dict(
                                 orientation="h",
                                 yanchor="bottom",
                                 y=-0.3,
                                 xanchor="center",
                                 x=0.5,
                                 font_family='Verdana'),
                                 autosize=False, height= 550, width=750
                                 )
                             
    p1_fig.update_xaxes(rangeslider_visible=True)

    
    
    return p1_fig

######################### Streamlit APP


html_header="""<head>
<title>StoneX - Energy </title>
<meta charset="utf-8">
<meta name="keywords" content="Test, visualizer, data">
<meta name="description" content="test Data Project">
<meta name="author" content="@Cober">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#B2292E; font-family:Verdana"> Jolts Visualizer beta<br>
 <h2 style="color:#B2292E; font-family:Verdana"> Testing ploting </h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1px;"></h1>
"""

st.set_page_config(page_title="Teste", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

#determinando os plots
fig =  line_plotly('BLS/jt/JTS000000000000000QUR')
fig1 = line_plotly('BLS/jt/JTS000000000000000QUR')
fig2 = line_plotly('BLS/jt/JTS000000000000000JOR')
fig3 = line_plotly('BLS/jt/JTS000000000000000JOL')
fig4 = line_plotly('BLS/jt/JTS000000000000000HIR')
fig5 = line_plotly('BLS/jt/JTS000000000000000UOR')


### Block 1#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5 = st.beta_columns([1,20,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.plotly_chart(fig)
    with col3:
        st.write("")
    with col4:
        st.plotly_chart(fig1)
    with col5:
         st.write("")


html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

### Block 2#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5 = st.beta_columns([1,20,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.plotly_chart(fig2)
    with col3:
        st.write("")
    with col4:
        st.plotly_chart(fig3)
    with col5:
         st.write("")


html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

### Block 2#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5 = st.beta_columns([1,20,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.plotly_chart(fig4)
    with col3:
        st.write("")
    with col4:
        st.plotly_chart(fig5)
    with col5:
         st.write("")


html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style="color:Gainsboro; text-align: right;">produzido por: @Cober</p>
"""
st.markdown(html_line, unsafe_allow_html=True)