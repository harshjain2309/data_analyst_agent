from langchain_together import Together
from dotenv import load_dotenv
import os

load_dotenv()

llm = Together(
    model=os.getenv("TOGETHER_MODEL"),  # should be: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
    temperature=0.3,
    max_tokens=100,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

response = llm.invoke("What is the capital of France?")
print(response)