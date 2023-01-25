import streamlit as st
import openai
openai.api_key = "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"
from streamlit_chat import message as st_message


def message_bot(prompt):
    user = prompt + '\\nA:'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response["choices"][0]['text']

if "history" not in st.session_state:
    st.session_state.history = []

st.title("How May I Help You?")


def generate_answer():
    user_message = st.session_state.input_text
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot(user_message), "is_user": False})


st.text_input("Talk To Me", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking