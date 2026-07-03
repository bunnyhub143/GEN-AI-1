from time import process_time_os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
model=init_chat_model("llama-3.1-8b-instant",model_provider="groq",temperature=0)
print(type(model).__name__)

#invoke to start the model
resp=model.invoke("What is the capital of india ?")
print(resp.content)



#batch invoke
batch_reso=model.batch(["What is the capital of india ?","What is the capital of telangana ?"])
for resp in batch_resp:
    print(resp.content)