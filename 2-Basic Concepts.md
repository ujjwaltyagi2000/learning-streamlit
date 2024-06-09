# Data flow

Streamlit's architecture allows you to write apps the same way you write plain Python scripts. To unlock this, Streamlit apps have a unique data flow: any time something must be updated on the screen, Streamlit reruns your entire Python script from top to bottom.

This can happen in two situations:

<ol>
<li>Whenever you modify your app's source code.</li>
<li>Whenever a user interacts with widgets in the app. For example, when dragging a slider, entering text in an input box, or clicking a button.</li>
</ol>

Whenever a callback is passed to a widget via the on_change (or on_click) parameter, the callback will always run before the rest of your script.

# Display and style data

There are a few ways to display data (tables, arrays, data frames) in Streamlit apps. Below, you will be introduced to magic and st.write(), which can be used to write anything from text to tables. After that, let's take a look at methods designed specifically for visualizing data.

### Use magic

You can also write to your app without calling any Streamlit methods. Streamlit supports "magic commands," which means you don't have to use st.write() at all! To see this in action try this snippet:

```python
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
```

> Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write(). For more information, refer to the documentation on magic commands.

Sure, here's the Streamlit code formatted with headings for easy copying into markdown:

---

### Displaying a Simple Dataframe

```python
import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
```

---

### Displaying an Interactive Table

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Using st.dataframe() to display an interactive table:")
dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe)
```

---

### Styling a Dataframe

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Styling a dataframe with Pandas Styler:")
styled_dataframe = dataframe.style.highlight_max(axis=0)
st.dataframe(styled_dataframe)
```

---

### Displaying a Static Table

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Using st.table() to display a static table:")
st.table(dataframe)
```

---

### Adding a Line Chart

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Adding a line chart with st.line_chart():")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)
```

---

### Plotting a Map

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Plotting a map with st.map():")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
```

---

### Adding Widgets

```python
import streamlit as st

st.write("Adding widgets with Streamlit:")
x = st.slider('Select a value for x')
st.write(x, 'squared is', x * x)
```

---

### Using Checkboxes to Show/Hide Data

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("Using checkboxes to show/hide data:")
if st.checkbox('Show dataframe'):
    st.write(chart_data)
```

---

### Using Selectbox to Choose from Data

```python
import streamlit as st
import pandas as pd

st.write("Using a selectbox to choose from data:")
option = st.selectbox('Which number do you like best?', df['first column'])
st.write('You selected:', option)
```

---

### Using Sidebar for Layout

```python
import streamlit as st

st.write("Using sidebar for layout with st.sidebar:")
with st.sidebar:
    add_selectbox = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
    add_slider = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
```

---

### Showing Progress with Progress Bar

```python
import streamlit as st
import time

st.write("Showing progress with st.progress():")
'Starting a long computation...'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'...and now we\'re done!'
```

---

Feel free to copy and paste these headings and code snippets directly into your markdown document. Adjust them as needed to fit your specific documentation style.
