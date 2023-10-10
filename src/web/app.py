import streamlit as st

from src.preprocess.preprocess import preprocess
from src.agent.dataframe_agent import DataFrameAgent


DATA_DIR = "data/techsauce_companies.csv"
data = preprocess(DATA_DIR)
agent = DataFrameAgent(data=data)


def main():
    st.title("Company-Startup Interaction Query System")

    st.sidebar.header("Query Input")
    st.sidebar.write("Enter your question below:")
    user_input = st.sidebar.text_input(
        "", "What startups did company A meet with on August 16?"
    )

    if user_input:
        answer = agent.answer(user_input)
        st.write("### Answer:")
        st.write(answer)


if __name__ == "__main__":
    main()
