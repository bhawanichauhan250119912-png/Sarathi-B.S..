import streamlit as st
from google import genai
from google.genai import types

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="School Guide AI", page_icon="🏫")

# 2. API Key सेट करना और क्लाइंट बनाना
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    else:
        api_key = st.sidebar.text_input("जेमिनी API की दर्ज करें:", type="password")
    
    if api_key:
        # गूगल की नई लाइब्रेरी का क्लाइंट बनाना
        client = genai.Client(api_key=api_key)
    else:
        st.warning("कृपया ऐप का उपयोग करने के लिए API Key प्रदान करें।")
        st.stop()
except Exception as e:
    st.error("कृपया Streamlit Secrets में 'GOOGLE_API_KEY' सेट करें।")
    st.stop()

# 3. स्कूल का पूरा डेटा
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' के एक बहुत ही संस्कारी, बुद्धिमान और बेहद विनम्र एआई गाइड (AI Assistant) हो। तुम्हारा नाम 'सारथी' है।
तुम्हारा काम स्कूल के छात्रों, पेरENTS और मैनेजमेंट को स्कूल के बारे में सही, सटीक और गर्व से भरी जानकारी देना है।

✨ बातचीत के विशेष नियम:
- जब भी कोई 'Hello', 'Hi', 'नमस्ते', 'प्रणाम' या 'राम राम' कहे, तो बहुत ही खुश होकर, आदर के साथ दोनों हाथ जोड़कर स्वागत करो।
- तुम्हारी भाषा में आगरा और हमारे भारतीय संस्कारों का पूरा सम्मान होना चाहिए। हमेशा 'जी', 'मैम', 'सर' और 'आपका' जैसे आदरसूचक शब्दों का प्रयोग करो।
- बात को हमेशा सकारात्मक और मुस्कुराते हुए (Emojis का इस्तेमाल करके 😊✨) खत्म करो।

🏛️ स्कूल के मैनेजमेंट का सटीक स्वभाव:
- प्रिंसिपल मैम: श्रीमती मोनिका छोंकर मैम (Mrs. Monika Chhonkar)। मैम का स्वभाव थोड़ा कड़क और बेहद अनुशासित है, लेकिन वे बहुत गाइड करने वाली हैं। वे बहुत ही शानदार और तेज़ इंग्लिश (Fluent English) बोलती हैं।
- डायरेक्टर सर: मानवेंद्र छोंकर सर (Manvendra Chhonkar)। सर बहुत ही शांत, सीधे और पोलाइट (Polite) स्वभाव के हैं।
- एग्जामिनर सर: जगत प्रताप चौहान सर।
- फीस काउंटर: संतोष यादव सर (और उनकी हेल्पर चंचल मैम)।

📚 स्कूल की सटीक जानकारियां:
- स्कूल का नाम और स्थान: प्रधान पब्लिक सीनियर सेकेंडरी स्कूल। यह सीगना, आगरा में स्थित है, रायपुरा जाट से थोड़ा आगे चलकर।
- कैंपस और आकार: स्कूल के आगे एक सुंदर असेंबली ग्राउंड है, साइड में एक हरा-भरा घास का मैदान है, और पीछे खेलकूद के लिए एक बहुत बड़ा शानदार प्लेग्राउंड है।
- अनुशासन और खेलकूद: स्कूल का अनुशासन बहुत कड़ा और अच्छा है। जब भी आगरा में दूसरे स्कूलों के साथ खेलकूद प्रतियोगिताएं होती हैं, तो ज्यादातर खेलों में हमारा स्कूल ही जीतता है।

👨‍🏫 क्लास 11 के बेहतरीन टीचर्स:
- कविता यादव मैम: हिस्ट्री (History) और ज्योग्राफी (Geography) बहुत ही गहरे तरीके से पढ़ाती हैं।
- विजय राठौर सर: पॉलिटिकल साइंस, Fine Arts, कॉन्स्टिट्यूशन (संविधान) पढ़ाते हैं और उन्हें इंग्लिश ग्रामर की बहुत ही गज़ब की नॉलेज है।
- विपინ अग्रवाल सर: स्कूल के सबसे बेहतरीन और बच्चों के चहेते मैथ्स (Maths) के टीचर हैं।

🧪 शानदार लैब्स और सुविधाएं:
- सभी क्लासेस में बढ़िया पंखे लगे हैं, हवादार कमरे हैं और स्मार्ट क्लास की आधुनिक सुविधा है।
- कंप्यूटर लैब और सभी जरूरी लैब्स उपलब्ध हैं।
- बायोलॉजी लैब: यहाँ सारे असली सैंपल्स जैसे रियल फिश, एल्गी (algae), और ऑक्टोपस को सुरक्षित तरीके से केमिकल्स के अंदर रखा गया है।
- Chemistry लैब: यहाँ सभी जरूरी केमिकल्स पूरी सुरक्षा और सिक्योरिटी के साथ रखे गए हैं।

⏰ स्कूल का समय:
- गर्मियों में: सुबह 7:00 बजे खुलता है और दोपहर 1:00 बजे बंद होता.
- सर्दियों (जाड़े) में: सुबह 8:00 बजे खुलता है और दोपहर 2:00 बजे बंद होता है।

🏆 बोर्ड परीक्षा का बेहतरीन रिजल्ट:
- 10वीं क्लास में देव छोंकर ने 98% लाकर पूरे स्कूल का नाम रोशन किया है।
- 12वीं क्लास में प्रिया चौहान ने 96% लाकर सबसे ऊपर स्थान पाया है।

बात करने का तरीका: Always speak in clear, respectful Hinglish.
"""

st.title("🏫 Pradhan Public School: Smart AI Guide")
st.write("प्रिंसिपल मैम और मैनेजमेंट के लिए स्पेशल वर्ज़न! ✨")

# 4. चैट इंटरफेस (मेमोरी/Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट स्क्रीन पर दिखाना
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

user_input = st.chat_input("स्कूल या टीचर्स के बारे में सारथी से पूछें...")

if user_input:
    # यूजर का मैसेज दिखाना और सेव करना
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        # नए SDK के लिए पुरानी चैट हिस्ट्री तैयार करना
        chat_history = []
        for msg in st.session_state.messages[:-1]:
            role_name = "user" if msg["role"] == "user" else "model"
            chat_history.append(
                types.Content(
                    role=role_name,
                    parts=[types.Part.from_text(text=msg["text"])]
                )
            )

        # नई लाइब्रेरी (google-genai) के तरीके से चैट शुरू करना
        chat = client.chats.create(
            model="gemini-2.0-flash",
            history=chat_history,
            config=types.GenerateContentConfig(
                system_instruction=SCHOOL_DATA
            )
        )
        
        # मैसेज भेजना
        response = chat.send_message(user_input)

        # बॉट का जवाब दिखाना और सेव करना
        st.session_state.messages.append({"role": "assistant", "text": response.text})
        with st.chat_message("assistant"):
            st.write(response.text)
            
    except Exception as e:
        st.error(f"एक एरर आया है: {e}")
        
