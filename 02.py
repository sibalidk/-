import streamlit as st
import random

st.set_page_config(page_title="유리함수 문제 생성기", page_icon="📘")

st.title("📘 유리함수 문제 생성기 (고1 수준)")
st.write("아래 버튼을 눌러 새로운 문제를 만들어보세요!")

# ------------------------------
# 문제은행 생성 함수
# ------------------------------

def generate_basic_problem():
    # 유리식 계산 문제
    problems = [
        ("다음을 계산하시오:  \\( \\frac{2x}{x^2 - 1} + \\frac{3x}{x + 1} \\)", "\\( \\frac{5x^2 + 2x}{x^2 - 1} \\)"),
        ("다음을 계산하시오:  \\( \\frac{x^2 - 4}{x^2 - x - 6} \\)", "\\( \\frac{(x-2)(x+2)}{(x-3)(x+2)} = \\frac{x-2}{x-3}, x \\neq -2, 3 \\)"),
        ("다음을 약분하시오:  \\( \\frac{x^2 - 9}{x^2 + 5x + 6} \\)", "\\( \\frac{x - 3}{x + 2}, x \\neq -2, -3 \\)")
    ]
    return random.choice(problems)

def generate_concept_problem():
    # 개념 확인 문제
    problems = [
        ("함수 \\( f(x) = \\frac{1}{x-3} \\) 의 정의역을 구하시오.", "정의역: \\( \\mathbb{R} \\setminus \\{3\\} \\)"),
        ("함수 \\( f(x) = \\frac{2x+1}{x} \\) 의 수직점근선의 방정식을 구하시오.", "수직점근선: \\( x = 0 \\)"),
        ("함수 \\( f(x) = \\frac{x-1}{x+2} \\) 의 수평점근선을 구하시오.", "수평점근선: \\( y = 1 \\)")
    ]
    return random.choice(problems)

def generate_graph_problem():
    # 그래프 해석 문제
    problems = [
        ("함수 \\( f(x) = \\frac{1}{x} \\) 의 그래프를 평행이동하여 \\( f(x) = \\frac{1}{x-2} + 1 \\) 이 되었다. 이동 방향과 거리를 말하시오.",
         "오른쪽으로 2, 위로 1 만큼 평행이동"),
        ("함수 \\( f(x) = \\frac{2}{x} \\) 그래프의 점근선을 쓰시오.", "수직점근선: x=0, 수평점근선: y=0"),
        ("함수 \\( f(x) = \\frac{1}{x+1} \\) 의 그래프는 \\( y = \\frac{1}{x} \\) 의 그래프를 어느 방향으로 이동한 것인가?",
         "왼쪽으로 1만큼 이동")
    ]
    return random.choice(problems)

def generate_applied_problem():
    # 응용형 문제
    problems = [
        ("어떤 탱크에 물을 넣을 때의 속도가 시간에 따라 \\( v(t) = \\frac{100}{t+2} \\) (L/min) 이라면, t=3일 때 속도를 구하시오.",
         "\\( v(3) = \\frac{100}{5} = 20 \\text{ L/min} \\)"),
        ("함수 \\( f(x) = \\frac{k}{x} \\) 가 점 (2,3)을 지난다면, 상수 k의 값을 구하시오.",
         "\\( 3 = \\frac{k}{2} \\Rightarrow k = 6 \\)"),
        ("함수 \\( f(x) = \\frac{1}{x-1} \\) 이 정의되지 않는 x의 값을 구하시오.",
         "x = 1")
    ]
    return random.choice(problems)

# ------------------------------
# 문제 선택 UI
# ------------------------------

problem_type = st.selectbox(
    "문제 유형을 선택하세요 👇",
    ("기본 유리식 계산", "유리함수 개념", "그래프 해석", "응용형 문제")
)

if st.button("문제 생성하기 🎲"):
    if problem_type == "기본 유리식 계산":
        q, a = generate_basic_problem()
    elif problem_type == "유리함수 개념":
        q, a = generate_concept_problem()
    elif problem_type == "그래프 해석":
        q, a = generate_graph_problem()
    else:
        q, a = generate_applied_problem()

    st.markdown(f"### 🧮 문제")
    st.markdown(q)
    with st.expander("정답 보기"):
        st.markdown(f"**정답:** {a}")
else:
    st.info("문제 유형을 선택하고 ‘문제 생성하기’ 버튼을 눌러보세요!")

st.write("---")
st.caption("© 2025 유리함수 문제 생성기 - 고등학교 1학년 수준")
