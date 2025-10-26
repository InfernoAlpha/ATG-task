from langchain_core.messages import BaseMessage,AIMessage,HumanMessage

class chat_history:
    def __init__(self,chat_window_size:int) -> None:
        self.size = chat_window_size*2
        self.lst = []
    def add(self,msg:BaseMessage) -> None:
        l = len(self.lst)
        if l <= self.size:
            self.lst.append(msg)
        else:
            self.lst.pop(0)
            self.lst.append(msg)
    def retrevie(self) -> list:
        return self.lst