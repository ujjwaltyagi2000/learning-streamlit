# What we're building?

# A simple app that shows the various ways on how to accept user input by adjusting the slider widget.

# Flow of the app:

#     User selects value by adjusting the slider widget
#     App prints out the selected value


import streamlit as st
from datetime import time, datetime


# Example 1:
st.header('st.slider()')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 10) # 25 is default value
st.write("I'm ", age, 'years old')

# Example 2:
st.subheader('Range slider')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Selected Range:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)