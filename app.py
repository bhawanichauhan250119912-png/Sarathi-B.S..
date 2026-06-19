import streamlit as st
from google import genai
from google.genai import types
import time

# 1. पेज का नाम और आइकॉन सेट करना
st.set_page_config(page_title="sarathi-B.S.", page_icon="🏫", layout="centered")

# 2. हेडिंग्स
st.title("🤖 sarathi-B.S.")
st.markdown("#### **स्वागत है प्रधान पब्लिक स्कूल में! ✨**")
st.markdown("---")

# 3. API Key सेटअप
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    else:
        api_key = st.sidebar.text_input("जेमिनी API की दर्ज करें:", type="password")
    
    if api_key:
        client = genai.Client(api_key=api_key)
    else:
        st.warning("कृपया ऐप का उपयोग करने के लिए API Key प्रदान करें।")
        st.stop()
except Exception as e:
    st.error("कृपया Streamlit Secrets में 'GOOGLE_API_KEY' सेट करें।")
    st.stop()

# 4. मास्टर डेटा - यहाँ सारी जानकारी सुरक्षित है!
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' के आधिकारिक AI गाइड हो। तुम्हारा नाम 'सारथी-B.S.' है।
तुम्हारी भाषा अत्यंत विनम्र, संस्कारी और प्रोफेशनल (Hinglish/Hindi) होनी चाहिए। 

### 🎯 जवाब देने का अनिवार्य फॉर्मेट:
- हमेशा आदर के साथ (नमस्ते/प्रणाम) शुरू करें।
- कभी भी पूरा जवाब पैराग्राफ में न लिखें।
- ### हेडिंग, *बुलेट पॉइंट्स* और **बोल्ड शब्दों** का उपयोग करें।
- जानकारी स्पष्ट, सटीक और आदरसूचक होनी चाहिए।

### 🏛️ स्कूल मैनेजमेंट:
- प्रिंसिपल मैम: **श्रीमती मोनिका छोंकर मैम** (अनुशासित और प्रभावशाली अंग्रेजी बोलने वालीं)।
- डायरेक्टर सर: **मानवेंद्र छोंकर सर** (विनम्र और शांत स्वभाव)।
- एग्जामिनर सर: जगत प्रताप चौहान सर।
- फीस काउंटर: संतोष यादव सर (सहायक: चंचल मैम)।

### 📚 स्कूल की जानकारियां:
- पता: प्रधान पब्लिक सीनियर सेकेंडरी स्कूल, सीगना, आगरा (रायपुरा जाट के आगे)।
- कैंपस: विशाल असेंबली ग्राउंड, हरा-भरा लॉन, पीछे बड़ा प्लेग्राउंड।
- अनुशासन: अत्यंत कड़ा अनुशासन, आगरा की खेल प्रतियोगिताओं में सदैव प्रथम।

### 👨‍🏫 क्लास 11 के शिक्षक:
- **कविता यादव मैम:** इतिहास और भूगोल विशेषज्ञ।
- **विजय राठौर सर:** राजनीति विज्ञान, Fine Arts और इंग्लिश ग्रामर विशेषज्ञ।
- **विपिन अग्रवाल सर:** गणित (Maths) के बेहतरीन शिक्षक।

### 🧪 सुविधाएं:
- स्मार्ट क्लास की सुविधा, हवादार क्लासरूम।
- **बायोलॉजी लैब:** असली सैंपल्स (फिश, ऑक्टोपस, एल्गी) केमिकल्स में सुरक्षित।
- **केमिस्ट्री लैब:** सुरक्षा मानकों के साथ सभी केमिकल्स उपलब्ध।

### ⏰ समय:
- **गर्मियाँ:** सुबह 7:00 से दोपहर 1:00 बजे तक।
- **सर्दियाँ:** सुबह 8:00 से दोपहर 2:00 बजे तक।

### 🏆 रिजल्ट:
- **10वीं:** देव छोंकर (98%)।
- **12वीं:** प्रिया चौहान (96%)।

उपरोक्त जानकारी के आधार पर ही उत्तर दें। हमेशा Emojis का सुंदर उपयोग करें।
"""

# 5. मेमोरी और चैट सेटअप
if "request_times" not in st.session_state:
    st.session_state.request_times = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट हिस्ट्री दिखाना (लोगो के साथ)
for msg in st.session_state.messages:
    custom_avatar = "👤" if msg["role"] == "user" else "74424.png"
    with st.chat_message(msg["role"], avatar=custom_avatar):
        st.write(msg["text"])

# चैट इनपुट
user_input = st.chat_input("स्कूल या टीचर्स के बारे में सारथी से पूछें...")

if user_input:
    # टाइमर और लिमिट चेक
    current_time = time.time()
    st.session_state.request_times = [t for t in st.session_state.request_times if current_time - t < 60]
    
    if len(st.session_state.request_times) >= 10:
        st.warning("⚠️ **चेतावनी:** आप बहुत तेज़ी से सवाल पूछ रहे हैं! कृपया 15 सेकंड का गैप दें।")

    st.session_state.request_times.append(current_time)
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    try:
        chat_history = []
        for msg in st.session_state.messages[:-1]:
            role_name = "user" if msg["role"] == "user" else "model"
            chat_history.append(
                types.Content(role=role_name, parts=[types.Part.from_text(text=msg["text"])])
            )

        # जेमिनी 2.5 मॉडल
        chat = client.chats.create(
            model="gemini-2.5-flash",
            history=chat_history,
            config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA)
        )
        
        response = chat.send_message(user_input)
        
        st.session_state.messages.append({"role": "assistant", "text": response.text})
        with st.chat_message("assistant", avatar="74424.png"):
            st.write(response.text)
            
    except Exception as e:
        err_message = str(e).upper()
        if "503" in err_message or "UNAVAILABLE" in err_message:
            st.info("🏫 **सारथी संदेश:** सर्वर पर ट्रैफिक है। कृपया 10 सेकंड रुक कर पुनः प्रयास करें! 😊")
        elif "429" in err_message or "RESOURCE_EXHAUSTED" in err_message:
            st.warning("⏳ **सारथी संदेश:** कोटा पूर्ण हो गया है। कृपया कुछ समय पश्चात प्रयास करें। 🙏")
        else:
            st.error("⚠️ **तकनीकी संदेश:** नेटवर्क में रुकावट है। थोड़ी देर बाद कोशिश करें।")
            
