#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

# Reference
# https://docs.kanaries.net/topics/Streamlit/streamlit-upload-file
# https://docs.streamlit.io/develop/api-reference/layout/st.columns
# https://docs.streamlit.io/develop/api-reference/navigation/st.navigation

st.set_page_config(layout="wide")
st.title("SWIFT Payment ISO 20022 Toolbox v1.0")

# Sidebar for navigation
page = st.sidebar.radio(
    "Select a page",
    ("CSV Upload", "XML Upload")
)

if page == "CSV Upload":
    st.header("CSV File Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, sep=';')
        data_transpose = data.transpose()
        st.write(data_transpose)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

elif page == "XML Upload":
    st.header("XML File Upload")
    uploaded_xml = st.file_uploader("Upload an XML file", type=['xml'])
    if uploaded_xml is not None:
        st.write(f"Uploaded file name: {uploaded_xml.name}")
        # TODO: Add XML parsing/processing code here as needed

st.sidebar.markdown("---")
st.sidebar.info("You can hide this sidebar using the arrow above.")


