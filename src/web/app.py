import streamlit as st
import pandas as pd

from src.preprocess.preprocess import preprocess
from src.agent.dataframe_agent import DataFrameAgent

DATA_DIR = "data/techsauce_companies.csv"
data = pd.read_csv(DATA_DIR)
data = preprocess(data)
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
    st.write("Enter your question below:", className="big-font")

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
