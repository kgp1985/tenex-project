# hashed out take one but keept it for data lineage
# # #import streamlit as st

# # Page Configuration
# st.set_page_config(page_title="Message for Tenex", page_icon="⚡")

# # Custom CSS for a clean, professional look
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f5f5f5;
#     }
#     .stButton>button {
#         width: 100%;
#         border-radius: 5px;
#         height: 3em;
#         background-color: #000000;
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Content
# st.title("To the Tenex Team ⚡")

# st.write("""
# Thank you for actually clicking this link. I made this site just for you using Gemini to help me code and deploy. 
# I hope you enjoyed my double answer to your Why statement and will consider me for this role. 
# **I am the one you seek.**
# """)

# st.subheader("- KP")

# st.divider()

# # Action Buttons
# col1, col2 = st.columns(2)

# with col1:
#     st.link_button("View My LinkedIn", "https://www.linkedin.com/in/kylegpederson")

# with col2:
#     # Option 1: Direct link to a hosted PDF (Google Drive/Dropbox)
#     st.link_button("Open My Resume", "https://drive.google.com/file/d/1kW7R6f9t40SHKX3zvZ1XsWC7BD2PfKPd/view?usp=drive_link")

# # Subtle footer
# st.caption("Built with Python & Curiosity.")

#take 2
import streamlit as st

# 1. Page Config
st.set_page_config(page_title="KP | Tenex", page_icon="⚡", layout="centered")

# 2. Custom CSS for the "Professional Minimalist" look
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; }
    div.stButton > button:first-child {
        background-color: #000000;
        color: #ffffff;
        border-radius: 8px;
        border: 1px solid #333;
        height: 3.5em;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #333333;
        border: 1px solid #555;
    }
    /* Style for the message box */
    .stInfo {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("Mission: Tenex ⚡")
st.write("---")

# 4. Your Custom Text
st.markdown("### To the Tenex Team,")
st.write("""
Thank you for actually clicking this link. I made this site just for you using Gemini to help me code and deploy. 
I hope you enjoyed my split answer to your Why statement and will consider me for this role.
""")

st.subheader("I am the one you seek.")
st.caption("- KP")

st.write("##") # Visual spacer

# 5. Action Section
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Status", value="Ready to Build")
    st.link_button("📂 View My Resume", "https://drive.google.com/file/d/1kW7R6f9t40SHKX3zvZ1XsWC7BD2PfKPd/view?usp=sharing", use_container_width=True)

with col2:
    st.metric(label="Tooling", value="Python + AI")
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/kylegpederson", use_container_width=True)

st.write("---")

# 6. Interactive Element (Optional "Tenex" Energy)
# --- The Surprise Section ---
st.write("##")
if st.button("Click for a surprise 🕹️"):
    st.balloons()
    st.markdown("### There's plenty more fun surprises if you choose to hire me!")
    
    # Using a reliable 8-bit Snake game embed
    st.components.v1.iframe("https://snake.io/", height=500, scrolling=True)
    
    st.info("I believe in building tools that are as engaging as they are functional.")