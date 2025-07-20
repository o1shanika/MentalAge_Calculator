import streamlit as st
from utils.loader import load_questions
from utils.scores import calculate_mental_age

st.set_page_config(page_title="Questions", layout="wide")

st.title("📝 The Quiz")
st.info("Please answer the following questions honestly to get the most accurate result.")

# Use columns for a cleaner layout
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("First, what is your biological age?", min_value=10, max_value=100, value=25)
with col2:
    gender = st.selectbox("What is your gender?", ["Female", "Male", "Other"])

st.divider()

questions = load_questions(age, gender)

# Check if questions were loaded
if not questions:
    st.error("Could not load questions. Please check the `data/questions.json` file.")
else:
    # Use a form to prevent re-running the app on each radio button selection
    with st.form("quiz_form"):
        responses = {}
        for i, q in enumerate(questions):
            # Use a unique key for each radio button
            responses[i] = st.radio(q['question'], q['options'], key=f"q_{i}")

        # Submit button for the form
        submitted = st.form_submit_button("🧠 Calculate My Mental Age")

    if submitted:
        with st.spinner("Calculating your result..."):
            mental_age = calculate_mental_age(responses, age, gender)

        st.success(f"## 🎉 Your estimated mental age is **{mental_age}**!")
        st.balloons()
        st.info("This is just for fun! Your mental age can change based on your mood, experiences, and perspective.")
