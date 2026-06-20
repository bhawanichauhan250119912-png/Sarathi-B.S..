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
# 2. SEAMLESS INTERFACE & GRAPHICS CSS
# ==========================================
st.markdown("""
    <style>
    /* Pure White Seamless App Background */
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

    /* Hide Native Chat Blocks to Prevent Conflicting Styles */
    [data-testid="stChatMessage"] { 
        background-color: transparent !important; 
        border: none !important; 
        box-shadow: none !important;
        padding: 0px !important;
    }
    [data-testid="stChatMessage"] [data-testid="stChatAvatar"] { 
        display: none !important; 
    }
    
    /* User Chat Bubble - Clean Shaded Capsule aligned to Right */
    .user-box-layout {
        display: flex;
        justify-content: flex-end;
        margin: 12px 0;
    }
    .user-bubble {
        background-color: #f0f2f5 !important;
        color: #1f2937 !important;
        border-radius: 20px !important;
        padding: 12px 20px !important;
        max-width: 80%;
        font-weight: 500;
    }

    /* Assistant Shaded Response Box (Like Professional UI) */
    .assistant-wrapper {
        margin: 18px 0;
        padding: 16px;
        background-color: #f8fafc !important; /* Shaded Box Portion */
        border-radius: 16px;
        border: 1px solid #e2e8f0;
    }
    .assistant-text-container {
        color: #1f2937 !important;
        font-size: 15px;
        line-height: 1.6;
    }
    .assistant-text-container p, .assistant-text-container li {
        color: #1f2937 !important;
    }

    /* Pure CSS 3D Skyblue Smiley Ball with Floating Animation */
    .avatar-3d-box {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .skyblue-3d-ball {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #e0f2fe, #38bdf8 40%, #0369a1 90%);
        box-shadow: 0 4px 8px rgba(3, 105, 161, 0.25);
        position: relative;
        flex-shrink: 0;
    }
    .skyblue-3d-ball::before {
        content: ''; position: absolute; background: #ffffff;
        width: 3.5px; height: 3.5px; border-radius: 50%; top: 11px; left: 9px; box-shadow: 10px 0 #ffffff;
    }
    .skyblue-3d-ball::after {
        content: ''; position: absolute; background: transparent;
        width: 12px; height: 6px; border: 2px solid #ffffff; border-top: none; border-radius: 0 0 12px 12px; top: 15px; left: 10px;
    }
    
    /* Main Header Large 3D Avatar */
    .header-logo-3d {
        width: 75px; height: 75px; border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #e0f2fe, #38bdf8 40%, #0369a1 90%);
        box-shadow: 0 10px 20px rgba(3, 105, 161, 0.2), inset -4px -4px 10px rgba(0,0,0,0.2);
        margin: 0 auto; position: relative; animation: floatingBall 3.5s infinite ease-in-out;
    }
    .header-logo-3d::before {
        content: ''; position: absolute; background: #ffffff; width: 8px; height: 8px; border-radius: 50%; top: 24px; left: 22px; box-shadow: 22px 0 #ffffff;
    }
    .header-logo-3d::after {
        content: ''; position: absolute; background: transparent; width: 26px; height: 13px; border: 3.5px solid #ffffff; border-top: none; border-radius: 0 0 26px 28px; top: 34px; left: 23px;
    }

    @keyframes floatingBall { 
        0%, 100% { transform: translateY(0px); } 
        50% { transform: translateY(-6px); } 
    }

    /* Flashing / Glowing Welcome Text Animation Below Avatar */
    .glowing-welcome {
        font-size: 16px;
        font-weight: 700;
        color: #0284c7;
        margin-top: 10px;
        letter-spacing: 0.5px;
        animation: flashWelcome 2s infinite ease-in-out;
    }
    @keyframes flashWelcome {
        0%, 100% { opacity: 0.6; transform: scale(0.98); filter: drop-shadow(0 0 2px rgba(56,189,248,0)); }
        50% { opacity: 1; transform: scale(1.02); filter: drop-shadow(0 0 8px rgba(56,189,248,0.5)); color: #0369a1; }
    }

    /* FIXED: Chat Input Box Typography & Layout */
    div[data-testid="stChatInput"] {
        background-color: #EAF2FC !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        border-radius: 30px !important;
        padding: 4px 12px !important;
        bottom: 20px !important;
    }
    /* Strictly target input text area for crisp black color on white canvas */
    div[data-testid="stChatInput"] textarea {
        background-color: transparent !important;
        color: #1f2937 !important; 
        font-size: 15px !important;
    }
    /* Sky Blue Send Icon button overrides */
    div[data-testid="stChatInput"] button svg {
        fill: #38bdf8 !important;
        color: #38bdf8 !important;
    }
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
    }

    /* Typing Indicator Inside Shaded Portion */
    .typing-container {
        display: flex; align-items: center; gap: 5px; font-style: italic; color: #6b7280;
    }
    .bounce-dot {
        width: 6px; height: 6px; background-color: #38bdf8; border-radius: 50%; display: inline-block; animation: dotBounce 1.4s infinite ease-in-out both;
    }
    .bounce-dot:nth-child(1) { animation-delay: -0.32s; }
    .bounce-dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes dotBounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1.0) translateY(-4px); }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SESSION STATE
# ==========================================
if "messages" not in st.session_state: 
    st.session_state.messages = []

# ==========================================
# 4. EXCLUSIVE SCHOOL KNOWLEDGE & LANGUAGE RULES
# ==========================================
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल', सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो।
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
# 5. SIDEBAR (NAVIGATION & RECENT CHATS)
# ==========================================
with st.sidebar:
    st.subheader("💬 Navigation")
    if st.button("🗑️ Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.subheader("🕒 Recent Chats")
    
    user_queries = [m["text"] for m in st.session_state.messages if m["role"] == "user"]
    if not user_queries:
        st.caption("No recent conversations.")
    else:
        seen = set()
        unique_queries = [x for x in user_queries if not (x in seen or seen.add(x))][-5:]
        for q in reversed(unique_queries):
            st.caption(f"📝 {q[:28]}...")

# ==========================================
# 6. BRANDING HEADER WITH FLASHING ANIMATION
# ==========================================
st.markdown(
    """
    <div style='text-align: center; margin-top: 15px;'>
        <div class='header-logo-3d'></div>
        <div class='glowing-welcome'>✨ Welcome to P.P.S Senior Secondary School ✨</div>
        <h1 style='margin-bottom: 0px; font-weight: 700; color: #1f2937; margin-top: 5px;'>Sarathi AI</h1>
        <p style='margin-top: 4px; color: #4b5563; font-size: 14px; font-weight: 500;'>Pradhan Public School's Digital Assistant</p>
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
# 8. DISPLAY LOGGED CHAT HISTORY
# ==========================================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class='user-box-layout'>
                <div class='user-bubble'>{msg['text']}</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class='assistant-wrapper'>
                <div class='avatar-3d-box'>
                    <div class='skyblue-3d-ball'></div>
                    <div style='font-weight: 600; color: #4b5563; font-size: 14px;'>Sarathi AI</div>
                </div>
                <div class='assistant-text-container'>✨ {msg['text']}</div>
            </div>
            """, 
            unsafe_allow_html=True
        )

# ==========================================
# 9. CHAT INPUT & STREAM RESPONSE LOGIC
# ==========================================
if user_input := st.chat_input("Ask me anything about the school..."):
    # Render User Input Immediately
    st.session_state.messages.append({"role": "user", "text": user_input})
    st.markdown(
        f"""
        <div class='user-box-layout'>
            <div class='user-bubble'>{user_input}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Context compilation
    api_contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model", 
            parts=[types.Part.from_text(text=m["text"])]
        ) for m in st.session_state.messages
    ]

    # Render Shaded Assistant Block Shell with Loader
    response_placeholder = st.empty()
    response_placeholder.markdown(
        """
        <div class='assistant-wrapper'>
            <div class='avatar-3d-box'>
                <div class='skyblue-3d-ball'></div>
                <div class='typing-container'>
                    Sarathi is responding...
                    <div class='bounce-dot'></div>
                    <div class='bounce-dot'></div>
                    <div class='bounce-dot'></div>
                </div>
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
        
        # Wipe loading state
        response_placeholder.empty()
        
        # Build Container for Shaded Area block containing Stream
        with st.container():
            st.markdown(
                """
                <div class='avatar-3d-box' style='margin-top:15px;'>
                    <div class='skyblue-3d-ball'></div>
                    <div style='font-weight: 600; color: #4b5563; font-size: 14px;'>Sarathi AI</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Text outputs stream crisp black inside the container nicely
            full_response = st.write_stream((chunk.text for chunk in response_stream if chunk.text))
            st.session_state.messages.append({"role": "assistant", "text": full_response})
            st.markdown("<br><hr style='border: none; border-top: 1px solid #e2e8f0; margin: 5px 0;'>", unsafe_allow_html=True)
            
    except Exception as e:
        response_placeholder.empty()
        st.error(f"Error: {e}")
        
