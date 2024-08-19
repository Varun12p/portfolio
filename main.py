import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1 , col2 = st.columns(2)

with col1:
    st.image("images/myphoto.png.jpg")

with col2:
    st.title("Varun Panjwani.")
    content = ("Hi, my name is Varun Panjwani. I am new python developer, learning how to create"
               "a web page. ")
    st.info(content)

information = """Below are all the apps I have developed and you can also find the links to
it. I am also writing a brief description of my apps."""
st.write(information)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source link]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source link]({row['url']})")
