import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                base_url= "https://openrouter.ai/api/v1",
                )

messages= [{"role": "system", "content": """Your are general type of friendly chat assistant.
You can give any answer perfect.
You double check every answer."""}] 

def chatbot(prompt: str):

    prm = {"role": "user", "content": prompt}

    messages.append(prm)
    
    chats = client.chat.completions.create(
        model= "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        messages= messages
    )

    reply = chats.choices[0].message.content
    
    messages.append({"role": "assistant", "content": reply})

    return {"message": reply}


####for checking
# while(True):
    
#     prompt = input("User: ")
#     if(prompt == "exit"):
#         break
#     else:
#         print(chatbot(prompt))
