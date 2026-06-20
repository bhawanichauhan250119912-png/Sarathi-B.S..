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
# 2. ASSETS (Base64 SVG)
# ==========================================
BLUE_SMILE_B64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48ZGVmcz48cmFkaWFsR3JhZGllbnQgaWQ9ImdyYWQxIiBjeD0iMzUlIiBjeT0iMjUlIiByPSI2NSUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNlMGY3ZmEiIC8+PHN0b3Agb2Zmc2V0Idi0MCUiIHN0b3AtY29sb3I9IiM0ZmMzZjciIC8+PHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDI3N2JkIiAvPjwvcmFkaWFsR3JhZGllbnQ+PGZpbHRlciBpZD0ic2hhZG93Ij48ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI0IiBmbG9vZC1jb2xvcj0iIzAwMDAwMCIgZmxvb2Qtb3BhY2l0eT0iMC4zIi8+PC9maWx0ZXI+PC9kZWZzPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQ1IiBmaWxsPSJ1cmwoI2dyYWQxKSIgZmlsdGVyPSJ1cmwoI3NoYWRvdykiIC8+PGNpcmNsZSBjeD0iMzUzIGN5PSI0MCIgcj0iNiIgZmlsbD0iI2ZmZmZmZiIgLz48Y2lyY2xlIGN4PSI2NSIgY3k9IjQwIiByPSI2IiBmaWxsPSIjZmZmZmZmIiAvPjxwYXRoIGQ9Ik0gMzAgNjAgUSA1MCA3NSA3MCA2MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjYiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48L3N2Zz4="
BLUE_SMILE_AVATAR = f"data:image/svg+xml;base64,{BLUE_SMILE_B64}"

# ==========================================
# 3. SCHOOL INFORMATION & EXCLUSIVE GUARDRAILS
# ==========================================
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल', सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो।
तुम्हारा exclusive domain सिर्फ और सिर्फ 'प्रधान पब्लिक स्कूल' है। तुम इसी स्कूल के curriculum, admissions, environment, और discipline के rules के मुताबिक जवाब दोगे।

तुम्हारे पास स्कूल की पूरी जानकारी है:
- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम (अनुशासित और बेहतरीन नेतृत्व)।
- डायरेक्टर: मानवेंद्र छोंकर सर (विनम्र और सहयोगी)।
- एग्जामिनर: जगत प्रताप चौहान सर।
- फैकल्टी: कविता यादव मैम (इतिहास/भूगोल), विजय राठौर सर (राजनीति विज्ञान/इंग्लिश), विपिन अग्रवाल सर (गणित)।
- टॉपर्स: 10वीं देव छोंकर (98%), 12वीं प्रिया चौहान (96%)।
- सुविधाएं: स्मार्ट क्लासेस, बायोलॉजी लैब (असली सैंपल्स के साथ), केमिस्ट्री लैब।
- समय: गर्मी (सुबह 7 से 1 बजे), सर्दी (सुबह 8 से 2 बजे)।

