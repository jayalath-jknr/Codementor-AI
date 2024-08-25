import streamlit as st
from services.watson_integration import WatsonIntegration
from streamlit_ace import st_ace

questions = [
    {"question": "Write a program in C++ to print 'Welcome to Programming Concepts'.", "expected_output": "Welcome to Programming Concepts\n"},
    {"question": "Write a program to print the following output.\nHi I am << Your Name>>\nThis is my first C++ program", "expected_output": "Hi I am << Your Name>>\nThis is my first C++ program\n"},
    # Add more questions and expected outputs as needed
]

def show():
    st.title("C++ Coding Questions")
    watson_integration = WatsonIntegration()
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        
        user_code = st_ace(
            value='',
            language='c_cpp',
            theme='monokai',
            key=f"code_{i}",
            height=300
        )
        
        if st.button(f"Evaluate Question {i+1}", key=f"eval_{i}"):
            if user_code:
                review_comments = watson_integration.review_code(user_code)
                st.subheader("AI Feedback")
                st.write(review_comments)

                output = watson_integration.generate_code(user_code)
                normalized_output = output.strip()
                normalized_expected_output = q["expected_output"].strip()
                if normalized_output == normalized_expected_output:
                    st.success(f"Correct! Output: {output}")
                    st.markdown("### Marks: 10/10")
                else:
                    st.error(f"Incorrect. \nExpected: {q['expected_output']}\nGot: {output}")
                    st.write("Raw Outputs for Debugging:")
                    st.text(f"Expected: {repr(q['expected_output'])}")
                    st.text(f"Got: {repr(output)}")
                    st.markdown("### Marks: 5/10")  # Adjust scoring logic as needed
            else:
                st.error("Please enter your code before evaluation.")
