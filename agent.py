# agent.py

import os
from langchain.agents import initialize_agent, AgentType
from langchain_together import Together
from tools import tools
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_agent():
    # Initialize LLM from Together API
    llm = Together(
    model=os.getenv("TOGETHER_MODEL"),
    temperature=0.3,
    max_tokens=512,
    together_api_key=os.getenv("TOGETHER_API_KEY")
    )
    # Set up the agent with tools and LLM
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent



def run_agent_question(question: str) -> str:
    try:
        agent = get_agent()
        response = agent.run(question)
        return response
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print("Full error:\n", error_details)
        return f"❌ Error while generating answer:\n{str(e)}"
    


print("Using model:", os.getenv("TOGETHER_MODEL"))
print("Using API key:", os.getenv("TOGETHER_API_KEY")[:6], "********")  # just to check it's loading