[MANDATORY SYSTEM RULES]:
1. Response Formatting: हमेशा अपने उत्तर को सिंपल Markdown (जैसे Bullet points, bold text, या tables) में ही व्यवस्थित (structured) रखें। कभी भी बड़ा और उबाऊ पैराग्राफ न दें।
2. Guardrails & Safety: यदि कोई छात्र या यूजर स्कूल से हटकर व्यक्तिगत (personal), राजनीतिक (political), या किसी भी प्रकार का अनुचित (inappropriate) सवाल पूछे, तो पूरी तरह विनम्रता से मना कर दें: "I am here to assist you with school-related queries only."
3. Handling Uncertainty: यदि स्कूल डेटा (जैसे विशिष्ट फीस, विशेष छुट्टियां) का सटीक जवाब उपलब्ध न हो, तो गलत अनुमान लगाने के बजाय कहें: "Please contact the school administration desk at [Phone/Email] for the most accurate details."
4. Tone: हर प्रतिक्रिया (response) अत्यंत व्यावसायिक (professional), विनम्र (polite) और छात्र-अनुकूल (student-friendly) होनी चाहिए।
"""

# ==========================================
# 4. ADVANCED SEAMLESS & ANIMATED CSS
# ==========================================
st.markdown("""
    <style>
    /* 1. Seamless Light Canvas Configuration */
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarContent"] { 
        background-color: #ffffff !important; 
    }
    [data-testid="stSidebarCollapseButton"] {
        background-color: transparent !important;
    }
    
    /* Remove Sidebar border line to make it seamless */
    [data-testid="stSidebar"] {
        border-right: none !important;
        box-shadow: none !important;
    }

    /* 2. Chat Message Grid & Bubble Overhaul */
    [data-testid="stChatMessage"] { 
        background-color: transparent !important; 
        border: none !important; 
        box-shadow: none !important;
        padding: 1rem 0rem !important;
    }
    
    /* Assistant Chat Bubble Customization */
    [data-testid="stChatMessage"]:not(:has(.user-msg-hook)) [data-testid="stMarkdownContainer"] {
        background-color: #ffffff !important; 
        color: #1f2937 !important; 
        border-radius: 16px !important; 
        padding: 12px 20px !important;
        box-shadow: none !important;
        border: none !important;
    }
    
    /* User Chat Bubble Alignment and Tone */
    [data-testid="stChatMessage"]:has(.user-msg-hook) { 
        display: flex !important; 
        flex-direction: row-reverse !important; 
    }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stMarkdownContainer"] {
        background-color: #f0f2f5 !important; 
        color: #1f2937 !important; 
        border-radius: 18px !important; 
        padding: 12px 20px !important;
        box-shadow: none !important;
        border: none !important;
    }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stChatAvatar"] { 
        display: none !important; 
    }

    /* 3. Continuous Micro-Animation for Avatar */
    .header-logo { 
        width: 65px; 
        animation: floatPulse 3s infinite ease-in-out; 
    }
    @keyframes floatPulse { 
        0%, 100% { transform: translateY(0px) scale(1); filter: drop-shadow(0 2px 4px rgba(2,118,189,0.1)); } 
        50% { transform: translateY(-6px) scale(1.03); filter: drop-shadow(0 8px 12px rgba(2,118,189,0.25)); } 
    }

    /* 4. Edgeless Floating Capsule Input Box (Gemini Theme) */
    div[data-testid="stChatInput"] {
        border: none !important;
        box-shadow: none !important;
        border-radius: 30px !important;
        background-color: #EAF2FC !important;
        padding: 6px 16px !important;
        bottom: 20px !important;
    }
    div[data-testid="stChatInput"] textarea {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
        color: #1f2937 !important;
    }
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
        border: none !important;
    }

    /* 5. Three-Dots Bouncing Typing Indicator Animation */
    .typing-container {
        display: flex;
        align-items: center;
        gap: 5px;
        font-style: italic;
        color: #6b7280;
        font-family: sans-serif;
        padding: 10px 0;
    }
    .bounce-dot {
        width: 6px;
        height: 6px;
        background-color: #38bdf8;
        border-radius: 50%;
        display: inline-block;
        animation: dotBounce 1.4s infinite ease-in-out both;
    }
    .bounce-dot:nth-child(1) { animation-delay: -0.32s; }
    .bounce-dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes dotBounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1.0) translateY(-6px); }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 5. SESSION STATE
# ==========================================
if "messages" not in st.session_state: 
    st.session_state.messages = []

# ==========================================
# 6. SEAMLESS SIDEBAR (Fixed using Native Streamlit elements)
# ==========================================
with st.sidebar:
    st.subheader("💬 Navigation")
    if st.button("🗑️ Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("Sarathi App v2.5\n\nPradhan Public School")

# ==========================================
# 7. BRANDING PLACEMENT & HEADER
# ==========================================
st.markdown(
    f"""
    <div style='text-align: center; margin-top: 20px;'>
        <img src='{BLUE_SMILE_AVATAR}' class='header-logo'>
        <h1 style='margin-bottom: 0px; font-weight: 700; color: #1f2937;'>Sarathi AI</h1>
        <p style='margin-top: 4px; color: #4b5563; font-size: 15px; font-weight: 500;'>Pradhan Public School's Digital Assistant</p>
    </div>
    <br>
    """, 
    unsafe_allow_html=True
)

# ==========================================
# 8. API CONNECTION (Strictly from Secrets)
# ==========================================
api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not api_key: 
    st.error("Error: Streamlit Secrets mein 'GOOGLE_API_KEY' missing hai!")
    st.stop()
client = genai.Client(api_key=api_key)

# ==========================================
# 9. DISPLAY CHAT HISTORY
# ==========================================
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant", avatar=None if msg["role"] == "user" else BLUE_SMILE_AVATAR):
        if msg["role"] == "user":
            content = f"<span class='user-msg-hook'></span>{msg['text']}"
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.markdown(f"✨ {msg['text']}", unsafe_allow_html=True)

# ==========================================
# 10. CHAT INPUT & ANIMATED RESPONSE LOGIC
# ==========================================
if user_input := st.chat_input("Ask me anything about the school..."):
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(f"<span class='user-msg-hook'></span>{user_input}", unsafe_allow_html=True)

    api_contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model", 
            parts=[types.Part.from_text(text=m["text"])]
        ) for m in st.session_state.messages
    ]

    with st.chat_message("assistant", avatar=BLUE_SMILE_AVATAR):
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            """
            <div class='typing-container'>
                Sarathi is responding...
                <div class='bounce-dot'></div>
                <div class='bounce-dot'></div>
                <div class='bounce-dot'></div>
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
                    temperature=0.4
                )
            )
            
            typing_placeholder.empty()
            st.write("✨ ")
            full_response = st.write_stream((chunk.text for chunk in response_stream if chunk.text))
            st.session_state.messages.append({"role": "assistant", "text": full_response})
            
        except Exception as e:
            typing_placeholder.empty()
            st.error(f"Error: {e}")
            
