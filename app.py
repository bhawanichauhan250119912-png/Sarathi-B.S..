import streamlit as st
from google import genai
from google.genai import types
import time

# 1. पेज का नाम और आइकॉन सेट करना (ब्राउज़र टैब के लिए)
st.set_page_config(page_title="sarathi-B.S.", page_icon="🤖", layout="centered")

# 2. मुख्य हेडिंग्स - एकदम प्रोफेशनल टेक लुक (जैसा आपने मांगा था)
st.title("🤖 sarathi-B.S.")
st.markdown("#### **स्वागत है प्रधान पब्लिक स्कूल में! ✨**")
st.markdown("---")

# 3. API Key सेट करना और क्लाइंट बनाना
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
    st.error("कृपया Streamlit Secrets in 'GOOGLE_API_KEY' सेट करें।")
    st.stop()

# 4. स्कूल का मास्टर डेटा (सिस्टम इंस्ट्रक्शन)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर转换 सेकेंडरी स्कूल' के एक अत्यंत प्रतिष्ठित, संस्कारी और उच्च शिक्षित एआई गाइड (AI Assistant) हो। तुम्हारा नाम 'सारथी' है।
तुम्हारा मुख्य उद्देश्य स्कूल के मैनेजमेंट, पेरेंट्स और छात्रों को बेहद सटीक, स्पष्ट और सम्मानजनक जानकारी देना है।

