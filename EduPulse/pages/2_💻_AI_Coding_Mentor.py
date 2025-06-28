import streamlit as st
from utils import load_css, run_watson_granite, show_error, show_success, show_info
import json

# Page config
st.set_page_config(page_title="AI Coding Mentor", page_icon="💻", layout="wide")

# Load CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>AI Coding Mentor 💻</h1>", unsafe_allow_html=True)

# Initialize session state
if 'code_history' not in st.session_state:
    st.session_state.code_history = []

# Sidebar with coding tasks
st.sidebar.markdown("<h2 class='sub-title'>Coding Assistant</h2>", unsafe_allow_html=True)
task_type = st.sidebar.selectbox(
    "What do you need help with?",
    ["Code Review", "Debug Help", "Code Explanation", "Best Practices", "Code Generation"]
)

# Task-specific prompts and button text
task_prompts = {
    "Code Review": "Please review this code and suggest improvements:",
    "Debug Help": "Help me find and fix bugs in this code:",
    "Code Explanation": "Please explain how this code works:",
    "Best Practices": "What are the best practices for this code:",
    "Code Generation": "Please help me generate code for:"
}

# Add button text mapping
task_buttons = {
    "Code Review": "🔍 Review Code",
    "Debug Help": "🐛 Debug Code",
    "Code Explanation": "📖 Explain Code",
    "Best Practices": "✨ Check Best Practices",
    "Code Generation": "🚀 Generate Code"
}

# Language selection
programming_language = st.sidebar.selectbox(
    "Programming Language",
    ["Python", "JavaScript", "Java", "C++", "SQL", "Other"]
)

# Main interface
st.markdown(
    f"""<div class='card'>
        <h3>{task_prompts[task_type]}</h3>
        <p class='info-text'>Selected language: {programming_language}</p>
    </div>""",
    unsafe_allow_html=True
)

# Code input
code_input = st.text_area("Enter your code or description:", height=200)

# Buttons
col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    if st.button("🧹 Clear History"):
        st.session_state.code_history = []
        show_success("History cleared!")
        st.rerun()

with col2:
    format_code = st.button("🎨 Format Code")

with col3:
    analyze_code = st.button(task_buttons[task_type])

if format_code and code_input:
    try:
        # System prompt for code formatting
        format_prompt = f"""Format the following {programming_language} code with proper 
        indentation and style guidelines. Return only the formatted code:
        
        {code_input}"""
        
        formatted_code = run_watson_granite(format_prompt)
        if not formatted_code.startswith("Error"):
            code_input = formatted_code
            show_success("Code formatted!")
        else:
            show_error(f"Formatting failed: {formatted_code}")
            
    except Exception as e:
        show_error(f"Formatting error: {str(e)}")

if analyze_code and code_input:
    try:
        # System prompt for code analysis
        system_prompt = f"""You are an expert {programming_language} developer and coding mentor.
        Analyze the code based on the selected task type: {task_type}.
        Provide detailed feedback including:
        1. Code quality assessment
        2. Potential improvements
        3. Best practices suggestions
        4. Security considerations
        5. Performance optimization tips
        Format your response in a clear, structured way."""
        
        response = run_watson_granite(code_input, system_prompt)
        
        if not response.startswith("Error"):
            st.session_state.code_history.append({
                "code": code_input,
                "language": programming_language,
                "task": task_type,
                "analysis": response
            })
            show_success("Analysis complete!")
        else:
            show_error(f"Analysis failed: {response}")
            
    except Exception as e:
        show_error(f"Analysis error: {str(e)}")

# Display analysis history
if st.session_state.code_history:
    st.markdown("<h2 class='sub-title'>Analysis History</h2>", unsafe_allow_html=True)
    
    for idx, entry in enumerate(reversed(st.session_state.code_history)):
        with st.container():
            st.markdown(f"**Task:** {entry['task']} ({entry['language']})")
            st.markdown("**Code:**")
            st.code(entry['code'], language=entry['language'].lower())
            st.markdown("**Analysis:**")
            st.markdown(entry['analysis'])
            st.markdown("---")

# Coding resources
with st.expander("📚 Coding Resources & Tips"):
    st.markdown(
        f"""
        ### {programming_language} Resources
        * Official Documentation
        * Popular Libraries & Frameworks
        * Style Guides
        * Common Design Patterns
        
        ### Best Practices
        * Write clean, readable code
        * Add proper documentation
        * Follow naming conventions
        * Handle errors appropriately
        * Write unit tests
        
        ### Debugging Tips
        * Use proper debugging tools
        * Add logging statements
        * Check common error patterns
        * Test edge cases
        * Review stack traces carefully
        """
    )

# Add footer messages mapping
footer_messages = {
    "Code Review": "Quality code starts with thorough reviews. Let's improve together!",
    "Debug Help": "No bug is too tricky. Let's solve it together!",
    "Code Explanation": "Understanding code is the first step. Let's learn together!",
    "Best Practices": "Better practices, better code. Let's grow together!",
    "Code Generation": "From ideas to code. Let's create together!"
}

# Footer
st.markdown(
    f"""<div style='text-align: center; margin-top: 3rem; padding: 1rem; background-color: #262730; border-radius: 0.5rem;'>
        <p>{footer_messages[task_type]}</p>
        <p class='info-text'>Happy coding! 🚀</p>
    </div>""",
    unsafe_allow_html=True
)