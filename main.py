import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトルを書く
st.title('超入門')

# テキスト入れる
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

st.write(df)

# この書き方でも良い
# 表の形式とか指定できる.列でmaxをハイライト色付けし，幅高さを指定の例
st.dataframe(df.style.highlight_max(axis=0), width=300, height=600)

# 静的（並び替えとかできない）表を作るならこれ
st.table(df.style.highlight_max(axis=0))

# マークダウンも書ける
# ``で囲えばコードも書ける．言語も指定できる

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# 折れ線・棒グラフを書く
df2 = pd.DataFrame(
    np.random.rand(20, 3), # 乱数表を作成
    columns=['a', 'b','c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# 地図上でのマッピングを描く
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+ [35.69, 139.70], # 乱数表を作成(新宿付近の緯度経度100個を作成)
    columns=['lat', 'lon']
)
st.map(df3)

# 画像などのメディアを埋め込む（動画や音楽も可能）
st.write('Display Image')
img = Image.open('money.jpg')
st.image(img, caption='お金の画像', use_column_width=True)

# チェックボックスを付けて，未なら画像を非表示とする
# TrueFalseを返すので，if文で書く
if st.checkbox('Show Image'):
    img = Image.open('money.jpg')
    st.image(img, caption='お金の画像', use_column_width=True)


# セレクトボックスを付けて，動的に数字を選ばせる
option = st.selectbox(
    'あなたの好きな数字を教えて下さい',
    list(range(1,11))
)
# そのまんまでもかける．セレクトボックスを変数にいれて書く
'あなたの好きな数字は',option, 'です'

# テキストボックスを付けて，動的にテキストを表示する
text = st.text_input('あなたの好きな趣味を教えて下さい')
'あなたの趣味は：',text

# スライダー（点を動かして数値を動かす）を描く
condition = st.slider('あんたの今の調子は？', 0, 100, 50)
'コンディション：',condition


# レイアウトを整える

# サイドバー追加
# スライダーをサイドバーに描く
condition2 = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション２：',condition2

# カラム追加
# ボタンを追加し，左カラムに置く．ボタン押下したら，右カラムに表示する．
left_colum, right_colum = st.columns(2)
buttun = left_colum.button('右カラムに文字を表示')
if buttun:
    right_colum.write('ここは右カラムです')

# エキスパンダ（展開・押下したら開くレイアウト）
expander1 = st.expander('問合せ1')
expander1.write('問合せ1の回答は○○です')
expander2 = st.expander('問合せ2')
expander2.write('問合せ2の回答は○○です')
expander3 = st.expander('問合せ3')
expander3.write('問合せ3の回答は○○です')


# プログレスバーの表示（動的な進捗状況のバー）
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!'


