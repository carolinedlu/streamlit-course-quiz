import streamlit as st

placeholder = st.empty()

with placeholder.container():
  st.write('Are you ready to answer a few questions about installing Streamlit?')
  ready = st.button("I'm ready!")

if ready:
  with placeholder.container():
    question_1 = st.radio(
      "What is a package manager?",
      ('A person who delivers Amazon shipments', 'A tool that automates the process of installing, upgrading, configuring, and removing dependencies', 'A method to keep your development environment separate from other projects on the same machine', 'A tool that automatically removes dependencies if they have been deprecated'))

    if question_1 == 'A tool that automates the process of installing, upgrading, configuring, and removing dependencies':
      st.success("That's right! Great job.", icon="✅")
    elif question_1 == 'A person who delivers Amazon shipments' or question_1 == A method to keep your development environment separate from other projects on the same machine' or question_1 == 'A tool that automatically removes dependencies if they have been deprecated':
      st.error('Uh oh. Wrong answer. Try again!', icon="🚨")

  
