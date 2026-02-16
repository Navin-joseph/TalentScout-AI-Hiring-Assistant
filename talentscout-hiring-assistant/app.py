import streamlit as st
from prompts import info_collection_prompt, generate_questions_prompt
from utils import call_llm

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

st.title("🤖 TalentScout Hiring Assistant")
st.markdown("Welcome! I will assist you with the initial screening process.")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "stage" not in st.session_state:
    st.session_state.stage = "collect_info"

if "tech_stack" not in st.session_state:
    st.session_state.tech_stack = None


user_input = st.chat_input("Type your message here...")

if user_input:

    # Exit Condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.chat_history.append(("assistant",
            "Thank you for applying to TalentScout. Our team will review your profile and contact you soon. Have a great day! 👋"))
        st.session_state.stage = "done"
    else:
        st.session_state.chat_history.append(("user", user_input))

    
        if st.session_state.stage == "collect_info":

            prompt = info_collection_prompt(user_input)
            response = call_llm(prompt)

            if any(keyword in user_input.lower() for keyword in
                   ["python", "java", "react", "node", "django",
                    "sql", "aws", "machine learning", "ml", "ai"]):

                st.session_state.tech_stack = user_input
                st.session_state.stage = "technical_questions"

        elif st.session_state.stage == "technical_questions":

            prompt = generate_questions_prompt(st.session_state.tech_stack)
            response = call_llm(prompt)

            st.session_state.stage = "completed"

        else:
            response = "The screening process is completed. Thank you!"

        st.session_state.chat_history.append(("assistant", response))


for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
