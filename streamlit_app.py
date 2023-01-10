import streamlit as st

placeholder = st.empty

st.write('Are you ready to answer a few questions about installing Streamlit?')
ready = st.button("I'm ready!")

if ready:
  st.subheader('What is a package manager?')
