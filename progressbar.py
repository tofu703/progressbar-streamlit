import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1内容')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2内容')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3内容')

#text = st.text_input('あなたの趣味を教えてください。') # テキスト入力
#condition = st.slider('あなたの今の調子は？', 0, 100, 50) # スライダー
#'あなたの趣味：', text, 'です。'
# 'コンディション', condition