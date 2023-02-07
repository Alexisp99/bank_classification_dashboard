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
        st.subheader("Open account per education level")
        st.write(px.histogram(df,x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per job type")
        st.write(px.histogram(df,x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
    with col2 :
        st.subheader("Open account per gender")
        st.write(px.histogram(df,x = "bank_account",color = "gender_of_respondent",barmode = "group",histnorm='percent'))
        st.subheader("Open account per country")
        px.histogram(df,x = "country",color = "bank_account",barmode = "group",histnorm='percent')
        
    
with Kenya :
    st.header("Kenya")
    col1,col2 = st.columns([1,1])
    with col1 :
        st.subheader("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Opean account per age of respondent")
        fig = px.histogram(df.loc[df["country"] == "Kenya"],x = "age_of_respondent",color = "bank_account",barmode = "stack",histnorm='percent')
        fig.update_layout(
        bargap=0.2 )
        st.write(fig)
        
    with col2 :
        st.subheader("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per household size ")
        st.write(px.histogram(df.loc[df["country"] == "Kenya"],x = "household_size",color = "bank_account",barmode = "group",histnorm='percent'))
        
with Rwanda :
    st.header("Rwanda")
    col1,col2 = st.columns([1,1])
    with col1 :
        st.subheader("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Opean account per age of respondent")
        fig = px.histogram(df.loc[df["country"] == "Rwanda"],x = "age_of_respondent",color = "bank_account",barmode = "stack",histnorm='percent')
        fig.update_layout(
        bargap=0.2 )
        st.write(fig)
        
    with col2 :
        st.subheader("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per household size ")
        st.write(px.histogram(df.loc[df["country"] == "Rwanda"],x = "household_size",color = "bank_account",barmode = "group",histnorm='percent'))

with Tanzania :
    st.header("Tanzania")
    col1,col2 = st.columns([1,1])
    with col1 :
        st.subheader("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Opean account per age of respondent")
        fig = px.histogram(df.loc[df["country"] == "Tanzania"],x = "age_of_respondent",color = "bank_account",barmode = "stack",histnorm='percent')
        fig.update_layout(
        bargap=0.2 )
        st.write(fig)
        
    with col2 :
        st.subheader("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per household size ")
        st.write(px.histogram(df.loc[df["country"] == "Tanzania"],x = "household_size",color = "bank_account",barmode = "group",histnorm='percent'))

with Uganda :
    st.header("Uganda")
    col1,col2 = st.columns([1,1])
    with col1 :
        st.subheader("Open account per education level")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "education_level",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per job type")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "job_type",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Opean account per age of respondent")
        fig = px.histogram(df.loc[df["country"] == "Uganda"],x = "age_of_respondent",color = "bank_account",barmode = "stack",histnorm='percent')
        fig.update_layout(
        bargap=0.2 )
        st.write(fig)
    with col2 :
        
        st.subheader("Open account per gender")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "gender_of_respondent",color = "bank_account",barmode = "group",histnorm='percent'))
        st.subheader("Open account per household size ")
        st.write(px.histogram(df.loc[df["country"] == "Uganda"],x = "household_size",color = "bank_account",barmode = "group",histnorm='percent'))