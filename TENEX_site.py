
#take 3
import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="Kyle Pederson | Tenex", layout="centered")

# 2. Custom CSS (Simplified & High-Priority)
st.markdown("""
    <style>
    /* This styles ALL buttons on the page to be Tenex Black */
    button, div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-radius: 5px !important;
        border: 1px solid #000000 !important;
        width: 100% !important;
        height: 3em !important;
    }
    
    button:hover {
        background-color: #333333 !important;
        border: 1px solid #333333 !important;
    }

    /* This targets the specific 'Take a break' expander text */
    .streamlit-expanderHeader {
        font-weight: bold !important;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("Kyle Pederson for Tenex AI Strategist")
st.write("---")

# 4. The Message
st.markdown("### To the Tenex Team,")
st.write(
    "Thank you for actually clicking this link. I made this site just for you using Gemini "
    "to help me code and deploy. I hope you enjoyed my split answer to your Why statement "
    "and will consider me for this role. **I am the one you seek.**"
)
st.write("— Kyle Pederson")

st.write("##") # Spacer

# 5. Professional Links
col1, col2 = st.columns(2)

with col1:
    # Standard Streamlit button (will be Black)
    st.link_button("View My Resume", "https://drive.google.com/file/d/1kW7R6f9t40SHKX3zvZ1XsWC7BD2PfKPd/view?usp=sharing", use_container_width=True)

with col2:
    # Custom HTML button for LinkedIn Blue
    # This bypasses Streamlit's button restrictions entirely
    st.markdown("""
        <a href="https://www.linkedin.com/in/kylegpederson" target="_blank" style="text-decoration: none;">
            <div style="
                background-color: #0077B5;
                color: white;
                padding: 10px;
                text-align: center;
                border-radius: 5px;
                font-weight: bold;
                height: 3em;
                display: flex;
                align-items: center;
                justify-content: center;
                border: 1px solid #0077B5;
                font-size: 14px;">
                LinkedIn Profile
            </div>
        </a>
    """, unsafe_allow_html=True)

# 6. The Surprise Section
st.write("##")
st.write("---")

# Initialize Session States
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

with st.expander("Take a break, enjoy a fun puzzle"):
    st.write("I'm thinking of a number between 1 and 100. Can you find it in the fewest moves?")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="game_input")
    
    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.info("Higher... ↑")
        elif guess > st.session_state.secret_number:
            st.info("Lower... ↓")
        else:
            st.success(f"Correct! It took you {st.session_state.attempts} attempts.")
            st.balloons()
            st.session_state.game_over = True
            
            # Add score to local leaderboard
            st.session_state.leaderboard.append(st.session_state.attempts)
            # Sort scores (lowest attempts first)
            st.session_state.leaderboard.sort()
            
            st.write("There's plenty more fun surprises if you choose to hire me.")

    # Display Local Leaderboard
    if st.session_state.leaderboard:
        st.write("### 🏆 Session Top 3")
        # Get the top 3 unique best scores
        top_scores = sorted(list(set(st.session_state.leaderboard)))[:3]
        
        for i, score in enumerate(top_scores):
            st.write(f"{i+1}. **{score} attempts**")

    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.rerun()

# 7. Subtle Footer
st.write("##")
st.caption("Built with Python, AI, and curiosity.")