import streamlit as st
from langchain_code import get_qa_chain

st.set_page_config(page_title="Tesco FAQs", page_icon="🚚")

st.title("🚚Tesco FAQs Chat Bot 🍎🧀🍖")

st.subheader("Question: ")
question = st.text_input("Question: ", label_visibility="hidden", placeholder="Write your question here and press Enter", help="If the answer is 'I don't know', it is because your question is not available in our database. But sometimes reformulating the question will solve the problem.")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.subheader("Answer: ")
    st.write(response["result"])