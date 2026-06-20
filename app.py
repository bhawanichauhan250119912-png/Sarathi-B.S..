import streamlit as st
from google import genai
from google.genai import types
import time
import os

# 1. Page Configuration (Home screen icon setup)
st.set_page_config(page_title="sarathi-B.S.", page_icon="logo.png", layout="centered")

# Logo Setup
LOGO_FILE = "logo.png"
school_logo = "🤖" 
if os.path.exists(LOGO_FILE):
    school_logo = LOGO_FILE

# 2. Advanced CSS - Logo 3D Shadow & Breathing Pulse Animation
st.markdown("""
    <style>
    @keyframes breathing {
        0% { transform: scale(1); filter: drop-shadow(0px 5px 10px rgba(255,255,255,0.2)); }
        50% { transform: scale(1.08); filter: drop-shadow(0px 15px 25px rgba(255,255,255,0.4)); }
        100% { transform: scale(1); filter: drop-shadow(0px 5px 10px rgba(255,255,255,0.2)); }
    }
    [data-testid="stImage"] img {
        animation: breathing 3.5s ease-in-out infinite;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SPLASH SCREEN (Starting Intro)
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    splash_holder = st.empty()
    with splash_holder.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, width=160)
        else:
            st.markdown("<h1 style='text-align: center;'>🏫</h1>", unsafe_allow_html=True)
            
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>🤖 sarathi-B.S.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888888; font-style: italic;'>Your Intelligent School Companion & AI Guide ✨</p>", unsafe_allow_html=True)
        st.markdown("<br><h3 style='text-align: center; color: #FF4B4B; font-weight: bold;'>स्वागत है प्रधान पब्लिक स्कूल में! 👋</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #555555;'>सारथी लोड हो रहा है...</p>", unsafe_allow_html=True)
    
    time.sleep(4.5)
    st.session_state.splash_done = True
    st.rerun()

# 4. MAIN CHAT INTERFACE
main_header = st.container()
with main_header:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=85)
    st.markdown("<h2 style='text-align: center;'>🤖 sarathi-B.S.</h2>", unsafe_allow_html=True)
    st.markdown("---")

# API Key Secure Fetch
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key:
    st.info("💡 **Setup Instruction:** Streamlit Secrets में GOOGLE_API_KEY सेट करें।")
    st.stop()

client = genai.Client(api_key=api_key)

# 5. MULTI-LINGUAL SCHOOL KNOWLEDGE BASE
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' (Pradhan Public Senior Secondary School) के आधिकारिक AI गाइड 'sarathi-B.S.' हो।

🗣️ **Language Rules (सबसे महत्वपूर्ण नियम):**
1. **Dynamic Language Matching:** तुम्हें हमेशा यूज़र की भाषा में ही जवाब देना है। 
   - If the user asks in **English**, you MUST reply in perfect, professional **English**.
   - अगर यूज़र **हिंदी** या **Hinglish** में पूछे, तो तुम्हें भी प्राकृतिक और सम्मानजनक **Hinglish/Hindi** में जवाब देना है।
2. **Tone:** हमेशा आदरपूर्ण रहें। अध्यापकों के लिए 'Sir' / 'Ma'am' या 'सर' / 'मैम' का प्रयोग करें।
3. **Formatting:** उत्तर हमेशा सुंदर बुलेट पॉइंट्स (-) और हेडिंग्स (###) में दें। मुख्य नामों और समय को **BOLD** करें। Emojis का उपयोग करें।

🏛️ स्कूल मैनेजमेंट (School Management):
- प्रिंसिपल (Principal): **श्रीमती मोनिका छोंकर मैम** (Mrs. Monika Chhonkar) - Highly disciplined and fluent in English.
- डायरेक्टर (Director): **मानवेंद्र छोंकर सर** (Mr. Manvendra Chhonkar) - Very polite, calm, and supportive.
- एग्जामिनर (Examiner): **जगत प्रताप चौहान सर** (Mr. Jagat Pratap Chauhan).
- फीस काउंटर (Fee Counter): **संतोष यादव सर** (Mr. Santosh Yadav) | सहायक (Assistant): **चंचल मैम** (Ms. Chanchal).

📍 स्थान और कैंपस (Location & Campus):
- पता: सीगना, आगरा (Singna, Agra).
- कैंपस में विशाल असेंबली ग्राउंड, हरा-भरा लॉन और एक बहुत बड़ा प्लेग्राउंड (Playground) है। यह स्कूल अपने कड़े अनुशासन और खेल प्रतियोगिताओं में प्रथम आने के लिए जाना जाता है।

🏆 टॉपर्स (Board Exam Toppers):
- कक्षा 10वीं: **देव छोंकर (98%)**
- कक्षा 12वीं: **प्रिया चौहान (96%)**

👨‍🏫 कक्षा 11 फैकल्टी (Class 11 Faculty):
- **कविता यादव मैम**: इतिहास (History) और भूगोल (Geography).
- **विजय राठौर सर**: राजनीति विज्ञान (Political Science), फाइन आर्ट्स (Fine Arts) और English Grammar.
- **विपिन अग्रवाल सर**: गणित (Mathematics) - Very popular and magical teacher.

🧪 सुविधाएं (Labs & Facilities):
- सभी कक्षाएं **Smart Classes** की सुविधा से लैस हैं।
- **Biology Lab**: यहाँ असली सैंपल्स (Real samples like fish, octopus) मौजूद हैं।
- **Chemistry Lab**: पूर्ण सुरक्षा मानकों के साथ सभी केमिकल्स उपलब्ध हैं।

⏰ स्कूल का समय (School Timings):
- गर्मियों में (Summer): सुबह 7:00 AM से दोपहर 1:00 PM
- सर्दियों में (Winter): सुबह 8:00 AM से दोपहर 2:00 PM
"""

# 6. Chat History Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    custom_avatar = "👤" if msg["role"] == "user" else school_logo
    with st.chat_message(msg["role"], avatar=custom_avatar):
        st.write(msg["text"])

# 7. User Input and AI Response Action
if user_input := st.chat_input("Ask me anything (English, Hindi, or Hinglish)..."):
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    chat_history = []
    for msg in st.session_state.messages[:-1]:
        chat_history.append(types.Content(role="user" if msg["role"] == "user" else "model", parts=[types.Part.from_text(text=msg["text"])]))

    with st.chat_message("assistant", avatar=school_logo):
        with st.spinner("सारथी जवाब तैयार कर रहा है... ✨"):
            try:
                chat = client.chats.create(
                    model="gemini-2.5-flash",
                    history=chat_history,
                    config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA)
                )
                response = chat.send_message(user_input)
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "text": response.text})
            except Exception as e:
                st.error("दैनिक निशुल्क सीमा या नेटवर्क त्रुटि। कृपया बाद में प्रयास करें।")
    
