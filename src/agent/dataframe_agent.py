import os

from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

from dotenv import load_dotenv

ENV_PATH = "env/openai_key"
load_dotenv(dotenv_path=ENV_PATH)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")


class DataFrameAgent:
    def __init__(
        self,
        data,
        model="gpt-3.5-turbo",
        temperature=0,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        **kwargs
    ):
        self._model = model
        self._temperature = temperature
        self.agent = create_pandas_dataframe_agent(
            ChatOpenAI(model=model, temperature=temperature),
            df=data,
            verbose=verbose,
            agent_type=agent_type,
            **kwargs
        )
        self.agent_kwargs = kwargs

    def answer(self, question: str):
        return self.agent.run(question)


if __name__ == '__main__':
    pass
