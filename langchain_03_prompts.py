from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv
load_dotenv()

# Initialize the model
llm = ChatGroq(model = "llama-3.3-70b-versatile", temperature = 0)

#prompt template
prompt = PromptTemplate.from_template("tell me 5 interesting facts about {topic}")
output_parser = StrOutputParser()

# chain
chain = prompt | llm | output_parser
# Invoke
# resp = chain.invoke({"topic": "Titanic"})
# print(resp)

# Chatprompttemplate
prompt2 = ChatPromptTemplate.from_messages([
    ("system","You are a helpful cooking assistant. you teaches recipies in Gen Z terms"),
    ("human", "{topic}")
])
# chain
chain2 = prompt2 | llm | output_parser 
# resp2 = chain2.invoke({"topic": "Biryani"})
# print(resp2)

# FewShotPromptTemplate
examples = [
    {"input": "Vizag", "output": "City of Destiny"},
    {"input": "Hyderabad", "output": "Biryani City"},
    {"input": "Amaravathi", "output": "Capital City"},
    {"input": "Guntur", "output": "City of Chillis"}
]
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt = example_prompt,
    examples = examples,
)
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that gives nicknames to cities."),
    few_shot_prompt,
    ("human", "{input}")
]
)

# Chain
few_shot_chain = final_prompt | llm | output_parser

resp_fsc = few_shot_chain.invoke({"input": "DUBAI"})
print(resp_fsc)