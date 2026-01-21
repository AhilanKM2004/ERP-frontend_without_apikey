
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = (st.secrets.get("GROQ_API_KEY"))

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
