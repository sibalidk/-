import streamlit as st
import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 범위에서
    numbers = range(1, 46)
    # 중복 없이 6개의 숫자를 무작위로 선택합니다.
    # random.sample은 중복 없이 고유한 요소를 선택하는 데 사용됩니다.
    lotto_numbers = random.sample(numbers, 6)
    # 숫자를 오름차순으로 정렬하여 표시하는 것이 일반적입니다.
    lotto_numbers.sort()
    return lotto_numbers

# Streamlit 앱의 제목 설정
st.title("🍀 대한민국 로또 번호 생성기")

# 설명 추가
st.write("아래 버튼을 누르면 1부터 45 사이의 숫자 중 **6개의 고유한** 로또 번호가 생성됩니다.")

# '생성' 버튼 생성
if st.button("✨ 번호 생성"):
    # 버튼이 눌리면 로또 번호를 생성합니다.
    result_numbers = generate_lotto_numbers()

    # 결과 표시
    st.subheader("✅ 생성된 로또 번호:")
    
    # 결과를 더 보기 좋게 표시합니다.
    # 각 숫자를 둥근 배지로 표시하는 Markdown과 HTML 스타일을 사용할 수 있습니다.
    
    # 각 숫자에 대해 스타일을 적용하여 문자열을 생성합니다.
    number_display = " ".join([
        f'<span style="background-color: #4CAF50; color: white; padding: 10px 15px; border-radius: 25px; font-size: 24px; font-weight: bold; margin: 0 5px;">{num}</span>'
        for num in result_numbers
    ])
    
    # st.markdown을 사용하여 HTML을 표시하고, unsafe_allow_html=True를 설정합니다.
    st.markdown(f'<div style="text-align: center; margin-top: 20px;">{number_display}</div>', unsafe_allow_html=True)
    
    # 추가 메시지
    st.balloons()