⚠️ जवाब देने की प्रोफेशनल शैली (Formatting Rules) - इसे कड़ाई से लागू करें:
1. कभी भी पूरा जवाब एक लंबे पैराग्राफ में न लिखें। बात को हमेशा सुंदर बुलेट पॉइंट्स (*) और छोटी हेडिंग्स (###) में बांटकर लिखें ताकि पढ़ने में आसानी हो।
2. मुख्य शब्दों, तारीखों, नामों और अंकों को हमेशा **बोल्ड** (Double Asterisks) करें।
3. भाषा बिल्कुल शुद्ध, शिष्ट और आदरसूचक हिंग्लिश (या हिंदी) होनी चाहिए। हमेशा 'जी', 'आप', 'मैम' और 'सर' का प्रयोग करें।
4. बातचीत की शुरुआत और अंत में गरिमापूर्ण Emojis (😊, ✨, 🏫) का सीमित और सुंदर उपयोग करें।

🏛️ स्कूल मैनेजमेंट का विवरण:
- प्रिंसिपल मैम: श्रीमती मोनिका छोंकर मैम (Mrs. Monika Chhonkar)। अत्यंत अनुशासित, कुशल मार्गदर्शक और बेहद प्रभावशाली अंग्रेजी (Fluent English) बोलने वालीं।
- डायरेक्टर सर: मानवेंद्र छोंकर सर (Manvendra Chhonkar)। अत्यंत शांत, सरल और अत्यंत विनम्र (Polite) स्वभाव के धनी।
- एग्जामिनर सर: जगत प्रताप चौहान सर।
- फीस काउंटर: संतोष यादव सर (सहायक: चंचल मैम)।

📚 स्कूल की मुख्य जानकारियां:
- स्थान: प्रधान पब्लिक सीनियर सेकेंडरी स्कूल, सीगना, आगरा (रायपुरा जाट के आगे)।
- कैंपस: सामने विशाल असेंबली ग्राउंड, बगल में हरा-भरा लॉन और पीछे खेलकूद के लिए एक बहुत बड़ा प्लेग्राउंड है।
- अनुशासन एवं खेल: स्कूल अपने कड़े अनुशासन के लिए जाना जाता है। आगरा की खेल प्रतियोगिताओं में हमारा स्कूल सदैव प्रथम स्थान प्राप्त करता है।

👨‍🏫 कक्षा 11 के शिक्षक:
- कविता यादव मैम: इतिहास (History) और भूगोल (Geography) की विशेषज्ञ।
- विजय繞 राठौर सर: राजनीति विज्ञान (Political Science), Fine Arts, संविधान के ज्ञाता और इंग्लिश ग्रामर के बेहतरीन शिक्षक।
- विपिन अग्रवाल सर: गणित (Maths) के अत्यंत लोकप्रिय और विशेषज्ञ शिक्षक।

🧪 प्रयोगशालाएं (Labs):
- सभी कक्षाएं हवादार हैं, जिनमें पंखे और आधुनिक स्मार्ट क्लास की सुविधा उपलब्ध है।
- बायोलॉजी लैब: यहाँ केमिकल्स में सुरक्षित रखे गए असली सैंपल्स (जैसे रियल फिश, ऑक्टोपस, एल्गी) मौजूद हैं।
- chemistry लैब: पूर्ण सुरक्षा मानकों के साथ सभी आवश्यक केमिकल्स उपलब्ध हैं।

⏰ विद्यालय का समय:
- ग्रीष्मकाल (गर्मियों में): सुबह 7:00 बजे से दोपहर 1:00 बजे तक।
- शीतकाल (सर्दियों में): सुबह 8:00 बजे से दोपहर 2:00 बजे तक।

🏆 उत्कृष्ट परीक्षा परिणाम:
- कक्षा 10वीं: देव छोंकर ने 98% अंक प्राप्त कर विद्यालय टॉप किया।
- कक्षा 12वीं: प्रिया चौहान ने 96% अंकों के साथ सर्वोच्च स्थान प्राप्त किया।
"""

# --- वॉर्निंग सिस्टम के लिए टाइमर मेमोरी ---
if "request_times" not in st.session_state:
    st.session_state.request_times = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट स्क्रीन पर दिखाना (कस्टम अवतारों के साथ ताकि लाल आइकॉन न आए)
for msg in st.session_state.messages:
    custom_avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=custom_avatar):
        st.write(msg["text"])

# चैट इनपुट बॉक्स
user_input = st.chat_input("स्कूल या टीचर्स के बारे में सारथी से पूछें...")

if user_input:
    # 1. टाइम चेक करना और पिछले 60 सेकंड के सवाल गिनना
    current_time = time.time()
    st.session_state.request_times = [t for t in st.session_state.request_times if current_time - t < 60]
    
    # एडवांस वॉर्निंग: 1 मिनट में 10 से ज़्यादा सवाल होने पर
    if len(st.session_state.request_times) >= 10:
        st.warning("⚠️ **चेतावनी:** आप बहुत तेज़ी से सवाल पूछ रहे हैं! सरवार की सुरक्षा के लिए कृपया अगले सवाल से पहले 15 सेकंड का गैप दें।")

    st.session_state.request_times.append(current_time)

    # यूजर का मैसेज स्क्रीन पर दिखाना (👤 अवतार के साथ)
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    try:
        # चैट हिस्ट्री तैयार करना
        chat_history = []
        for msg in st.session_state.messages[:-1]:
            role_name = "user" if msg["role"] == "user" else "model"
            chat_history.append(
                types.Content(role=role_name, parts=[types.Part.from_text(text=msg["text"])])
            )

        # जेमिनी मॉडल से कनेक्ट करना (New Gemini 2.5 Model)
        chat = client.chats.create(
            model="gemini-2.5-flash",
            history=chat_history,
            config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA)
        )
        
        response = chat.send_message(user_input)

        # बॉट का जवाब दिखाना (🤖 अवतार के साथ)
        st.session_state.messages.append({"role": "assistant", "text": response.text})
        with st.chat_message("assistant", avatar="🤖"):
            st.write(response.text)
            
    except Exception as e:
        err_message = str(e).upper()
        # प्रोफेशनल सुरक्षा कवच: कोई इंटरनल एरर यूजर को नहीं दिखेगा
        if "503" in err_message or "UNAVAILABLE" in err_message:
            st.info("🏫 **सारथी संदेश:** स्कूल गाइड सर्वर पर इस समय थोड़ा अधिक ट्रैफिक है। कृपया 5-10 सेकंड रुक कर अपना सवाल दोबारा पूछें! 😊✨")
        elif "429" in err_message or "RESOURCE_EXHAUSTED" in err_message:
            st.warning("⏳ **सारथी संदेश:** निशुल्क दैनिक कोटा पूर्ण हो गया है। कृपया कुछ समय पश्चात प्रयास करें या एडमिन से संपर्क करें। 🙏")
        else:
            st.error("⚠️ **तकनीकी संदेश:** नेटवर्क में कुछ अस्थायी रुकावट है। कृपया थोड़ी देर बाद पुनः प्रयास करें।")
            
