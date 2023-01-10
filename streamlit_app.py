import streamlit as st

st.subheader("Quiz!")
placeholder = st.empty()

with placeholder.container():
  st.write('Are you ready to answer a few questions about installing Streamlit?')
  ready = st.button("I'm ready!")

if ready:
  with placeholder.container():
    with st.form("question_1"):
      question_1 = st.radio(
        "What is a package manager?",
        ('A person who delivers Amazon shipments', 'A tool that automates the process of installing, upgrading, configuring, and removing dependencies', 'A method to keep your development environment separate from other projects on the same machine', 'A tool that automatically removes dependencies if they have been deprecated'))

      submit = st.form_submit_button("Submit")
      if submit:
        if question_1 == 'A tool that automates the process of installing, upgrading, configuring, and removing dependencies':
          st.success("That's right! Great job.", icon="✅")
        else:
          st.error('Uh oh. Wrong answer. Try again!', icon="🚨")
    

  
