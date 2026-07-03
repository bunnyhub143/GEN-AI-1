from dotenv import load_dotenv
load_dotenv()
# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq
# pyrefly: ignore [missing-import]
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatGroq(model = "llama-3.3-70b-versatile", temperature = 0.7)
'''
response = llm.invoke("teach me dynamic programming")
print(response.content)
message1 = [
     SystemMessage(content = "You are a old british programming teacher. Please explain the code in a simple and understandable manner"),
     HumanMessage(content = "teach me dynamic programming"), 
 ]
response1 = llm.invoke(message1)
print(response1.content)
'''
message2 = [
    SystemMessage(content = "You are a GEN Z news reporter, you speak only in gen Z terms. "),
    HumanMessage(content = "tell me about Telugu Titans in Pro Kabbadi"),
    AIMessage(content = "The Telugu Titans are actually low-key popping off this season, fr fr."),
    HumanMessage(content = "give me some solid proofs")
]
response2 = llm.invoke(message2)
print(response2.content)