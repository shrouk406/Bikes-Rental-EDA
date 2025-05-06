
import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout = 'wide', page_title = 'Bikes Rental EDA')

st.write('# Welcome To the Analysis of the Bikes Rental Dataset!')

st.image('https://miro.medium.com/v2/resize:fit:793/0*9AfBNIW4lnK_7wOt.jpg')

df = pd.read_csv('cleaned.csv', index_col= 0)
st.dataframe(df.head(4))

page = st.sidebar.selectbox('Analysis category', ['Univariate Analysis', 'Bivariate Analysis', 'Multivariate'])

if page == 'Univariate Analysis':

    col = st.selectbox('Select Column', df.columns)
    
    chart = st.selectbox('Select Chart', ['Histogram', 'Box', 'Pie'])

    if chart == 'Histogram':
        st.plotly_chart(px.histogram(df, x = col, title= col))

    elif chart == 'Box':
        st.plotly_chart(px.box(data_frame= df, x= col, title= col))

    elif chart == 'Pie':
        st.plotly_chart(px.pie(data_frame= df, names= col, title= col))
    

    st.write('# Some Analysis Questions to check!')

    st.header('Q1: What is the distribution of daily bike rentals (count)?')  
    st.plotly_chart(px.histogram(data_frame= df, x = 'rented_bikes_count'))
    
    st.header('Q2: Which season has the highest number of bike rentals?')  
    st.plotly_chart(px.pie(data_frame= df, names = 'season'))

    st.header('Q3:  How many rentals occur on working days vs. weekends? ')  
    st.plotly_chart(px.pie(data_frame= df, names = 'workingday'))

    st.header('Q4: What is the distribution of tempreture?')  
    st.plotly_chart(px.histogram(data_frame= df, x = 'temp'))
#


elif page == 'Bivariate Analysis':


    col_1 = st.selectbox('Select the first Column', df.columns)
    col_2 = st.selectbox('Select the second Column', df.columns)

    chart = st.selectbox('Select Chart', ['Scatter', 'Box', 'Bar'])

    if chart == 'Scatter':
        st.plotly_chart(px.scatter(df, x = col_1, y = col_2))

    elif chart == 'Box':
        st.plotly_chart(px.box(df, x = col_1, y = col_2))

    elif chart == 'Bar':
        st.plotly_chart(px.bar(df, x = col_1, y = col_2))    


    st.write('# Some Analysis Questions to check!')

    st.header('Q1: Is there a correlation between temperature and rental count?')  
    st.plotly_chart(px.scatter(df, x = 'temp', y = 'rented_bikes_count'))
    

    st.header('Q2: Do people rent more bikes on working days or non-working days?')  
    st.plotly_chart(px.scatter(df, x = 'workingday', y = 'rented_bikes_count'))

    st.header('Q3: How do humidity levels impact rental count? ')  
    st.plotly_chart(px.scatter(df, x = 'humidity', y = 'rented_bikes_count'))

    st.header('Q4: What is the average count for each day of the week?')  
    st.plotly_chart(px.scatter(df, x = 'day name', y = 'rented_bikes_count'))
    

elif page == 'Multivariate':
    
    st.header('Q1: Show The correlation between all columns with the bike rental')  
    correlation = df.corr(numeric_only= True)
    fig, ax = plt.subplots()
    sns.heatmap(correlation, ax=ax)
    st.pyplot(fig)

    st.header('Q2: How does temperature and humidity together impact rental count?')
    st.plotly_chart(px.scatter(df, x = 'humidity', y = 'temp'))
