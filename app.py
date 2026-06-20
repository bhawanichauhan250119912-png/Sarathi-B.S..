import streamlit as st
from google import genai
from google.genai import types
import time
import os

# 1. Page Configuration
st.set_page_config(page_title="sarathi-B.S.", page_icon="logo.png", layout="centered")

# Logo Setup
LOGO_FILE = "logo.png"
school_logo = "🤖" 
if os.path.exists(LOGO_FILE):
    school_logo = LOGO_FILE

# 2. Advanced CSS - Anti-Blur & High Quality 3D Animation
st.markdown("""
    <style>
    @keyframes breathing {
        0% { transform: scale(1); filter: drop-shadow(0px 4px 8px rgba(255,255,255,0.15)); }
        50% { transform: scale(1.05); filter: drop-shadow(0px 12px 20px rgba(255,255,255,0.3)); }
        100% { transform: scale(1); filter: drop-shadow(0px 4px 8px rgba(255,255,255,0.15)); }
    }
    [data-testid="stImage"] img {
        animation: breathing 3.5s ease-in-out infinite;
        display: block;
        margin-left: auto;
        margin-right: auto;
        /* Anti-Blur CSS Rules */
        image-rendering: -webkit-optimize-contrast;
        image-rendering: high-quality;
        object-fit: contain;
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
            # Size slightly reduced to prevent pixel stretching
            st.image(LOGO_FILE, width=130) 
        else:
            st.markdown("<h1 style='text-align: center;'>🏫</h1>", unsafe_allow_html=True)
            
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>🤖 sarathi-B.S.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888888; font-style: italic;'>Your Intelligent School Companion & AI Guide ✨</p>", unsafe_allow_html=True)
        st.markdown("<br><h3 style='text-align: center; color: #FF4B4B; font-weight: bold;'>स्वागत है प्रधान पब्लिक स्कूल में! 👋</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #555555;'>सारथी सिस्टम लोड हो रहा है...</p>", unsafe_allow_html=True)
    
    time.sleep(4.0)
    st.session_state.splash_done = True
    st.rerun()

# 4. MAIN CHAT INTERFACE
main_header = st.container()
with main_header:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=75) # Crisp size for chat header
    st.markdown("<h2 style='text-align: center;'>🤖 sarathi-B.S.</h2>", unsafe_allow_html=True)
    st.markdown("---")

# API Key Secure Fetch
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key:
    st.info("💡 **Setup Instruction:** Streamlit Secrets में GOOGLE_API_KEY सेट करें।")
    st.stop()

client = genai.Client(api_key=api_key)

# 5. NEW STRICT MASTER DATA (Language Mirroring & Detailed Explanations)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' (Pradhan Public Senior Secondary School) के अत्यंत बुद्धिमान और आधिकारिक AI गाइड 'sarathi-B.S.' हो। 

🚨 **तुम्हारे 3 सबसे कड़े नियम (STRICT DIRECTIVES):**
1. **100% Language Mirroring:** तुम्हें यूज़र की भाषा को तुरंत पकड़ना है। बिना यूज़र के कहे:
   - If the user types in **English**, your ENTIRE response MUST be in fluent, professional, and grammatically perfect **English**.
   - अगर यूज़र **हिंदी या Hinglish** में बात करे, तो तुम्हारा जवाब भी पूरी तरह प्राकृतिक **हिंदी/Hinglish** में होना चाहिए।
2. **Deep & Detailed Explanations:** कभी भी 1-2 लाइन का छोटा जवाब मत देना। यूज़र जो भी पूछे, उसे बहुत ही विस्तार (Detail) से, अच्छे से समझाकर (Elaborate) जवाब दो। उसे ऐसा लगना चाहिए कि कोई बहुत ज्ञानी इंसान उसे समझा रहा है।
3. **Tone & Formatting:** हमेशा सम्मानजनक (Sir/Ma'am/सर/मैम) रहो। जवाबों को सुंदर पैराग्राफ्स और स्पष्ट बुलेट पॉइंट्स में बांटो।

🏛️ **स्कूल मैनेजमेंट (School Management Data):**
- प्रिंसिपल (Principal): श्रीमती मोनिका छोंकर मैम (Mrs. Monika Chhonkar) - Highly disciplined, excellent leadership, and fluent in English.
- डायरेक्टर (Director): मानवेंद्र छोंकर सर (Mr. Manvendra Chhonkar) - Very polite, calm, and highly supportive of students.
- एग्जामिनर (Examiner): जगत प्रताप चौहान सर (Mr. Jagat Pratap Chauhan).
- फीस काउंटर (Fee Counter): संतोष यादव सर (Mr. Santosh Yadav) और उनकी सहायक चंचल मैम (Ms. Chanchal).

📍 **स्थान और कैंपस (Location & Infrastructure):**
- पता: सीगना, आगरा (Singna, Agra).
- कैंपस: इसमें एक विशाल असेंबली ग्राउंड, सुंदर हरा-भरा लॉन और खेलकूद (Sports) के लिए एक बहुत बड़ा प्लेग्राउंड है। स्कूल कड़े अनुशासन और खेल में आगरा में अव्वल रहने के लिए प्रसिद्ध है।

🏆 **बोर्ड परीक्षा टॉपर्स (Board Exam Toppers):**
- कक्षा 10वीं टॉपर: देव छोंकर (Dev Chhonkar) - 98%
- कक्षा 12वीं टॉपर: प्रिया चौहान (Priya Chauhan) - 96%

👨‍🏫 **कक्षा 11 फैकल्टी (Class 11 Faculty):**
- कविता यादव मैम (Kavita Yadav Ma'am): इतिहास (History) और भूगोल (Geography) की विशेषज्ञ।
- विजय राठौर सर (Vijay Rathore Sir): राजनीति विज्ञान (Political Science), फाइन आर्ट्स (Fine Arts) और English Grammar के बेहतरीन शिक्षक।
- विपिन अग्रवाल सर (Vipin Agarwal Sir): गणित (Mathematics) के अत्यंत लोकप्रिय और जादुई शिक्षक।

🧪 **सुविधाएं (Facilities):**
- Smart Classes: सभी कक्षाएं आधुनिक तकनीक से लैस हैं।
- Biology Lab: असली सैंपल्स (Real samples like fish, octopus, algae) उपलब्ध हैं जो इसे खास बनाते हैं।
- Chemistry Lab: प्रयोगों के लिए उच्च स्तरीय और सुरक्षित केमिकल्स उपलब्ध हैं।

⏰ **स्कूल का समय (Timings):**
- गर्मियों में (Summer): सुबह 7:00 AM से दोपहर 1:00 PM.
- सर्दियों में (Winter): सुबह 8:00 AM से दोपहर 2:00 PM.
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
                    config=types.GenerateContentConfig(
                        system_instruction=SCHOOL_DATA,
                        temperature=0.7 # Helps AI give more creative and detailed answers
                    )
                )
                response = chat.send_message(user_input)
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "text": response.text})
            except Exception as e:
                st.error("दैनिक निशुल्क सीमा या नेटवर्क त्रुटि। कृपया बाद में प्रयास करें।")
                         
