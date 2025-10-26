from agent_model import agent_msg
from langchain_core.messages import HumanMessage
from memory import chat_history

history = chat_history(5)

while True:
    query = HumanMessage(input("Human:"))
    if(query.content == "\\exit"):
        break
    history.add(query)
    reply = agent_msg(history.retrevie())
    print(f"AI:{reply.content}")
    history.add(reply)

print(history.retrevie())