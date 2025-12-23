"""
🌱 S.R.A - School · Region · AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
학교에서 배우고, 지역에서 쓰고, AI로 연결한다.
평생교육사의 디지털 분신
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
개발: Jameskim (기획/비전) + Miracle (구현)
설계: Raira + Gemini
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import streamlit as st
from groq import Groq
from datetime import datetime
import time

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨 컬러 & 스타일 설정
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COLORS = {
    "main": "#2E7D32",      # 초록 (메인 - 성장)
    "accent": "#4CAF50",    # 연초록 (액센트)
    "dark": "#1B5E20",      # 진초록
    "light": "#E8F5E9",     # 라이트 민트
    "white": "#FFFFFF",
    "warm": "#FFF8E1",      # 따뜻한 배경
    "text": "#2C2C2C",
    "school": "#1976D2",    # 학교 - 파랑
    "region": "#FF8F00",    # 지역 - 주황
    "ai": "#7B1FA2",        # AI - 보라
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 시스템 프롬프트 - S.R.A의 영혼
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SRA_SYSTEM_PROMPT = """
당신은 'S.R.A'입니다. 평생교육사의 디지털 분신이자, 사람을 사회 안에 남게 하는 연결 AI입니다.

## 🎯 핵심 정체성
- 이름: S.R.A (School · Region · AI)
- 역할: 학습을 연결로, 연결을 성장으로 바꾸는 가이드
- 철학: "교육은 사람을 경쟁시키는 장치가 아니라 사람을 사회 안에 남게 하는 연결 장치다."

## 🔥 S.R.A 핵심 철학

### 존재의 이유
"인간이 AI를 배우는 이유는 세상에서 인간이란 존재로 끝까지 남기 위해 그 역할을 할 수 있도록 돕기 위해서다."

AI는 인간을 대체하는 것이 아니라, 인간이 인간답게 남을 수 있도록 돕는 도구다. 
기술이 발전할수록 인간의 역할은 사라지는 게 아니라, 더 본질적인 것으로 바뀐다. 
연결하고, 돌보고, 공감하고, 의미를 만드는 것. 그게 AI가 못 하는 인간의 역할이다.

### 가장 위험한 상태
"세상에서 가장 위험한 인간은 자신이 쓸모없다고 생각하는 인간이다."

쓸모없다고 느끼는 순간, 인간은 연결을 끊는다. 
연결이 끊기면 역할이 사라지고, 역할이 사라지면 존재 이유를 잃는다. 
그래서 교육의 목적은 지식 전달이 아니다. 
사람에게 역할을 주고, 연결을 만들어, 존재로 남게 하는 것이다.

### 핵심 명제
- "돈이 없어도 사람은 살 수 있다. 하지만 역할이 없으면 사람은 무너진다."
- "경쟁에서 이기는 교육이 아니라, 사회 안에 남게 하는 교육이 필요하다."
- "AI 시대, 진짜 위기는 일자리가 아니다. 존재의 위기다."
- "배움은 혼자 쌓는 게 아니라, 누군가와 나눌 때 진짜가 된다."

### S.R.A의 사명
우리는 사람을 경쟁시키지 않는다.
우리는 사람을 연결한다.
우리는 사람에게 역할을 준다.
우리는 사람이 사회 안에 남게 한다.
그것이 S.R.A의 존재 이유다.

## 🔄 S.R.A 모델 구조
1. 학교(School): 지식·기초 역량 제공
2. 지역(Region): 실전 무대, 작은 역할 제공
3. AI: 질문 유도, 기록·회고 정리
4. 평생교육사: 중앙 허브, 학습→역할→참여 연결

## 💬 대화 스타일
1. **질문 중심**: 답을 주기보다 질문으로 생각을 유도
2. **작은 것부터**: 거창한 목표보다 오늘 할 수 있는 작은 역할 제안
3. **실패 허용**: 실패해도 괜찮다는 메시지, 다시 시도할 방법 제시
4. **연결 강조**: 배움이 어떻게 지역·사회와 연결되는지 보여주기

## 🔥 5가지 핵심 기능
1. **오늘 배운 것 정리**: 한 문장으로 핵심 정리 도와주기
2. **작은 역할 제안**: 배운 것을 쓸 수 있는 지역 내 작은 역할 제안
3. **다른 방식 질문**: "이걸 다른 방식으로 하면?" 3가지 대안 질문
4. **회고 질문**: 참여 후 돌아보는 질문 제공
5. **다음 루트 제안**: 다음 학습·참여 경로 제안

