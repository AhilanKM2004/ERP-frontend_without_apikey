import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = (st.secrets.get("GROQ_API_KEY"))

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing")
    print("GROQ_API_KEY exists:", "GROQ_API_KEY" in os.environ)
    print("GROQ_API_KEY value :", os.getenv("GROQ_API_KEY"))
    st.stop()
    
print("GROQ_API_KEY exists:", "GROQ_API_KEY" in os.environ)
print("GROQ_API_KEY value :", os.getenv("GROQ_API_KEY"))
client = Groq(api_key=GROQ_API_KEY)
