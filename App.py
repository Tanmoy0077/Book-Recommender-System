import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def suggest_similar_books(book_name, num):
    similar = sorted(list(enumerate(cosine_similarity(data[data['Title'] == book_name].iloc[:, 1:], data.iloc[:,1:])[0])),key=lambda x:x[1],reverse=True)[1:num+1]
    return [data.iloc[x[0],:]['Title'] for x in similar]


data = pd.read_csv('final_data.csv')

st.header("Book Recommender System")

book_name = st.selectbox(
    'Choose the book you read',
    data['Title'].values)

if st.button("Suggest Book"):
    items = []
    with st.spinner("Please wait ..."):
        items = suggest_similar_books(book_name, 5)
        st.write("You should read :-")
    for name in items:
        st.markdown(f"- {name}")
