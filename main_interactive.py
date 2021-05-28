import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('000002.jpg')
    st.image(img, caption='Naoki Fujiwara', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

# テキスト入力
text = st.sidebar.text_input('あなたの趣味を教えてください。') #sidebar.を入れるとサイドバーに移動できる


# スライダー
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text, 'です。'
'コンディション', condition