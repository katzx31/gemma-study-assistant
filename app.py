import streamlit as st
import ollama

st.set_page_config(page_title="Gemma Study Buddy", page_icon="💡")
st.title("💡 Gemma 2: Offline Study & Code Assistant")
st.caption("Powered by Google Gemma 2B & Ollama (Running 100% locally)")

mode = st.sidebar.selectbox(
    "Choose Assistant Mode",
    ["Code Explainer & Reviewer", "Exam Study Buddy", "General Q&A"]
)

system_prompts = {
    "Code Explainer & Reviewer": "You are an expert developer. Review the user's code, explain bugs simply, and suggest cleaner solutions.",
    "Exam Study Buddy": "You are a patient academic tutor. Explain complex concepts in simple terms, provide quick examples, and quiz the student.",
    "General Q&A": "You are a helpful, concise AI assistant."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question or paste code..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    messages_payload = [{"role": "system", "content": system_prompts[mode]}]
    messages_payload.extend(st.session_state.messages)

    with st.chat_message("assistant"):
        response_box = st.empty()
        full_response = ""
        
        response_stream = ollama.chat(
            model="gemma2:2b",
            messages=messages_payload,
            stream=True
        )
        
        for chunk in response_stream:
            full_response += chunk["message"]["content"]
            response_box.markdown(full_response + "▌")
            
        response_box.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})