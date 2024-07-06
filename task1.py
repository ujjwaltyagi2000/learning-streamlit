# button to count the number of times the page has been run

import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")

st.button("Run it again")

print(st.session_state) # prints dictionary containing counter on terminal
