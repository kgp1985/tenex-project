import streamlit as st

# Page Configuration
st.set_page_config(page_title="Message for Tenex", page_icon="⚡")

# Custom CSS for a clean, professional look
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #000000;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Content
st.title("To the Tenex Team ⚡")

st.write("""
Thank you for actually clicking this link. I made this site just for you using Gemini to help me code and deploy. 
I hope you enjoyed my double answer to your Why statement and will consider me for this role. 
**I am the one you seek.**
""")

st.subheader("- KP")

st.divider()

# Action Buttons
col1, col2 = st.columns(2)

with col1:
    st.link_button("View My LinkedIn", "https://www.linkedin.com/in/kylegpederson")

with col2:
    # Option 1: Direct link to a hosted PDF (Google Drive/Dropbox)
    st.link_button("Open My Resume", "https://drive.google.com/file/d/1kW7R6f9t40SHKX3zvZ1XsWC7BD2PfKPd/view?usp=drive_link")

# Subtle footer
st.caption("Built with Python & Curiosity.")
