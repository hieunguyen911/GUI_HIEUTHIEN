from streamlit_echarts import st_echarts
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from streamlit_star_rating import st_star_rating
import warnings
warnings.filterwarnings('ignore', message="Error kìa")
st.set_page_config(layout="wide")
#1 read data
data=pd.read_csv("data.csv", encoding='utf-8')
data_res=st.session_state.data_res
id_res=st.session_state.idRes

#2 process data
df_comment= data[data["IDRestaurant"]==id_res]
df_rating=df_comment.groupby('Rating').value_counts()
score= df_comment['score'].value_counts()
try:
    st.write("Positive/Negative: ", score[1], '/', score[0])
    if (score[1]!=0) and (score[0]!=0):
        p_n=round(score[1]/(score[0]+score[1])*100,2)
    else:
        p_n=0
except:
    p_n=0

   
def res_item(name,address,rating,count):
    st.write("#### "+name)
    star=st_star_rating(label="Rating",maxValue=10, defaultValue=rating,size=20)
    st.write(star)
    st.write("###### Số lượt rating : "+str(count))
    st.write("###### Địa chỉ: "+ address) 
r=data_res[data_res["ID"]==id_res].iloc[0].to_list()

#GUI
col1, col2  =st.columns(2)
with col1:
    res_item(name=r[1],address=r[2],count=r[9],rating=r[8])
with col2:
    option = {
        "tooltip": {
            "formatter": '{a} <br/>{b} : {c}%'
        },
        "series": [{
            "name": 'Progress',
            "type": 'gauge',
            "startAngle": 180,
            "endAngle": 0,
            "progress": {
                "show": "true"
            },
            "radius":'100%', 

            "itemStyle": {
                "color": '#58D9F9',
                "shadowColor": 'rgba(0,138,255,0.45)',
                "shadowBlur": 10,
                "shadowOffsetX": 2,
                "shadowOffsetY": 2,
                "radius": '55%',
            },
            "progress": {
                "show": "true",
                "roundCap": "true",
                "width": 15
            },
            "pointer": {
                "length": '60%',
                "width": 8,
                "offsetCenter": [0, '5%']
            },
            "detail": {
                "valueAnimation": "true",
                "formatter": '{value}%',
                "backgroundColor": '#58D9F9',
                "borderColor": '#999',
                "borderWidth": 4,
                "width": '60%',
                "lineHeight": 20,
                "height": 20,
                "borderRadius": 188,
                "offsetCenter": [0, '45%'],
                "valueAnimation": "true",
            },
            "data": [{
                "value": p_n,
                "name": 'Mức độ hài lòng'
            }]
        }]
    };
    st.write(st_echarts(options=option))
col1, col2  =st.columns(2)
with col1:
    st.write("""#### Số lượt comment theo thời gian""") 
    fig, ax = plt.subplots(figsize = (10, 3))
    ax.hist(df_comment['Time_Y'], bins=100)
    plt.yticks(range(0, 50, 10))
    plt.title('Distribution of Comment over Year')
    plt.xlabel('Year')
    st.pyplot(fig)
with col2:
    st.write("""#### Số lượt Rating""") 
    bins = np.arange(0, 11, 1)  # Creates bins [0, 1, 2, ..., 10]
    labels = [f'{i} to {i+1}' for i in range(10)]
    df_comment['RatingGroup'] = pd.cut(df_comment['Rating'], bins=bins, labels=labels, right=False)
    df_comment.groupby('RatingGroup')['RatingGroup'].count().plot(kind='bar')
    st.pyplot(fig)