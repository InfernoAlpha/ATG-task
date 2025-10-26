from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from typing import List
from langchain_core.messages import BaseMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen3-4B-Instruct-2507",task="text-generation")
model = ChatHuggingFace(llm = llm)

def agent_msg(lst:List[BaseMessage]):
    return AIMessage(model.invoke(lst).content)