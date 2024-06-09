import streamlit as st
import time

st.write("Showing progress with st.progress():")
'Starting a long computation...'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'...and now we\'re done!'