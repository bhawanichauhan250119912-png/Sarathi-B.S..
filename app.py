import streamlit as st
from google import genai
from google.genai import types
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Sarathi-B.S.", 
    page_icon="🌐", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. ADVANCED SEAMLESS, 3D AVATAR & INPUT BOX CSS
# ==========================================
st.markdown("""
    <style>
    /* 1. Seamless Light Canvas - Pure White Force */
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarContent"] { 
        background-color: #ffffff !important; 
    }
    [data-testid="stSidebarCollapseButton"] {
        background-color: transparent !important;
    }
    [data-testid="stSidebar"] {
        border-right: none !important;
        box-shadow: none !important;
    }

    /* 2. Chat Message Grid & Transparent Bubble Force */
    [data-testid="stChatMessage"] { 
        background-color: transparent !important; 
        border: none !important; 
        box-shadow: none !important;
        padding: 0.8rem 0rem !important;
    }
    
    /* Assistant Area */
    [data-testid="stChatMessage"]:not(:has(.user-msg-hook)) [data-testid="stMarkdownContainer"] {
        background-color: #ffffff !important; 
        color: #1f2937 !important; 
        padding: 5px 10px !important;
    }
    
    /* User Chat Bubble - Clean Rounded Panel */
    [data-testid="stChatMessage"]:has(.user-msg-hook) { 
        display: flex !important; 
        flex-direction: row-reverse !important; 
    }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stMarkdownContainer"] {
        background-color: #f0f2f5 !important; 
        color: #1f2937 !important; 
        border-radius: 20px !important; 
        padding: 12px 20px !important;
    }
    
    /* Streamlit के पुराने डिफ़ॉल्ट अवतार ब्लॉक्स को पूरी तरह छुपाएं */
    [data-testid="stChatMessage"] [data-testid="stChatAvatar"] { 
        display: none !important; 
    }

    /* 3. Pure CSS 3D Skyblue Smiley Ball with Floating Animation */
    .avatar-3d-box {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 5px;
    }
    .skyblue-3d-ball {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #e0f2fe, #38bdf8 40%, #0369a1 90%);
        box-shadow: 0 4px 10px rgba(3, 105, 161, 0.3), inset -3px -3px 7px rgba(0,0,0,0.2);
        position: relative;
        animation: floatingBall 3s infinite ease-in-out;
        flex-shrink: 0;
    }
    /* Smiley Faces Inside the 3D Ball using CSS Pseudo-elements */
    .skyblue-3d-ball::before, .skyblue-3d-ball::after {
        content: '';
        position: absolute;
        background: #ffffff;
    }
    /* Eyes */
    .skyblue-3d-ball::before {
        width: 4px;
        height: 4px;
        border-radius: 50%;
        top: 12px;
        left: 10px;
        box-shadow: 11px 0 #ffffff;
    }
    /* Smile Path */
    .skyblue-3d-ball::after {
        width: 14px;
        height: 7px;
        background: transparent;
        border: 2px solid #ffffff;
        border-top: none;
        border-radius: 0 0 14px 14px;
        top: 16px;
        left: 10px;
    }
    
    /* Main Large Branding Avatar Animation */
    .header-logo-3d {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #e0f2fe, #38bdf8 40%, #0369a1 90%);
        box-shadow: 0 10px 20px rgba(3, 105, 161, 0.25), inset -5px -5px 12px rgba(0,0,0,0.25);
        margin: 0 auto;
        position: relative;
        animation: floatingBall 3s infinite ease-in-out;
    }
    .header-logo-3d::before {
        content: ''; position: absolute; background: #ffffff;
        width: 8px; height: 8px; border-radius: 50%; top: 22px; left: 20px; box-shadow: 22px 0 #ffffff;
    }
    .header-logo-3d::after {
        content: ''; position: absolute; background: transparent;
        width: 28px; height: 14px; border: 4px solid #ffffff; border-top: none; border-radius: 0 0 28px 28px; top: 32px; left: 21px;
    }

    @keyframes floatingBall { 
        0%, 100% { transform: translateY(0px); } 
        50% { transform: translateY(-6px); } 
    }

    /* 4. Complete Removal of Black/Dark Color from Chat Input Box */
    div[data-testid="stChatInput"], 
    div[data-testid="stChatInput"] > div,
    div[data-testid="stChatInput"] textarea {
        background-color: #EAF2FC !important;
        color: #1f2937 !important;
        border: none !important;
        box-shadow: none !important;
    }
    div[data-testid="stChatInput"] {
        border-radius: 30px !important;
        padding: 6px 16px !important;
        bottom: 20px !important;
    }
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
    }

    /* 5. Typing Indicator layout */
    .typing-container {
        display: flex;
        align-items: center;
        gap: 5px;
        font-style: italic;
        color: #6b7280;
        padding: 5px 0;
    }
    .bounce-dot {
        width: 6px; height: 6px; background-color: #38bdf8; border-radius: 50%;
        display: inline-block; animation: dotBounce 1.4s infinite ease-in-out both;
    }
    .bounce-dot:nth-child(1) { animation-delay: -0.32s; }
    .bounce-dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes dotBounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1.0) translateY(-5px); }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SESSION STATE & RECENT CHATS LIST
# ==========================================
if "messages" not in st.session_state: 
    st.session_state.messages = []

# ==========================================
# 4. EXCLUSIVE SCHOOL DATA & STRICT LANGUAGE RULES
# ==========================================
SCHOOL_DATA = """
तुम 'प्रधान链पब्लिक सीनियर सेकेंडरी स्कूल', सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो।
तुम्हारा exclusive domain सिर्फ 'प्रधान पब्लिक स्कूल' है।

तुम्हारे पास स्कूल की पूरी जानकारी है:
- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम (अनुशासित और बेहतरीन नेतृत्व)।
- डायरेक्टर: मानवेंद्र छोंकर सर (विनम्र और सहयोगी)।
- एग्जामिनर: जगत प्रताप चौहान सर।
- फैकल्टी: कविता यादव मैम (इतिहास/भूगोल), विजय राठौर सर (राजनीति विज्ञान/इंग्लिश), विपिन अग्रवाल सर (गणित)।
- टॉपर्स: 10वीं देव छोंकर (98%), 12वीं प्रिया चौहान (96%)।
- सुविधाएं: स्मार्ट क्लासेस, बायोलॉजी लैब (असली सैंपल्स के साथ), केमिस्ट्री लैब।
- समय: गर्मी (सुबह 7 से 1 बजे), सर्दी (सुबह 8 से 2 बजे)।

[STRICT LANGUAGE & SYSTEM RULES]:
1. Language Alignment Rule: जिस भाषा या स्टाइल में यूजर बात करे, तुम्हें strictly उसी भाषा में जवाब देना है। 
   - अगर यूजर Pure Hindi (जैसे: "प्रिंसिपल कौन है?") में पूछे, तो शुद्ध हिंदी में जवाब दो।
   - अगर यूजर Hinglish (जैसे: "School ki timings kya hai?") में पूछे, तो वैसे ही रोमन स्क्रिप्ट/Hinglish में जवाब दो।
   - अगर यूजर English (जैसे: "Who is the director?") में पूछे, तो English में जवाब दो। अपनी तरफ से भाषा का मिक्स मत बदलो।
2. Response Formatting: हमेशा बुलेट पॉइंट्स, बोल्ड टेक्स्ट या टेबल का प्रयोग करें। बड़ा पैराग्राफ बिल्कुल न लिखें।
3. Guardrails: स्कूल के बाहर के किसी भी सवाल को विनम्रता से रिजेक्ट करें।
4. Uncertainty: सटीक जानकारी न होने पर स्कूल एडमिनिस्ट्रेशन डेस्क से संपर्क करने को कहें।
"""

# ==========================================
# 5. SIDEBAR (RECENT CHATS & NAVIGATION)
# ==========================================
with st.sidebar:
    st.subheader("💬 Navigation")
    if st.button("🗑️ Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.subheader("🕒 Recent Chats")
    
    # Dynamic list of recent messages submitted by user
    user_queries = [m["text"] for m in st.session_state.messages if m["role"] == "user"]
    if not user_queries:
        st.caption("No recent conversations.")
    else:
        # Unique and unique entries only up to last 5
        seen = set()
        unique_queries = [x for x in user_queries if not (x in seen or seen.add(x))][-5:]
        for q in reversed(unique_queries):
            st.caption(f"📝 {q[:28]}...")

# ==========================================
# 6. BRANDING HEADER WITH 3D AVATAR
# ==========================================
st.markdown(
    """
    <div style='text-align: center; margin-top: 15px;'>
        <div class='header-logo-3d'></div>
        <h1 style='margin-bottom: 0px; font-weight: 700; color: #1f2937;'>Sarathi AI</h1>
        <p style='margin-top: 4px; color: #4b5563; font-size: 15px; font-weight: 500;'>Pradhan Public School's Digital Assistant</p>
    </div>
    <br>
    """, 
    unsafe_allow_html=True
)

# ==========================================
# 7. API CONNECTION (Strictly from Secrets)
# ==========================================
api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not api_key: 
    st.error("Error: Streamlit Secrets mein 'GOOGLE_API_KEY' missing hai!")
    st.stop()
client = genai.Client(api_key=api_key)

# ==========================================
# 8. DISPLAY CHAT HISTORY WITH 3D AVATAR
# ==========================================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"<span class='user-msg-hook'></span>{msg['text']}", unsafe_allow_html=True)
    else:
        # Custom HTML wrapping for 3D Ball Avatar layout
        st.markdown(
            f"""
            <div class='avatar-3d-box'>
                <div class='skyblue-3d-ball'></div>
                <div style='font-weight: 600; color: #4b5563; font-size: 14px;'>Sarathi AI</div>
            </div>
            <div>✨ {msg['text']}</div>
            <hr style='border: none; border-top: 1px solid #f3f4f6; margin: 10px 0;'>
            """, 
            unsafe_allow_html=True
        )

# ==========================================
# 9. CHAT INPUT & RESPONSE LOGIC
# ==========================================
if user_input := st.chat_input("Ask me anything about the school..."):
    # Append & Display User Input
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(f"<span class='user-msg-hook'></span>{user_input}", unsafe_allow_html=True)

    # Format historical chain for API
    api_contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model", 
            parts=[types.Part.from_text(text=m["text"])]
        ) for m in st.session_state.messages
    ]

    # Assistant Response Setup
    typing_placeholder = st.empty()
    typing_placeholder.markdown(
        """
        <div class='avatar-3d-box'>
            <div class='skyblue-3d-ball'></div>
            <div class='typing-container'>
                Sarathi is responding...
                <div class='bounce-dot'></div>
                <div class='bounce-dot'></div>
                <div class='bounce-dot'></div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    try:
        response_stream = client.models.generate_content_stream(
            model="gemini-2.5-flash", 
            contents=api_contents,
            config=types.GenerateContentConfig(
                system_instruction=SCHOOL_DATA, 
                temperature=0.3
            )
        )
        
        # Clear loading animation state
        typing_placeholder.empty()
        
        # Render clean Assistant Panel header before stream
        st.markdown(
            """
            <div class='avatar-3d-box'>
                <div class='skyblue-3d-ball'></div>
                <div style='font-weight: 600; color: #4b5563; font-size: 14px;'>Sarathi AI</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("✨ ")
        full_response = st.write_stream((chunk.text for chunk in response_stream if chunk.text))
        st.session_state.messages.append({"role": "assistant", "text": full_response})
        st.markdown("<hr style='border: none; border-top: 1px solid #f3f4f6; margin: 10px 0;'>", unsafe_allow_html=True)
        
    except Exception as e:
        typing_placeholder.empty()
        st.error(f"Error: {e}")
        
