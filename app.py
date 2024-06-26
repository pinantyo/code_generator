import streamlit as st
import streamlit.components.v1 as components
from utility import *





generate_session()



with st.container():
    st.markdown("# Code Generator")
    st.sidebar.markdown("# Code Generator")


    text_input = st.text_input(
        "Enter instructions for code generator",
    )

    # Model generator



    text_output = st.text_area(
        'Output',
        value="<html><h1>Output generated by code<h1><br><h4>H4 Text</h4><html>",
        disabled=True
    )

    with open('.caches/index_{st.session_state.key}.html', 'w') as f:
        f.write(text_output)



with st.container():
    st.markdown("# Output Website")

    with open('.caches/index_{st.session_state.key}.html', 'r') as f:
        source_code = f.read()

        components.html(source_code, height=600)



