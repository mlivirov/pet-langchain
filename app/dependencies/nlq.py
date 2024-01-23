import os
from time import sleep
from typing import List, Optional, Any

from langchain.agents import AgentType, AgentExecutor
from langchain_community.agent_toolkits import SQLDatabaseToolkit, create_sql_agent
from langchain_community.chat_models import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatResult


# throttle requests
class MyChatOpenAI(ChatOpenAI):
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        stream: Optional[bool] = None,
        **kwargs: Any,
    ) -> ChatResult:
        sleep(10)
        return super()._generate(messages, stop, run_manager, stream, **kwargs)


class NlqAgent:
    def __init__(self, agent: AgentExecutor):
        self.agent = agent

    def prompt(self, body: str):
        return self.agent.run(body)


def nql_agent_factory() -> NlqAgent:
    model = MyChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo-16k-0613",
        temperature=0.5,
    )

    db = SQLDatabase.from_uri(os.getenv("DATABASE_URI"))
    toolkit = SQLDatabaseToolkit(db=db, llm=model)

    agent = create_sql_agent(
        llm=model,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )

    return NlqAgent(agent)
