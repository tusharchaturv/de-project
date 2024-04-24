import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_pro_model():
    gemini_pro_model= genai.GenerativeModel('gemini-pro')
    return gemini_pro_model