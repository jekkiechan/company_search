import streamlit as st
import pandas as pd

from src.preprocess.preprocess import preprocess
from src.agent.dataframe_agent import DataFrameAgent

DATA_DIR = "data/company_database.xlsx"
company = pd.read_excel(DATA_DIR, usecols="B:P", sheet_name="Company")
people = pd.read_excel(DATA_DIR, usecols="B:AB", sheet_name="Person")
data = preprocess(company, people)
agent = DataFrameAgent(data=data)


def main():
    st.title("Company-Startup Interaction Query System")

    st.markdown("""
        <style>
            .reportview-container {
                background-color: #f0f0f5;
                color: #111;
            }
            .big-font {
                font-size:20px !important;
            }
            .text-input {
                width:70%;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header("Query Input")
    st.write("Enter your question below:")

    user_input = st.text_input(
        label="This is a text",
        value=None,
        label_visibility="hidden",
        placeholder="What startups did company A meet with on August 16?",
    )

    if user_input:
        answer = agent.answer(user_input)
        st.write("### Answer:")
        st.write(answer)


if __name__ == "__main__":
    main()
