import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyDnSF5aTGJuffYy75ff-FJ11V2NIYBNEQI")

# Course Catalog
COURSES = [
    {"title": "Intro to Python", "domain": "Programming", "level": "Beginner", "duration": "4 weeks"},
    {"title": "Data Science with Python", "domain": "Data Science", "level": "Intermediate", "duration": "6 weeks"},
    {"title": "Cloud Fundamentals", "domain": "Cloud", "level": "Beginner", "duration": "3 weeks"},
    {"title": "Advanced Machine Learning", "domain": "AI", "level": "Advanced", "duration": "8 weeks"},
    {"title": "Generative AI with Watsonx", "domain": "AI", "level": "Intermediate", "duration": "5 weeks"},
    {"title": "Prompt Engineering Basics", "domain": "AI", "level": "Beginner", "duration": "2 weeks"},
    {"title": "Cybersecurity Essentials", "domain": "Cybersecurity", "level": "Beginner", "duration": "4 weeks"},
    {"title": "DevOps and CI/CD", "domain": "Software Engineering", "level": "Intermediate", "duration": "5 weeks"},
    {"title": "Frontend Web Development", "domain": "Web", "level": "Beginner", "duration": "6 weeks"},
    {"title": "Backend with Node.js", "domain": "Web", "level": "Intermediate", "duration": "5 weeks"},
]

df_courses = pd.DataFrame(COURSES)
model = genai.GenerativeModel('gemini-1.5-flash')

def recommend_courses(user_prompt: str) -> str:
    context = (
        "You are an AI-powered course advisor. Based on the user's background, interests, and goals, "
        "analyze and suggest relevant courses. Match their interests to the following catalog with detailed explanations, durations, and levels:"
        + df_courses.to_string(index=False) + ""
        "User input: " + user_prompt
    )
    response = model.generate_content(context)
    return response.text

# Streamlit UI setup
st.set_page_config(page_title="🎓 Smart Course Advisor", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
        font-family: 'Gotham', sans-serif;
    }
    .main-title {
        text-align: center;
        color: #003366;
        padding: 30px ;
    }
    .author-tag {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: -10px;
    }
    .response-box {
        background: #000000;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #d1e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">🎓 Smart Course Recommendation Bot</h1>', unsafe_allow_html=True)
st.markdown('<div class="author-tag">Built with ❤️ by Aayush Raj | Reg No: 23bce0372</div>', unsafe_allow_html=True)

st.markdown("#### 📘 Tell us a bit about yourself and your interests:")

with st.form("course_form"):
    user_input = st.text_area("🧑‍💻 Background, skills, and goals", height=150, placeholder="Example: I'm a beginner interested in AI and cloud computing.")
    submitted = st.form_submit_button("🔍 Get Personalized Recommendations")

if submitted and user_input.strip():
    with st.spinner("🤖 Analyzing your profile and matching with top courses..."):
        reply = recommend_courses(user_input)
    st.markdown("### 📚 Your Personalized Learning Path")
    st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)
