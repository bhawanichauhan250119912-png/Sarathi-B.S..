import streamlit as st
from google import genai
from google.genai import types
import time
import os

# 1. Page Configuration (Home screen icon)
st.set_page_config(page_title="sarathi-B.S.", page_icon="logo.png", layout="centered")

# Logo Setup (Naya background-removed logo)
LOGO_FILE = "logo.png"
school_logo = "🤖" 
if os.path.exists(LOGO_FILE):
    school_logo = LOGO_FILE

# 2. CSS - 3D Logo Animation & Centering
st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    [data-testid="stImage"] img {
        animation: pulse 3s infinite;
        filter: drop-shadow(0px 8px 15px rgba(0, 0, 0, 0.4)); /* 3D Shadow Effect */
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SPLASH SCREEN (Starting Welcome Animation)
if "app_loaded" not in st.session_state:
    st.session_state.app_loaded = False

if not st.session_state.app_loaded:
    splash = st.empty()
    with splash.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, width=150) # Bada Logo Splash Screen par
        
        st.markdown("<h1 style='text-align: center;'>🤖 sarathi-B.S.</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: gray;'>*Your Intelligent School Companion & AI Guide* ✨</h4>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #FF4B4B;'>**स्वागत है प्रधान पब्लिक स्कूल में! 👋**</h3>", unsafe_allow_html=True)
    
    # 3.5 seconds tak welcome screen dikhegi, fir automatic chat khulega
    time.sleep(3.5)
    splash.empty() 
    st.session_state.app_loaded = True
    st.rerun()

# 4. MAIN CHAT INTERFACE (Splash Screen hatne ke baad yahan aayega)
if os.path.exists(LOGO_FILE):
    st.image(LOGO_FILE, width=90) # Chota logo chat interface par

st.markdown("<h2 style='text-align: center;'>🤖 sarathi-B.S.</h2>", unsafe_allow_html=True)
st.markdown("---")

# API Key Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key:
    st.info("💡 **Setup:** API Key enter karein.")
    st.stop()

client = genai.Client(api_key=api_key)

# 5. MASTER DATA (Saari school ki details safe hain)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' के आधिकारिक AI गाइड 'sarathi-B.S.' हो।
भाषा: Hinglish (आदरपूर्ण 'जी', 'सर', 'मैम' का प्रयोग)। 
फॉर्मेट: बुलेट पॉइंट्स और हेडिंग्स का उपयोग करें, मुख्य शब्दों को **BOLD** करें।

🏛️ मैनेजमेंट:
- प्रिंसिपल: **मोनिका छोंकर मैम**
- डायरेक्टर: **मानवेंद्र छोंकर सर**
- एग्जामिनर: **जगत प्रताप चौहान सर**
- फीस: **संतोष यादव सर** (सहायक: **चंचल मैम**)

📍 स्थान: प्रधान पब्लिक सीनियर सेकेंडरी स्कूल, सीगना, आगरा। कैंपस: विशाल असेंबली ग्राउंड, लॉन, बड़ा प्लेग्राउंड।
🏆 रिजल्ट: 10वीं: **देव छोंकर (98%)**, 12वीं: **प्रिया चौहान (96%)**।

👨‍🏫 कक्षा 11 फैकल्टी:
- कविता यादव मैम: History/Geography।
- विजय राठौर सर: Political Science, Fine Arts, इंग्लिश।
- विपिन अग्रवाल सर: Maths।

🧪 सुविधाएं: Smart Classes, Biology Lab (Real Samples), Chemistry Lab।
⏰ समय: Summer (7AM-1PM), Winter (8AM-2PM)।
"""

# 6. Session State & Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    custom_avatar = "👤" if msg["role"] == "user" else school_logo
    with st.chat_message(msg["role"], avatar=custom_avatar):
        st.write(msg["text"])

# 7. Chat Input Field
if user_input := st.chat_input("स्कूल या टीचर्स के बारे में पूछें..."):
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    chat_history = []
    for msg in st.session_state.messages[:-1]:
        chat_history.append(types.Content(role="user" if msg["role"] == "user" else "model", parts=[types.Part.from_text(text=msg["text"])]))

    with st.chat_message("assistant", avatar=school_logo):
        with st.spinner("सारथी जवाब ढूँढ रहा है... ✨"):
            try:
                chat = client.chats.create(model="gemini-2.5-flash", history=chat_history, config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA))
                response = chat.send_message(user_input)
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "text": response.text})
            except Exception as e:
                st.error("सर्वर में एरर है। थोड़ी देर बाद कोशिश करें।")
                
