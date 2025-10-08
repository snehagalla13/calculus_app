import streamlit as st
import random
import re

# Configure page
st.set_page_config(
    page_title="UNC Calculus Practice",
    page_icon="📚",
    layout="centered"
)

# UNC Colors
UNC_BLUE = "#7BAFD4"
UNC_NAVY = "#13294B"

# Custom styling for UNC theme using inline HTML styles
st.markdown("""
<div style="background: linear-gradient(135deg, #7BAFD4 0%, #4B9CD3 100%); position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
""", unsafe_allow_html=True)

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = {'correct': 0, 'total': 0}
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'feedback' not in st.session_state:
    st.session_state.feedback = None
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ''

# Problem generators
def generate_power_rule():
    coef = random.randint(1, 10)
    power = random.randint(2, 6)
    return {
        'type': 'derivative_power',
        'question': f'Find the derivative of',
        'latex': f'f(x) = {coef}x^{{{power}}}',
        'answer': f'{coef * power}x^{{{power - 1}}}',
        'numeric_coef': coef * power,
        'numeric_power': power - 1,
        'topic': 'Power Rule',
        'resources': [
            ('Khan Academy: Power Rule', 'https://www.khanacademy.org/math/calculus-1/cs1-derivatives-definition-and-basic-rules/cs1-power-rule/v/power-rule'),
            ('Paul\'s Online Notes: Derivatives', 'https://tutorial.math.lamar.edu/classes/calci/DerivativeIntro.aspx')
        ]
    }

def generate_sum_rule():
    c1 = random.randint(2, 9)
    p1 = random.randint(2, 5)
    c2 = random.randint(2, 9)
    p2 = random.randint(1, 3)
    return {
        'type': 'derivative_sum',
        'question': f'Find the derivative of',
        'latex': f'g(x) = {c1}x^{{{p1}}} + {c2}x^{{{p2}}}',
        'answer': f'{c1 * p1}x^{{{p1 - 1}}} + {c2 * p2}x^{{{p2 - 1}}}',
        'topic': 'Sum Rule & Power Rule',
        'resources': [
            ('Khan Academy: Sum Rule', 'https://www.khanacademy.org/math/calculus-1/cs1-derivatives-definition-and-basic-rules/cs1-sum-and-difference-rules/v/sum-rule-for-derivatives'),
            ('Calculus: Sum & Difference Rules', 'https://www.mathsisfun.com/calculus/derivatives-rules.html')
        ]
    }

def generate_basic_limit():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 5)
    answer = a * c + b
    return {
        'type': 'limit_basic',
        'question': f'Evaluate',
        'latex': f'\\lim_{{x \\to {c}}} ({a}x + {b})',
        'answer': str(answer),
        'numeric_answer': answer,
        'topic': 'Basic Limits',
        'resources': [
            ('Khan Academy: Limits Intro', 'https://www.khanacademy.org/math/calculus-1/cs1-limits-and-continuity/cs1-limits-intro/v/introduction-to-limits-hd'),
            ('Paul\'s Notes: Limits', 'https://tutorial.math.lamar.edu/classes/calci/LimitsIntro.aspx')
        ]
    }

def generate_chain_rule():
    outer = random.randint(2, 5)
    inner_c = random.randint(1, 5)
    result_coef = outer * (inner_c ** outer)
    result_power = outer - 1
    return {
        'type': 'chain_rule',
        'question': f'Find the derivative of',
        'latex': f'h(x) = ({inner_c}x)^{{{outer}}}',
        'answer': f'{result_coef}x^{{{result_power}}}',
        'numeric_coef': result_coef,
        'numeric_power': result_power,
        'topic': 'Chain Rule',
        'resources': [
            ('Khan Academy: Chain Rule', 'https://www.khanacademy.org/math/calculus-1/cs1-diff-chain-rule-and-other-advanced-topics/cs1-chain-rule/v/chain-rule-introduction'),
            ('Chain Rule Examples', 'https://www.mathsisfun.com/calculus/derivatives-rules.html')
        ]
    }

def generate_problem():
    generators = [generate_power_rule, generate_sum_rule, generate_basic_limit, generate_chain_rule]
    return random.choice(generators)()

def normalize_answer(ans):
    # Remove all spaces
    ans = ans.replace(' ', '')
    # Handle different formats
    ans = ans.lower()
    return ans

