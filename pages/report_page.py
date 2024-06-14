from streamlit_echarts import st_echarts
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from streamlit_star_rating import st_star_rating
import warnings
warnings.filterwarnings('ignore', message="Error kìa")
st.set_page_config(layout="wide")
data = np.array([10, 15, 7, 20, 13, 15])
st.balloons()
st.write(id_restaurant)
st.button("show", type="primary")
if st.button("show"):
    st.write("Why hello there")
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(data)), data, color='skyblue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Bar Plot of 6 Numbers')
    plt.xticks(range(len(data)), ['A', 'B', 'C', 'D', 'E', 'F'])
    plt.plot()

col1, col2, col3 =st.columns(3)
with col1:
    stars = st_star_rating(label="Rating",maxValue=10, defaultValue=5,size=20,)
    st.write(stars)
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
                "value": 50,
                "name": 'Mức độ hài lòng'
            }]
        }]
    };
    st.write(st_echarts(options=option, key="1"))
with col3:
    stars = st_star_rating(label="Rating",maxValue=10, defaultValue=8,size=20)
    st.write(stars)
