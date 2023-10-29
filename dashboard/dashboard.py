#import the library 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px 

#import the data
df = pd.read_csv('final_hour_data.csv')

st.set_page_config(page_title="Capital Bikeshare Dashboard",
                   page_icon=":stuck_out_tongue:",
                   layout="wide")
#title
st.header(' :bike: Capital Bikeshare Activites Dashboard :bike:', divider='rainbow')


#--------SIDEBAR---------
with st.sidebar: 
    #logo perusahaan
    st.image("2E-N0B6u_400x400.jpg")
    # st.image("https://github.com/kamandanu9/Dicoding-Bike-Sharing-Project/blob/723fb5860b07a70966eb12abdddf6fe3881b79da/image/2E-N0B6u_400x400.jpg")
    st.write(f'Select `year` as **time filter** for this dashboard')

time_filter = st.sidebar.selectbox(
    label='Select Year',
    options=df['new_yr'].unique()
    # horizontal=False
)


st.sidebar.header('Let\'s connect! ')
st.sidebar.markdown("[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/gakamdanu9/)")
st.sidebar.markdown(':copyright: 2023 made by Gregorius Abiyoso Kamandanu')


total_activites = df.cnt.sum()
st.metric("Total Bike Rent Activites", value=total_activites)

#-------MONTHLY PLOT

monthly_activites_df=df[df['new_yr']==time_filter].groupby('mnth').agg({
    'cnt':'sum'
}).reset_index()

fig = px.line(x=monthly_activites_df['mnth'],
              y=monthly_activites_df['cnt'],
              markers=True,
              title=f"Monthly Bike Rent Activites in {time_filter}").update_layout(xaxis_title='', yaxis_title='Total')

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = np.arange(1,13),
        ticktext = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    )
)


st.plotly_chart(fig, use_container_width=True)

col1,col2 =st.columns(2)
#-----SEASON PLOT
season_activites_df=df[df['new_yr']==time_filter].groupby('new_season').agg({
    'cnt':'sum'
}).reset_index()
 
fig1 = px.bar(x=season_activites_df['new_season'],
              y=season_activites_df['cnt'],
              color=season_activites_df['cnt'], 
              title=f"Season Bike Rent Activites in {time_filter}").update_layout(xaxis_title='', yaxis_title='Total')

#------USER ACTIVITIES PLOT
user_activities_df=pd.DataFrame({
    "category":['casual','registered'],
    "values":[df[df['new_yr']==time_filter].casual.sum(), df[df['new_yr']==time_filter].registered.sum()]
})

fig2 = px.pie(user_activities_df, 
              values='values', 
              names='category',
              title=f"Type of Bike Rent Users  in {time_filter}")
fig2.update_traces(pull=[0.1,0])

col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

#-------DAILY ACTIVITES PLOT

daily_activites_df=df[df['new_yr']==time_filter].groupby('new_weekday').agg({
    'cnt':'sum'
}).reset_index()
 
fig3 = px.line(x=daily_activites_df['new_weekday'],
              y=daily_activites_df['cnt'],
              markers=True,
              title=f"Daily Bike Rent Activites in {time_filter}").update_layout(xaxis_title='', yaxis_title='Total')


#------- HOURLY ACTIVITIES PLOT
hourly_activites_df=df[df['new_yr']==time_filter].groupby('hr').agg({
    'cnt':'sum'
}).reset_index()


fig4 = px.line(x=hourly_activites_df['hr'],
              y=hourly_activites_df['cnt'],
              markers=True,
              title=f"Hourly Bike Rent Activites in {time_filter}").update_layout(xaxis_title='', yaxis_title='Total')

col3, col4 = st.columns(2)

col3.plotly_chart(fig3, use_container_width=True)
col4.plotly_chart(fig4, use_container_width=True)