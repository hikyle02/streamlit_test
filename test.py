import streamlit as st
import pandas as pd

view = [100,220,330]
st.write('KDcamp View')
st.write('## raw')

view
st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview