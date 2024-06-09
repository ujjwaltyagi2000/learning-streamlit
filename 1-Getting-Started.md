# Install Streamlit in your environment

In the terminal with your environment activated, type:

```sh
pip install streamlit
```

Test that the installation worked by launching the Streamlit Hello example app:

```sh
streamlit hello
```

If this doesn't work, use the long-form command:

```sh
python -m streamlit hello`
```

<!--
```python
import streamlit
``` -->

Streamlit's Hello app should appear in a new tab in your web browser!

# Create a "Hello World" app and run it

Create a file named app.py in your project folder.

```python
import streamlit as st

st.write("Hello world")
```

Run your Streamlit app.

```sh
streamlit run app.py
```

To stop the Streamlit server, press `Ctrl+C` in the terminal.
