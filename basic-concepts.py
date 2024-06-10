# # insert a dataframe -->

# import streamlit as st
# import pandas as pd
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]}))
    


# # insert an interactive table -->

# import streamlit as st
# import numpy as np
# import pandas as pd

# st.write("Using st.dataframe() to display an interactive table:")
# dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe)



# # styling a table -->

# import streamlit as st
# import numpy as np
# import pandas as pd

# dataframe = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]})
# st.write("Styling a dataframe with Pandas Styler:")
# styled_dataframe = dataframe.style.highlight_max(axis=0)
# st.dataframe(styled_dataframe)



# # line chart -->

# import streamlit as st
# import numpy as np
# import pandas as pd

# st.write("Adding a line chart with st.line_chart():")
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# st.line_chart(chart_data)




# # plotting a map -->

# import streamlit as st
# import numpy as np
# import pandas as pd

# st.write("Plotting a map with st.map():")
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(map_data)




# # adding a widget -->

# import streamlit as st

# st.write("Adding widgets with Streamlit:")
# x = st.slider('Select a value for x')
# st.write(x, 'squared is', x * x)



# # Using Checkboxes to Show/Hide Data

# import streamlit as st
# import numpy as np
# import pandas as pd

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# st.write("Using checkboxes to show/hide data:")
# if st.checkbox('Show dataframe'):
#     st.write(chart_data)



# progress bar -->

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