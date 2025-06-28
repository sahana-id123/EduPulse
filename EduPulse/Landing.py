import streamlit as st
from utils import load_css
import random





# Page config
st.set_page_config(
    page_title="EduNexus 2.0 🚀",
    page_icon="🚀",
    layout="wide"
)




# Load custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Title Section
st.markdown("<h1 class='main-title'>Welcome to EduPluse  🚀</h1>", unsafe_allow_html=True)

# Inspirational quotes
quotes = [
    '"Education is not preparation for life; education is life itself." - John Dewey',
    '"Live as if you were to die tomorrow. Learn as if you were to live forever." - Mahatma Gandhi',
    '"The beautiful thing about learning is that no one can take it away from you." - B.B. King',
    '"Education is the most powerful weapon which you can use to change the world." - Nelson Mandela'
]



# Display random quote
st.markdown(
    f"""<div class='card'>
        <p style='text-align: center; font-style: italic;'>{random.choice(quotes)}</p>
    </div>""",
    unsafe_allow_html=True
)



# Features Section
st.markdown("<h2 class='sub-title'>Our Features</h2>", unsafe_allow_html=True)

# Custom CSS for fixed card size
st.markdown("""
    <style>
    .feature-card {
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: #262730;
        border-radius: 1rem;
        border: 1px solid #464646;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .feature-card h3 {
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .feature-card p {
        flex-grow: 1;
        color: #fafafa;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """<div class='feature-card'>
            <h3>🎓 Personalized Learning</h3>
            <p>Get customized learning plans and guidance tailored to your unique educational journey and goals.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>💻 AI Code Mentor</h3>
            <p>Receive expert coding assistance, reviews, and debugging help from our intelligent coding companion.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>📹 Lecture Summaries</h3>
            <p>Transform lengthy video lectures into concise, structured summaries for efficient learning.</p>
        </div>""", unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """<div class='feature-card'>
            <h3>❓ Real-time Support</h3>
            <p>Get instant answers to your academic questions with our AI-powered Q&A system.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>📅 Study Planner</h3>
            <p>Create personalized study schedules and track your progress with our interactive planner.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>🌍 Multi-Language</h3>
            <p>Break language barriers with our comprehensive multi-language learning support system.</p>
        </div>""", unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """<div class='feature-card'>
            <h3>📚 Smart Summaries</h3>
            <p>Convert complex documents into clear, concise summaries for better understanding.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>🧠 Mental Wellness</h3>
            <p>Access comprehensive support and resources for maintaining mental well-being during studies.</p>
        </div>""", unsafe_allow_html=True
    )
    st.markdown(
        """<div class='feature-card'>
            <h3>📚 Study Resources</h3>
            <p>Generate customized study materials, practice tests, and revision guides with AI assistance.</p>
        </div>""", unsafe_allow_html=True
    )


# # Team Section
# st.markdown("<h2 class='sub-title'>Meet Our Team</h2>", unsafe_allow_html=True)

# team_col1, team_col2, team_col3, team_col4, team_col5, team_col6 = st.columns(6)

# with team_col1:
#     st.markdown(
#         """<div class='card'>
#             <h3>John Doe</h3>
#             <p>Lead Developer</p>
#             <p class='info-text'>Expert in AI and Machine Learning</p>
#         </div>""",
#         unsafe_allow_html=True
#     )

# with team_col2:
#     st.markdown(
#         """<div class='card'>
#             <h3>Jane Smith</h3>
#             <p>UX Designer</p>
#             <p class='info-text'>Specialized in Educational Technology</p>
#         </div>""",
#         unsafe_allow_html=True
#     )

# with team_col3:
#     st.markdown(
#         """<div class='card'>
#             <h3>Mike Johnson</h3>
#             <p>Education Expert</p>
#             <p class='info-text'>PhD in Educational Psychology</p>
#         </div>""",
#         unsafe_allow_html=True
#     )
# with team_col4:
#     st.markdown(
#         """<div class='card'>
#             <h3>Mike Johnson</h3>
#             <p>Education Expert</p>
#             <p class='info-text'>PhD in Educational Psychology</p>
#         </div>""",
#         unsafe_allow_html=True
#     )
# with team_col5:
#     st.markdown(
#         """<div class='card'>
#             <h3>Mike Johnson</h3>
#             <p>Education Expert</p>
#             <p class='info-text'>PhD in Educational Psychology</p>
#         </div>""",
#         unsafe_allow_html=True
#     )
# with team_col6:
#     st.markdown(
#         """<div class='card'>
#             <h3>Mike Johnson</h3>
#             <p>Education Expert</p>
#             <p class='info-text'>PhD in Educational Psychology</p>
#         </div>""",
#         unsafe_allow_html=True
#     )            
# Team Section
