import streamlit as st
from utils import process
import os
import google.generativeai as genai

def main():
    # Streamlit page configuration
    st.set_page_config(page_title="QuestAI",
                        page_icon="🔍",
                        layout='centered',
                        initial_sidebar_state='collapsed')

    # Header
    st.header("QuestAI: Your Smart Search Companion 🔎")

    # Input for Google API key with secure input
    key = st.text_input("Enter your Google API key", type="password")

    # Input for app link
    input_text = st.text_input("Enter Your Query")

    # Button to analyze the app
    submit = st.button("Search")

    # API key validation and model setup
    if key:
        try:
            genai.configure(api_key=key)
            gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        except Exception as e:
            st.error("An error occurred.")
    else:
        gemini_model=None

    # Analyze the app link
    if submit:
        if input_text:
            if key:
                try:
                    with st.spinner('Searching...'):
                        result = process.process_query(input_text, gemini_model)
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error searching: {str(e)}")
            else:
                st.warning("Please enter Google API key.")
        else:
            st.error("Please enter a valid query.")

if __name__ == "__main__":
    main()
