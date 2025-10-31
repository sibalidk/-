import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, Poly
import random

# --- 세션 상태 초기화 ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- 문제 생성 함수 ---

def generate_rational_expression_problem():
    """유리식 계산 문제 (고1 수준)"""
    x = symbols('x')
    a, b, c, d = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
    
    # 간단한 유리식 덧셈/뺄셈/곱셈/나눗셈 중 랜덤 선택
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        expr1 = (a * x) / (x + b)
        expr2 = c / (x + b)
        question = f"다음 유리식을 간단히 하시오: $\\frac{{{a}x}}{{{x} + {b}}} + \\frac{{{c}}}{{{x} + {b}}}$"
        correct_answer = simplify(expr1 + expr2)
    elif op == '-':
        expr1 = (a * x) / (x - b)
        expr2 = c / (x - b)
        question = f"다음 유리식을 간단히 하시오: $\\frac{{{a}x}}{{{x} - {b}}} - \\frac{{{c}}}{{{x} - {b}}}$"
        correct_answer = simplify(expr1 - expr2)
    elif op == '*':
        expr1 = (x + a) / (x + b)
        expr2 = (x + b) / (x + c)
        question = f"다음 유리식을 간단히 하시오: $\\frac{{x + {a}}}{{x + {b}}} \\times \\frac{{x + {b}}}{{x + {c}}}$"
        correct_answer = simplify(expr1 * expr2)
        
    return {
        "type": "유리식 계산",
        "question": question,
        "correct_answer": f"${correct_answer}$ (예: $\\frac{{x+1}}{{x+3}}$ 형태로 입력)"
    }

def generate_concept_problem():
    """유리함수의 개념 확인 문제 (점근선, 정의역, 치역)"""
    a, b, c, d = random.choice([-2, -1, 1, 2]), random.randint(1, 5), random.randint(1, 5), random.choice([-2, -1, 1, 2])
    
    # $y = \frac{a}{x-p} + q$ 형태
    p = b
    q = d
    
    question_type = random.choice(["점근선", "정의역", "치역"])
    function_str = f"$\\large y = \\frac{{{a}}}{{x - {p}}} + {q}$"
    
    if question_type == "점근선":
        question = f"함수 {function_str}의 **수직 점근선**과 **수평 점근선**의 교점의 좌표는?"
        correct_answer = f"$({p}, {q})$"
    elif question_type == "정의역":
        question = f"함수 {function_str}의 정의역은? (단, $x \\ne k$의 형태로 입력)"
        correct_answer = f"$x \\ne {p}$"
    elif question_type == "치역":
        question = f"함수 {function_str}의 치역은? (단, $y \\ne k$의 형태로 입력)"
        correct_answer = f"$y \\ne {q}$"
        
    return {
        "type": "개념 확인",
        "question": question,
        "correct_answer": correct_answer
    }

def generate_graph_interpretation_problem():
    """그래프 해석 문제 (그래프 보고 특징 파악)"""
    st.subheader("3. 그래프 해석 문제")
    
    a = random.choice([-2, -1, 1, 2])
    p = random.randint(1, 3) * random.choice([-1, 1])
    q = random.randint(1, 3) * random.choice([-1, 1])
    
    # 그래프 그리기
    x_range = np.linspace(-10, 10, 400)
    y_vals = a / (x_range - p) + q
    
    # 점근선 주변 값 처리
    y_vals[np.abs(x_range - p) < 0.1] = np.nan
    
    fig, ax = plt.subplots()
    ax.plot(x_range, y_vals, label=f'$y = \\frac{{{a}}}{{x - {p}}} + {q}$')
    
    # 점근선 그리기
    ax.axvline(p, color='r', linestyle='--', label=f'x={p}')
    ax.axhline(q, color='b', linestyle='--', label=f'y={q}')
    
    ax.set_title('유리함수 그래프')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(p - 5, p + 5)
    ax.set_ylim(q - 5, q + 5)
    ax.grid(True)
    ax.legend(loc='lower right')
    
    # 문제 유형 선택
    question_type = random.choice(["대칭 중심", "평행 이동"])
    
    if question_type == "대칭 중심":
        question = "위 그래프의 **점의 대칭 중심**의 좌표는?"
        correct_answer = f"$({p}, {q})$"
    else: # 평행 이동
        question = f"위 그래프는 함수 $y = \\frac{{{a}}}{{x}}$의 그래프를 x축 방향으로 $m$, y축 방향으로 $n$만큼 평행이동한 것이다. $m$과 $n$의 값을 순서대로 구하시오."
        correct_answer = f"$m={p}, n={q}$"
        
    return {
        "type": "그래프 해석",
        "question": question,
        "plot": fig,
        "correct_answer": correct_answer
    }

