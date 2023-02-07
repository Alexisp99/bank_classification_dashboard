import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit_nested_layout

#create the page of the web app
st.set_page_config(page_title = "Training",
                   layout = "wide", 
                   )
df = pd.read_csv("data.csv")


all_for_country, Kenya, Rwanda, Tanzania, Uganda = st.tabs(["all 4 country","Kenya","Rwanda","Tanzania", "Uganda"])

with all_for_country:
    col1,col2 = st.columns([1,1])
    
    with col1 :
        st.header("Open account per education level")
        st.write(px.histogram(df,x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.header("Open account per job type")
        st.write(px.histogram(df,x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.header("Open account per gender")
        st.write(px.histogram(df,x = "bank_account",color = "gender_of_respondent",barmode = "group",histnorm='percent'))
    
with Kenya :
    col1,col2 = st.columns([1,1])
    with col1 :
        st.header("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.header("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.header("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))

with Rwanda :
    col1,col2 = st.columns([1,1])
    with col1 :
        st.header("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.header("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.header("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))

with Tanzania :
    col1,col2 = st.columns([1,1])
    with col1 :
        st.header("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.header("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.header("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))

with Uganda :
    col1,col2 = st.columns([1,1])
    with col1 :
        st.header("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.header("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.header("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))