import streamlit as st

# The options split into three columns
options_column_1 = [
    '鹹酥雞', 
    '臭豆腐', 
    '滷肉飯', 
    '蚵仔煎', 
    '生煎包', 
    '肉圓', 
    '滷味', 
    '鹹水雞', 
    '小籠包', 
    '蔥抓餅', 
    '拔絲地瓜', 
    '豬血糕', 
    '米苔目冰'
]
options_column_2 = [
    '糖葫蘆',
    '地瓜球', 
    '粉粿', 
    '刈包', 
    '肉粽', 
    '雞肉飯', 
    '韭菜盒', 
    '潤餅捲', 
    '白糖粿', 
    '擔仔麵', 
    '鐵蛋',
    '牛肉湯', 
    '阿給'
]
options_column_3 = [
    '豆花', 
    '黑白切',
    '車輪餅', 
    '客家麻糬',
    '大腸包小腸', 
    '豬油拌飯',
    '燒餅油條', 
    '芋粿巧',
    '排骨酥湯', 
    '薑母鴨',
    '四神湯', 
    '魷魚焿',
    '花生捲冰淇淋'
]


# Function to calculate the score
def calculate_score(options):
    return sum(options)

st.set_page_config(
    page_title="台灣小吃我超愛清單",
    page_icon="🍢",
    layout="wide"
)

# Display the checkboxes and calculate the score
#st.title('')
st.markdown("<h1 style='text-align: center; color: red;'>台灣小吃我超愛清單!</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; '>made by <a href='https://github.com/ThisIsJeron' target='_blank'>Jeron Wong</a></h3>",
    unsafe_allow_html=True
)



col1, col2, col3 = st.columns(3)
selected_options = []

with col1:
    selected_options.extend([st.checkbox(option, key=option) for option in options_column_1])

with col2:
    selected_options.extend([st.checkbox(option, key=option) for option in options_column_2])

with col3:
    selected_options.extend([st.checkbox(option, key=option) for option in options_column_3])

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button('顯示結果'):
        score = calculate_score(selected_options)
        if score <= 9:
            result = '超愛0~9「我標準很高」'
        elif score <= 19:
            result = '超愛10~19=「一般人」'
        elif score <= 29:
            result = '超愛20~29-「吃貨」'
        else:
            result = '超愛30個=「食神」'

        # Use markdown with HTML for centered text
        #st.markdown(f'<h2 style="text-align: center;">您的選擇計分是: {score}</h2>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="text-align: center;">您的美食愛好者等級是: {result}</h2>', unsafe_allow_html=True)