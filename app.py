import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration (Title Capitalized)
st.set_page_config(page_title="Sarathi-B.S.", page_icon="🤖", layout="centered")

# 2. PREMIUM CSS - Sky Blue Theme, Gemini Chat Bubbles & Animations
st.markdown("""
    <style>
    /* --- 1. Background Theme (Sky Blue Mix) --- */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%) !important;
    }
    /* Force Text to be Dark on Light Background */
    h1, h2, h3, h4, p, span {
        color: #0f172a !important;
    }

    /* --- 2. Code-Based Animated Logo --- */
    @keyframes floatAndGlow {
        0% { transform: translateY(0px) scale(1); filter: drop-shadow(0px 5px 15px rgba(59, 130, 246, 0.3)); }
        50% { transform: translateY(-12px) scale(1.08); filter: drop-shadow(0px 15px 25px rgba(59, 130, 246, 0.6)); }
        100% { transform: translateY(0px) scale(1); filter: drop-shadow(0px 5px 15px rgba(59, 130, 246, 0.3)); }
    }
    .ai-logo {
        font-size: 85px;
        text-align: center;
        animation: floatAndGlow 3.5s ease-in-out infinite;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    /* --- 3. Chat Input Box (No Red Border, Gemini Style) --- */
    [data-testid="stChatInput"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 30px !important;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05) !important;
        padding-right: 5px;
    }
    [data-testid="stChatInput"]:focus-within {
        border: 2px solid #3b82f6 !important; /* Blue outline on typing */
    }
    [data-testid="stChatInput"] textarea {
        color: #0f172a !important;
    }
    /* Send Button Arrow Style */
    [data-testid="stChatInputSubmitButton"] {
        background-color: #3b82f6 !important;
        border-radius: 50% !important;
        transition: 0.3s;
    }
    [data-testid="stChatInputSubmitButton"] svg {
        fill: white !important; /* White Arrow */
    }
    [data-testid="stChatInputSubmitButton"]:hover {
        background-color: #2563eb !important;
        transform: scale(1.1);
    }

    /* --- 4. Chat Bubbles Alignment (Right & Left) --- */
    /* Hide Default Human Avatar */
    [data-testid="chatAvatarIcon-user"] {
        display: none !important; 
    }
    
    /* USER Message - Right Side (Blue Bubble) */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        flex-direction: row-reverse; /* Pushes to Right */
        background-color: transparent !important;
    }
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] {
        background-color: #3b82f6 !important;
        padding: 12px 20px;
        border-radius: 20px 20px 0px 20px; /* Chat bubble tail */
        display: inline-block;
        box-shadow: 0px 4px 10px rgba(59, 130, 246, 0.2);
    }
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) p {
        color: #ffffff !important; /* White text for User */
        margin: 0;
    }

    /* ASSISTANT Message - Left Side (White Bubble) */
    [data-testid="stChatMessage"]:not(:has([data-testid="chatAvatarIcon-user"])) {
        background-color: transparent !important;
    }
    [data-testid="stChatMessage"]:not(:has([data-testid="chatAvatarIcon-user"])) [data-testid="stMarkdownContainer"] {
        background-color: #ffffff !important;
        padding: 15px 20px;
        border-radius: 20px 20px 20px 0px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.03);
    }

    /* --- 5. 3-Dots Typing Animation --- */
    .typing-box {
        display: inline-flex;
        align-items: center;
        background-color: #ffffff;
        padding: 10px 20px;
        border-radius: 20px 20px 20px 0px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.03);
        color: #3b82f6 !important;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 15px;
    }
    .dot {
        animation: blink 1.4s infinite ease-in-out both;
        font-size: 24px;
        line-height: 10px;
        margin-left: 3px;
    }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes blink {
        0%, 80%, 100% { opacity: 0; transform: scale(0.8); }
        40% { opacity: 1; transform: scale(1.2); }
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Custom Logo (Capitalized Name)
st.markdown("<div class='ai-logo'>🤖</div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-weight: 800;'>Sarathi-B.S.</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #64748b !important;'>Your Intelligent School Companion ✨</p>", unsafe_allow_html=True)
st.markdown("---")

# API Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key:
    st.info("💡 **Setup Instruction:** Streamlit Secrets में GOOGLE_API_KEY सेट करें।")
    st.stop()

client = genai.Client(api_key=api_key)

# 4. Strict Knowledge Base
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' के AI गाइड 'Sarathi-B.S.' हो। 
नियम:
1. हमेशा यूज़र की भाषा (English, Hindi, या Hinglish) में ही जवाब दो।
2. विस्तार से जवाब दो और बुलेट पॉइंट्स का इस्तेमाल करो।
3. हमेशा सम्मानजनक टोन रखो।

- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम 
- डायरेक्टर: मानवेंद्र छोंकर सर
- एग्जामिनर: जगत प्रताप चौहान सर
- फीस काउंटर: संतोष यादव सर
- 10वीं टॉपर: देव छोंकर (98%) | 12वीं टॉपर: प्रिया चौहान (96%)
- फैकल्टी: कविता यादव मैम (History/Geo), विजय राठौर सर (Pol. Science/English), विपिन अग्रवाल सर (Maths)
- लैब: Smart Classes, Biology Lab (Real samples), Chemistry Lab
- समय: Summer (7 AM - 1 PM), Winter (8 AM - 2 PM)
"""

# 5. Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    # 'user' role automatically triggers the right-side CSS we wrote
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# 6. Chat Input & AI Response
if user_input := st.chat_input("Ask me anything (English, Hindi, or Hinglish)..."):
    
    # 1. User Message (Right Side)
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Prepare history for AI
    chat_history = []
    for msg in st.session_state.messages[:-1]:
        chat_history.append(types.Content(role="user" if msg["role"] == "user" else "model", parts=[types.Part.from_text(text=msg["text"])]))

    # 2. Assistant Response with 3-Dots Animation
    with st.chat_message("assistant", avatar="🤖"):
        # Create empty box for animation
        loading_box = st.empty()
        
        # Inject custom 3-dots animation HTML
        loading_box.markdown("""
            <div class="typing-box">
                Sarathi is responding
                <span class="dot">.</span>
                <span class="dot">.</span>
                <span class="dot">.</span>
            </div>
        """, unsafe_allow_html=True)
        
        try:
            # Fetch response
            chat = client.chats.create(
                model="gemini-2.5-flash",
                history=chat_history,
                config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA, temperature=0.7)
            )
            response = chat.send_message(user_input)
            
            # Clear animation and show real text
            loading_box.empty()
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "text": response.text})
            
        except Exception as e:
            loading_box.empty()
            st.error("दैनिक निशुल्क सीमा या नेटवर्क त्रुटि। कृपया बाद में प्रयास करें।")
            
