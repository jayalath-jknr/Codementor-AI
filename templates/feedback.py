import streamlit as st
from services.falcon_integration import FalconIntegration

def show_feedback():
    falcon = FalconIntegration()
    st.title("Feedback and Support")
    
    user_message = st.text_area("Enter your message:", height=150)
    if st.button("Get Feedback"):
        if user_message:
            feedback = falcon.get_feedback(user_message)
            st.subheader("AI Feedback")
            st.write(feedback)
        else:
            st.error("Please enter your message before getting feedback.")

show_feedback()
