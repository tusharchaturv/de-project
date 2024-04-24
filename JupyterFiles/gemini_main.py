import streamlit as st
from streamlit_option_menu import option_menu
import os
from gemini_utility import load_gemini_pro_model
import os



# Setting the page configuration
st.set_page_config(
    page_title="Gemini AI",
    layout="centered"
)

# Sidebar options
with st.sidebar:
    # Using option_menu for selecting AI mode
    selected = option_menu("Gemini AI",
                           ["ChatBot",
                            ],
                           menu_icon='robot',
                           icons=['chat-dots-fill',
                                  ],
                           default_index=0)

# Function to translate roles
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role

# Checking the selected mode
if selected == "ChatBot":  # Corrected the capitalization
    model = load_gemini_pro_model()

    # Checking if chat session exists in session state
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])  # Passing an empty history

    # Title for the ChatBot section
    st.title("ChatBot")

    # Displaying chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input for user prompt
    user_prompt = st.chat_input("Ask Gemini-Pro")

    # Checking if user has inputted something
    if user_prompt:
        # Displaying user prompt
        st.chat_message("user").markdown(user_prompt)

        # Sending user prompt to Gemini and displaying the response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