def check_answer(problem, user_ans):
    user_ans = normalize_answer(user_ans)
    correct_ans = normalize_answer(problem['answer'])
    
    if user_ans == correct_ans:
        return True
    
    # For derivative problems, try alternate formats
    if problem['type'] in ['derivative_power', 'chain_rule']:
        alt = f"{problem['numeric_coef']}x^{problem['numeric_power']}"
        alt2 = f"{problem['numeric_coef']}x^{{{problem['numeric_power']}}}"
        if user_ans == normalize_answer(alt) or user_ans == normalize_answer(alt2):
            return True
    
    # For limits, check numeric value
    if problem['type'] == 'limit_basic':
        try:
            if float(user_ans) == problem['numeric_answer']:
                return True
        except:
            pass
    
    return False

def new_problem():
    st.session_state.current_problem = generate_problem()
    st.session_state.feedback = None
    st.session_state.user_answer = ''

# Header
st.markdown("""
<div style="background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 2rem;">
    <h1 style='color: #13294B; margin: 0;'>📚 UNC Calculus Practice</h1>
    <p style='color: #666; margin-top: 0.5rem;'>Master Calculus 1 with randomly generated problems</p>
</div>
""", unsafe_allow_html=True)

# Score display
col1, col2, col3 = st.columns([2, 1, 1])
with col2:
    st.metric("Correct", st.session_state.score['correct'])
with col3:
    st.metric("Total", st.session_state.score['total'])

# Generate initial problem
if st.session_state.current_problem is None:
    new_problem()

problem = st.session_state.current_problem

# Problem display
st.markdown(f"""
<div style="background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 2rem;">
    <div style="background-color: #7BAFD4; color: white; padding: 0.5rem 1rem; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 1rem;">{problem['topic']}</div>
    <p style='font-size: 1.1rem; color: #333; margin-bottom: 1rem;'>{problem['question']}</p>
</div>
""", unsafe_allow_html=True)

# Display LaTeX
st.latex(problem['latex'])

# Answer input
if st.session_state.feedback is None:
    user_answer = st.text_input(
        "Your Answer:",
        value=st.session_state.user_answer,
        placeholder="Enter your answer (e.g., 6x^2 or 15)",
        help="Use ^ for exponents (e.g., x^2 for x²)",
        key="answer_input"
    )
    
    if st.button("Check Answer", disabled=not user_answer.strip()):
        is_correct = check_answer(problem, user_answer)
        st.session_state.score['total'] += 1
        if is_correct:
            st.session_state.score['correct'] += 1
        st.session_state.feedback = {
            'correct': is_correct,
            'user_answer': user_answer
        }
        st.rerun()
else:
    # Show feedback
    if st.session_state.feedback['correct']:
        st.markdown("""
        <div style="background-color: #d4edda; border: 2px solid #28a745; padding: 1.5rem; border-radius: 10px; margin-top: 1rem;">
            <h3 style='color: #155724; margin-top: 0;'>✅ Excellent Work!</h3>
            <p style='color: #155724; margin-bottom: 0;'>You're mastering calculus! Keep up the great work, Tar Heel! 🐏</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color: #f8d7da; border: 2px solid #dc3545; padding: 1.5rem; border-radius: 10px; margin-top: 1rem;">
            <h3 style='color: #721c24; margin-top: 0;'>❌ Not Quite Right</h3>
            <p style='color: #721c24;'>The correct answer is:</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(problem['answer'])
        
        st.markdown("### 📚 Helpful Resources:")
        for title, url in problem['resources']:
            st.markdown(f"- [{title}]({url})")
    
    if st.button("Next Problem"):
        new_problem()
        st.rerun()

# Instructions at bottom
with st.expander("ℹ️ How to Use"):
    st.markdown("""
    1. **Read the problem** and the equation displayed
    2. **Enter your answer** in the text box (use ^ for exponents, like `6x^2`)
    3. **Click "Check Answer"** to see if you're correct
    4. If incorrect, you'll see the correct answer and helpful learning resources
    5. **Click "Next Problem"** to practice more!
    
    **Tips:**
    - For derivatives, write your answer like: `12x^3` or `6x^2 + 4x`
    - For limits, just enter the numeric value: `15`
    - Practice makes perfect! 💙
    """)