import base64
import os
from google import generativeai as genai
from google.generativeai import types
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

#model configs
generate_content_config = types.GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    top_k=64,
    max_output_tokens=65536,
    response_mime_type="text/plain",
)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generate_content_config,
    system_instruction="You are motivational support speaker. You give the user motivational feedback on how they can achieve their fitness goals by providing a workout and meal plan and a motivational quote.",
)

#functionality to start a chat and append contents
chat_session = model.start_chat(
    history=[]
)

while True:
    user_input=input('Write your question: ')
    print()
    
    response = chat_session.send_message(user_input)
    model_response = response.text
  
    print(model_response)
    print()
    
    chat_session.history.append({'role': 'user', 'parts': [user_input]})
    chat_session.history.append({'role': 'model', 'parts': [model_response]})

    
