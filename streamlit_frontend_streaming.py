import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot

configuration = {"configurable": {"thread_id": "1"}}

user_input = st.chat_input("Type here")

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


# loading the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])


if user_input:

    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, matadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=configuration,
                stream_mode="messages"
            )
        )

    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
