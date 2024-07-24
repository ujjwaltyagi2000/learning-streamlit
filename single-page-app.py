# exploring a public Uber dataset for pickups and drop-offs in New York City

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time' # The name of the column in the dataset that contains the date and time information.
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz') # The URL where the dataset is hosted. The data is stored in a gzipped CSV file.

@st.cache_data #  decorator to cache the output of the function, improving performance by not reloading the data each time the app runs.
def load_data(nrows):
    '''
    A function that reads the CSV file from DATA_URL using Pandas, processes the data by converting column names to lowercase, and parses the 'DATE_COLUMN' as datetime.
    The number of rows loaded is controlled by the 'nrows' parameter.

    '''

    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...') # A placeholder that displays text while the data is being loaded.
data = load_data(10000) # The number of rows loaded is controlled by the 'nrows' parameter.
data_load_state.text("Done! (using st.cache_data)") # A placeholder that displays text once the data has been loaded.

if st.checkbox('Show raw data'): # A checkbox that allows the user to show the raw data
    st.subheader('Raw data') 
    st.write(data) # Displays the raw data in the Streamlit app.

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)