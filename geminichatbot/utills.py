import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = ""

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Store conversation history
chat_history = []

def Load_Model(modelname: str) -> genai.GenerativeModel:
    try:
        model = genai.GenerativeModel(modelname)
        return model
    except Exception as e:
        raise e

def generate_response(prompt: str, model: genai.GenerativeModel) -> str:
    try:
        # Combine chat history with the new prompt
        history_text = "\n".join(chat_history)
        full_prompt = f"{history_text}\nUser: {prompt}\nAI:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        # Store user prompt and AI response in history
        chat_history.append(f"User: {prompt}")
        chat_history.append(f"AI: {response.text}")

        return response.text
    except Exception as e:
        raise e
