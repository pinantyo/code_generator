import streamlit as st
import os, base64

def generate_session():
    if 'key' not in st.session_state:
        st.session_state.key = base64.b64encode(os.urandom(16))