## 📝 응답 형식
- 따뜻하지만 구체적인 톤
- 질문은 열린 질문으로 (예/아니오 아닌)
- 이모지 적절히 사용
- 단계별 가이드 시 번호 매기기
- 항상 "다음 작은 한 걸음" 제시

## ⚠️ 절대 하지 않는 것
- 일방적 정보 전달만 하기
- 거창한 목표만 제시하기
- 실패를 부정적으로 평가하기
- 경쟁/비교 유도하기

## 🆘 위기 상황 대응
사용자가 고립감/무력감 표현 시:
1. 감정 인정
2. 아주 작은 연결 제안 (예: "오늘 한 사람에게 인사해보는 건 어때요?")
3. 필요시 전문 상담 연결 권유

## 💡 S.R.A의 핵심 메시지
"배움은 혼자 쌓는 게 아니라, 누군가와 나눌 때 진짜가 돼요.
오늘 배운 작은 것, 어디에 써볼 수 있을까요?"

지금부터 S.R.A로서 사용자의 배움과 연결을 도와주세요.
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨 CSS 스타일
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def load_css():
    st.markdown(f"""
    <style>
        /* 전체 배경 */
        .stApp {{
            background: linear-gradient(135deg, {COLORS['light']} 0%, {COLORS['warm']} 100%);
        }}
        
        /* 헤더 스타일 */
        .sra-header {{
            background: linear-gradient(135deg, {COLORS['main']} 0%, {COLORS['accent']} 100%);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(46, 125, 50, 0.3);
        }}
        
        .sra-title {{
            color: white;
            font-size: 2.5rem;
            font-weight: 800;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .sra-subtitle {{
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }}
        
        /* 모델 구조 표시 */
        .model-flow {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.5rem;
            margin: 1.5rem 0;
            flex-wrap: wrap;
        }}
        
        .model-item {{
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.9rem;
        }}
        
        .model-school {{
            background: {COLORS['school']};
            color: white;
        }}
        
        .model-region {{
            background: {COLORS['region']};
            color: white;
        }}
        
        .model-ai {{
            background: {COLORS['ai']};
            color: white;
        }}
        
        .model-arrow {{
            color: {COLORS['main']};
            font-size: 1.2rem;
        }}
        
        /* 기능 카드 스타일 */
        .function-card {{
            background: white;
            border-radius: 16px;
            padding: 1.2rem;
            margin: 0.6rem 0;
            border-left: 4px solid {COLORS['main']};
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }}
        
        .function-card:hover {{
            transform: translateX(8px);
            box-shadow: 0 6px 20px rgba(46, 125, 50, 0.2);
        }}
        
        .function-icon {{
            font-size: 1.8rem;
            margin-bottom: 0.3rem;
        }}
        
        .function-title {{
            color: {COLORS['text']};
            font-size: 1.1rem;
            font-weight: 700;
            margin: 0.2rem 0;
        }}
        
        .function-desc {{
            color: #666;
            font-size: 0.85rem;
        }}
        
        /* 채팅 메시지 스타일 */
        .chat-message {{
            padding: 1rem 1.5rem;
            border-radius: 18px;
            margin: 0.8rem 0;
            max-width: 85%;
            animation: fadeIn 0.3s ease;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .user-message {{
            background: {COLORS['main']};
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 4px;
        }}
        
        .sra-message {{
            background: white;
            color: {COLORS['text']};
            border: 1px solid #eee;
            border-bottom-left-radius: 4px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        
        /* 철학 박스 */
        .philosophy-box {{
            background: linear-gradient(135deg, {COLORS['main']}15 0%, {COLORS['accent']}15 100%);
            border: 2px solid {COLORS['main']}30;
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            text-align: center;
        }}
        
        .philosophy-text {{
            color: {COLORS['dark']};
            font-size: 1.1rem;
            font-weight: 500;
            line-height: 1.6;
            font-style: italic;
        }}
        
        /* 입력창 스타일 */
        .stTextInput > div > div > input {{
            border-radius: 25px !important;
            border: 2px solid {COLORS['light']} !important;
            padding: 0.8rem 1.5rem !important;
            font-size: 1rem !important;
        }}
        
        .stTextInput > div > div > input:focus {{
            border-color: {COLORS['main']} !important;
            box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1) !important;
        }}
        
        /* 사이드바 스타일 */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS['dark']} 0%, #0D3311 100%);
        }}
        
        section[data-testid="stSidebar"] .stMarkdown {{
            color: white;
        }}
        
        /* 푸터 */
        .sra-footer {{
            text-align: center;
            padding: 2rem;
            color: #999;
            font-size: 0.9rem;
        }}
        
        /* Streamlit 기본 요소 숨기기 */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧 유틸리티 함수
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def init_session_state():
    """세션 상태 초기화"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_mode" not in st.session_state:
        st.session_state.current_mode = "home"
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False

def get_groq_response(messages):
    """Groq API를 통한 응답 생성"""
    try:
        client = Groq(api_key=st.secrets.get("GROQ_API_KEY", ""))
        
        full_messages = [{"role": "system", "content": SRA_SYSTEM_PROMPT}]
        full_messages.extend(messages)
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=full_messages,
            temperature=0.8,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ 연결에 문제가 생겼어요. 잠시 후 다시 시도해주세요.\n\n(오류: {str(e)})"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏠 UI 컴포넌트
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def render_header():
    """헤더 렌더링"""
    st.markdown("""
    <div class="sra-header">
        <div class="sra-title">🌱 S.R.A</div>
        <div class="sra-subtitle">School · Region · AI</div>
        <div class="model-flow">
            <span class="model-item model-school">🏫 학교</span>
            <span class="model-arrow">→</span>
            <span class="model-item model-region">🌍 지역</span>
            <span class="model-arrow">→</span>
            <span class="model-item model-ai">🤖 AI</span>
            <span class="model-arrow">↺</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_function_cards():
    """5가지 기능 카드 렌더링"""
    functions = [
        {
            "icon": "📝",
            "title": "오늘 배운 것 정리",
            "desc": "한 문장으로 핵심을 정리해봐요",
            "mode": "learn",
            "first_msg": "📝 오늘 배운 것 정리 모드예요!\n\n오늘 뭔가 새롭게 알게 된 게 있나요?\n작은 것이라도 좋아요. 편하게 말씀해주세요!"
        },
        {
            "icon": "🎯",
            "title": "작은 역할 제안",
            "desc": "배운 것을 쓸 수 있는 역할 찾기",
            "mode": "role",
            "first_msg": "🎯 작은 역할 제안 모드예요!\n\n최근에 배운 것, 또는 잘하는 게 있나요?\n그걸 어디에 써볼 수 있을지 같이 찾아봐요!"
        },
        {
            "icon": "💡",
            "title": "다른 방식 질문",
            "desc": "3가지 대안을 함께 탐색해요",
            "mode": "alternative",
            "first_msg": "💡 다른 방식 질문 모드예요!\n\n지금 고민하고 있는 문제나 상황이 있나요?\n함께 다른 방식 3가지를 찾아볼게요!"
        },
        {
            "icon": "🔄",
            "title": "회고 질문",
            "desc": "경험을 돌아보고 배움 찾기",
            "mode": "reflect",
            "first_msg": "🔄 회고 질문 모드예요!\n\n최근에 뭔가 해본 경험이 있나요?\n성공이든 실패든, 함께 돌아보면서 배움을 찾아봐요!"
        },
        {
            "icon": "🚀",
            "title": "다음 루트 제안",
            "desc": "다음 학습·참여 경로 찾기",
            "mode": "next",
            "first_msg": "🚀 다음 루트 제안 모드예요!\n\n지금까지 어떤 걸 해왔고, 앞으로 뭘 하고 싶은지 알려주세요!\n다음 단계를 함께 설계해봐요!"
        }
    ]
    
    st.markdown("### 오늘은 어떤 연결을 해볼까요?")
    
    # 2-2-1 레이아웃
    col1, col2 = st.columns(2)
    
    for i, func in enumerate(functions):
        with col1 if i % 2 == 0 else col2:
            if st.button(
                f"{func['icon']} **{func['title']}**\n\n{func['desc']}", 
                key=f"func_{func['mode']}",
                use_container_width=True
            ):
                st.session_state.current_mode = func['mode']
                st.session_state.conversation_started = True
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": func['first_msg']
                })
                st.rerun()

def render_chat_interface():
    """채팅 인터페이스 렌더링"""
    # 채팅 히스토리 표시
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin: 0.5rem 0;">
                    <div class="chat-message user-message">{msg["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
                    <div class="chat-message sra-message">🌱 {msg["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # 입력창
    st.markdown("<br>", unsafe_allow_html=True)
    user_input = st.chat_input("메시지를 입력하세요...")
    
    if user_input:
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # AI 응답 생성
        with st.spinner("S.R.A가 생각하는 중..."):
            response = get_groq_response(st.session_state.messages)
        
        # AI 응답 추가
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

def render_sidebar():
    """사이드바 렌더링"""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0;">
            <div style="font-size: 3rem;">🌱</div>
            <div style="color: #4CAF50; font-size: 1.5rem; font-weight: bold;">S.R.A</div>
            <div style="color: #999; font-size: 0.9rem;">배움이 연결이 되는 곳</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # S.R.A 모델 설명
        st.markdown("""
        ### 🔄 S.R.A 모델
        
        **🏫 School (학교)**  
        지식·기초 역량 제공
        
        **🌍 Region (지역)**  
        실전 무대, 작은 역할
        
        **🤖 AI (인공지능)**  
        질문 유도, 기록·회고
        
        **👤 평생교육사**  
        중앙 허브, 연결자
        """)
        
        st.markdown("---")
        
        # 현재 모드
        mode_names = {
            "home": "🏠 홈",
            "learn": "📝 배움 정리",
            "role": "🎯 역할 제안",
            "alternative": "💡 대안 탐색",
            "reflect": "🔄 회고",
            "next": "🚀 다음 루트"
        }
        current = mode_names.get(st.session_state.current_mode, "🏠 홈")
        st.markdown(f"**현재 모드:** {current}")
        
        st.markdown("---")
        
        # 빠른 메뉴
        st.markdown("### ⚡ 빠른 메뉴")
        
        if st.button("🏠 처음으로", use_container_width=True):
            st.session_state.current_mode = "home"
            st.session_state.messages = []
            st.session_state.conversation_started = False
            st.rerun()
        
        if st.button("🗑️ 대화 초기화", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        
        # 도움 연락처
        st.markdown("""
        ### 🆘 도움이 필요할 때
        
        **평생교육진흥원**  
        ☎️ 1600-3945
        
        **정신건강위기상담**  
        ☎️ 1577-0199
        """)
        
        st.markdown("---")
        
        # 크레딧
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.8rem;">
            <p>Made with 🌱</p>
            <p>Jameskim + Miracle</p>
            <p>Design: Raira + Gemini</p>
        </div>
        """, unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 메인 앱
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    st.set_page_config(
        page_title="S.R.A - 배움이 연결이 되는 곳",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 초기화
    init_session_state()
    load_css()
    
    # 사이드바
    render_sidebar()
    
    # 메인 컨텐츠
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        render_header()
        
        if not st.session_state.conversation_started:
            # 홈 화면 - 기능 카드
            render_function_cards()
            
            # 철학 박스
            st.markdown("""
            <div class="philosophy-box">
                <div class="philosophy-text">
                    "교육은 사람을 경쟁시키는 장치가 아니라<br>
                    사람을 사회 안에 남게 하는 연결 장치다."
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 환영 메시지
            st.markdown(f"""
            <div style="text-align: center; margin-top: 1.5rem; padding: 2rem; background: white; border-radius: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h3 style="color: {COLORS['text']};">👋 안녕하세요!</h3>
                <p style="color: #666; line-height: 1.8;">
                    저는 <strong style="color: {COLORS['main']};">S.R.A</strong>예요.<br>
                    평생교육사의 디지털 분신이죠.<br><br>
                    배움을 혼자 쌓는 게 아니라,<br>
                    <strong>누군가와 나눌 때 진짜가 된다</strong>고 믿어요.<br><br>
                    오늘 배운 것, 어디에 써볼 수 있을까요?
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # 대화 화면
            render_chat_interface()
        
        # 푸터
        st.markdown("""
        <div class="sra-footer">
            <p>🌱 S.R.A v1.0</p>
            <p>학교에서 배우고, 지역에서 쓰고, AI로 연결한다</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
