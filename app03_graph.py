import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.line_chart(dataframe) # 線グラフ
st.area_chart(dataframe) # チャート
st.bar_chart(dataframe) # 棒グラフ