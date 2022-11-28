import streamlit as st
import numpy as np
import pandas as pd

st.title("タイトル")
st.write('データフレーム')

df = pd.DataFrame({
    '一列目':[1,2,3,4],
    '２列目':[10,20,30,40,]

})

st.write(df)
#長過ぎるときは下のやつで表示範囲を決める
#st.dataframe(df, width=100, height=100)

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)