def generate_application_problem():
    """응용형 문제 (일반형 $y=\frac{ax+b}{cx+d}$에서 시작하여 점근선 구하기)"""
    
    a, b, c, d = random.choice([2, 3, 4]), random.choice([1, 2, 3]), 1, random.choice([-2, -1, 1, 2])
    
    # 분자/분모 차수 맞춰 $y = \frac{ax+b}{x+d}$ 형태
    # $y = \frac{a(x+d) + (b-ad)}{x+d} = a + \frac{b-ad}{x+d}$
    
    p = -d
    q = a
    k = b - a * d
    
    if k == 0 or p == 0: # 유리함수의 기본 형태가 아닌 경우 재생성
        return generate_application_problem()
    
    function_str = f"$\\large y = \\frac{{{a}x + {b}}}{{x + {d}}}$"
    
    question = f"함수 {function_str}의 그래프의 **점근선**은 $x=p$, $y=q$이다. $p+q$의 값은?"
    correct_answer = f"${p + q}$" # $p = -d$, $q = a$
        
    return {
        "type": "응용형",
        "question": question,
        "correct_answer": correct_answer
    }


def generate_all_problems():
    """모든 유형의 문제를 생성하여 세션 상태에 저장"""
    
    problems = []
    
    # 유형별 문제 1개씩 생성
    problems.append(generate_rational_expression_problem())
    problems.append(generate_concept_problem())
    
    # 그래프 문제는 plotting을 위해 별도로 처리
    graph_prob = generate_graph_interpretation_problem()
    problems.append(graph_prob)
    
    problems.append(generate_application_problem())
    
    # st.session_state 업데이트
    st.session_state.quiz_data = problems
    st.session_state.answers = {i: "" for i in range(len(problems))}
    st.session_state.submitted = False

# --- Streamlit UI 구성 ---

st.title("➗ 고등학교 유리함수 퀴즈 앱")
st.markdown("---")

if st.session_state.quiz_data:
    st.sidebar.success("문제가 생성되었습니다.")
else:
    if st.sidebar.button("문제 생성 (4문제)"):
        generate_all_problems()
        st.experimental_rerun() # 문제를 표시하기 위해 앱을 다시 실행

# --- 문제 표시 ---

if st.session_state.quiz_data:
    
    with st.form("quiz_form"):
        
        for i, problem in enumerate(st.session_state.quiz_data):
            st.subheader(f"💡 문제 {i+1}. [{problem['type']}]")
            st.markdown(f"**질문:** {problem['question']}")
            
            # 그래프 해석 문제인 경우 그래프 표시
            if problem['type'] == "그래프 해석":
                st.pyplot(problem['plot'])
            
            # 사용자 답변 입력
            st.session_state.answers[i] = st.text_input(
                f"답변 {i+1} (정답 예시: {problem['correct_answer']})",
                value=st.session_state.answers.get(i, ""),
                key=f"answer_{i}"
            )
            st.markdown("---")

        submit_button = st.form_submit_button("정답 확인 및 채점")
        
        if submit_button:
            st.session_state.submitted = True
            
            
# --- 채점 결과 표시 ---

if st.session_state.submitted:
    
    correct_count = 0
    st.header("✅ 채점 결과")
    st.markdown("---")

    # 모든 유형의 문제의 정답 확인 로직
    for i, problem in enumerate(st.session_state.quiz_data):
        user_answer = st.session_state.answers[i].strip().replace(" ", "").replace("$", "")
        correct_answer = problem['correct_answer'].strip().replace(" ", "").replace("$", "")
        
        st.subheader(f"문제 {i+1} 결과")
        st.markdown(f"**유형:** {problem['type']}")
        st.markdown(f"**질문:** {problem['question']}")
        
        # 그래프 해석 문제인 경우 그래프 표시
        if problem['type'] == "그래프 해석":
            st.pyplot(problem['plot'])

        # 정답 비교 (대소문자 무시, 공백 무시, $ 기호 제거)
        is_correct = (user_answer.lower() == correct_answer.lower())
        
        if is_correct:
            st.success("🎉 정답입니다!")
            correct_count += 1
        else:
            st.error("❌ 오답입니다.")
        
        st.info(f"**제출한 답:** {st.session_state.answers[i]}")
        st.info(f"**정답:** {problem['correct_answer']}")
        st.markdown("---")

    st.balloons()
    st.subheader(f"최종 점수: {correct_count} / {len(st.session_state.quiz_data)}")
    
    # 다시 풀기 버튼
    if st.button("다시 문제 생성"):
        generate_all_problems()
        st.experimental_rerun()


# --- 초기 상태 처리 (문제 생성 버튼이 아직 눌리지 않았을 때) ---

if not st.session_state.quiz_data and not st.session_state.submitted:
    st.info("왼쪽 사이드바의 **'문제 생성'** 버튼을 눌러 퀴즈를 시작하세요.")

