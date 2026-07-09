import streamlit as st
from agentic_chatbot_backend import chatbot
from langchain_core.messages import HumanMessage, BaseMessage

CONFIG = {
    "configurable": {
        "thread_id": "thread_1",
    }
}

st.title("Agentic AI with Langgraph")

user_input = st.chat_input("Enter your message:", key="user_input")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content
    with st.chat_message("assistant"):
     st.text(ai_message)