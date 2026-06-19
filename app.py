import streamlit as st
from google import genai
from google.genai import types
import time
import os

# 1. Page configuration - Logo set as page_icon
st.set_page_config(
    page_title="sarathi-B.S.", 
    page_icon="74424.png",  # Yahan emoji ki jagah aapka naya logo aa gaya!
    layout="centered"
)


# --- Full-Proof Logo and Avatar Management ---
school_logo = "🤖" # Default backup emoji
for ext in ["png", "PNG", "jpg", "jpeg", "JPG"]:
    if os.path.exists(f"74424.{ext}"):
        school_logo = f"74424.{ext}"
        break

# 2. Main Premium Header Design (Gemini Inspired UI Layout)
st.title("🤖 sarathi-B.S.")
st.markdown("##### *Your Intelligent School Companion & AI Guide* ✨")
st.markdown("#### **स्वागत है प्रधान पब्लिक स्कूल में! 👋**")
st.markdown("---")

# 3. Secure API Key Setup (Streamlit Secrets & Sidebar Fallback)
api_key = None
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
elif hasattr(st, "sidebar") and api_key is None:
    api_key = st.sidebar.text_input("जेमिनी API की दर्ज करें:", type="password")

if not api_key:
    st.info("💡 **Setup Instruction:** Please configure `GOOGLE_API_KEY` in your Streamlit Secrets or provide it in the sidebar to wake up Sarathi.")
    st.stop()

# Initialize the official New GenAI Client safely
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Initialization Error: {e}")
    st.stop()

# 4. Master Data - Strict Prompts & Gemini Style Output Guidelines
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' के आधिकारिक AI गाइड हो। तुम्हारा नाम 'sarathi-B.S.' है।
तुमसे जो भी पूछा जाए, उसका जवाब तुम बिल्कुल एक प्रीमियम, बुद्धिमान, आधुनिक और अत्यंत सुलझे हुए AI की तरह दोगे।

⚠️ बातचीत और फॉर्मेटिंग के कड़े नियम (Strict Output Rules):
1. **भाषा शैली (Language Style - Hinglish):** तुम्हारी भाषा न तो बहुत कठिन शुद्ध हिंदी होनी चाहिए और न ही पूरी इंग्लिश। तुम्हें एक बहुत ही सुंदर, साफ, और सम्मानजनक Hinglish का उपयोग करना है (जैसे: "Namaste sir! School ka timing winter me subah 8:00 AM se hota hai..."). बातचीत में हमेशा 'जी', 'आप', 'मैम' और 'सर' का उपयोग करके अत्यंत आदरपूर्ण बातें करनी हैं।
2. **Gemini फॉर्मेटिंग शैली (Perfect Presentation):** कभी भी पूरा जवाब एक लंबे, बोरिंग पैराग्राफ में मत लिखना। बात को हमेशा सुंदर बुलेट पॉइंट्स (*) और छोटी हेडिंग्स (###) में बांटकर लिखना। मुख्य शब्दों, तारीखों, क्लास, और नामों को हमेशा **बोल्ड** करना ताकि यूजर को तुरंत समझ आये।
3. **Emojis का भरपूर उपयोग:** हर जवाब में उचित और प्यारे Emojis (😊, ✨, 🏫, 🧪, 👨‍🏫) का स्वभाविक रूप से इस्तेमाल करें।

🏛️ स्कूल मैनेजमेंट का सटीक विवरण (Master Data):
- ### 👥 स्कूल मैनेजमेंट (School Management)
  - **प्रिंसिपल मैम:** श्रीमती **मोनिका छोंकर मैम** (Mrs. Monika Chhonkar) - अत्यंत अनुशासित, कुशल मार्गदर्शक और बेहद प्रभावशाली इंग्लिश (**Fluent English**) बोलने वालीं।
  - **डायरेक्टर सर:** **मानवेंद्र छोंकर सर** (Manvendra Chhonkar) - बहुत ही शांत, सीधे और विनम्र (**Polite**) स्वभाव के धनी।
  - **एग्जामिनर सर:** **जगत प्रताप चौहान सर**।
  - **फीस काउंटर:** **संतोष यादव सर** (सहायक: **चंचल मैम**)।

📚 स्कूल की मुख्य जानकारियां:
- ### 📍 स्थान एवं कैंपस (Location & Campus)
  - **पता:** **प्रधान पब्लिक सीनियर सेकेंडरी स्कूल**, सीगना, आगरा (रायपुरा जाट के आगे)।
  - **कैंपस:** सामने विशाल **असेंबली ग्राउंड**, साइड में हरा-भरा **लौन** और पीछे खेलकूद के लिए एक बहुत बड़ा शानदार **प्लेग्राउंड** है।
  - **अनुशासन:** स्कूल अपने कड़े अनुशासन के लिए जाना जाता है। आगरा की खेल प्रतियोगिताओं में अक्सर हमारा स्कूल ही **प्रथम स्थान** पर आता है।

👨‍🏫 कक्षा 11 के शिक्षक (Faculty):
- ### 👨‍🏫 फैकल्टी (Class 11 Teachers)
  - **कविता यादव मैम:** इतिहास (**History**) और भूगोल (**Geography**) की विशेषज्ञ।
  - **विजय राठौर सर:** राजनीति विज्ञान (**Political Science**), **Fine Arts**, **संविधान** और **इंग्लिश ग्रामर** के बेहतरीन शिक्षक।
  - **विपिन अग्रवाल सर:** गणित (**Maths**) के अत्यंत लोकप्रिय और जादुई शिक्षक।

🧪 प्रयोगशालाएं और सुविधाएं:
- ### 🧪 लैब्स और सुविधाएं (Modern Infrastructure)
  - सभी कक्षाएं हवादार हैं और **स्मार्ट क्लास** (Smart Classroom) की आधुनिक सुविधा से लैस हैं।
  - **बायोलॉजी लैब (Biology Lab):** यहाँ केमिकल्स में सुरक्षित रखे गए असली सैंपल्स (जैसे **रियल फिश, ऑक्टोपस, एल्गी**) मौजूद हैं।
  - **केमिस्ट्री लैब (Chemistry Lab):** पूर्ण सुरक्षा मानकों के साथ सभी आवश्यक केमिकल्स उपलब्ध हैं।

⏰ विद्यालय का समय (School Timings):
- ### ⏰ स्कूल का समय
  - **गर्मियों में (Summer Time):** सुबह **7:00 AM** से दोपहर **1:00 PM** तक।
  - **सर्दियों में (Winter Time):** सुबह **8:00 AM** से दोपहर **2:00 PM** तक।

🏆 उत्कृष्ट परीक्षा परिणाम (Board Results):
- ### 🏆 टॉपर्स (Board Exam Results)
  - **कक्षा 10वीं:** **देव छोंकर** ने **98%** अंक प्राप्त कर विद्यालय टॉप किया।
  - **कक्षा 12वीं:** **प्रिया चौहान** ने **96%** अंकों के साथ सर्वोच्च स्थान प्राप्त किया।
"""

# 5. Session State Memory & Rate Limiter Setup
if "request_times" not in st.session_state:
    st.session_state.request_times = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history with updated clean avatars
for msg in st.session_state.messages:
    custom_avatar = "👤" if msg["role"] == "user" else school_logo
    with st.chat_message(msg["role"], avatar=custom_avatar):
        st.write(msg["text"])

# 6. Chat input interface
user_input = st.chat_input("स्कूल या टीचर्स के बारे में सारथी से पूछें...")

if user_input:
    current_time = time.time()
    # Filter out requests older than 60 seconds
    st.session_state.request_times = [t for t in st.session_state.request_times if current_time - t < 60]
    
    # Preventing API spam on free tier
    if len(st.session_state.request_times) >= 10:
        st.warning("⚠️ **चेतावनी:** आप बहुत तेज़ी से सवाल पूछ रहे हैं! कृपया थोड़ा रुक कर पूछें।")
        st.stop()

    st.session_state.request_times.append(current_time)
    
    # Append user prompt and display it instantly
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    # Reconstruct history dynamically using correct google-genai structured types
    chat_history = []
    for msg in st.session_state.messages[:-1]:
        role_name = "user" if msg["role"] == "user" else "model"
        chat_history.append(
            types.Content(role=role_name, parts=[types.Part.from_text(text=msg["text"])])
        )

    # 7. AI Processing block with elegant loading spinner (Gemini-style)
    with st.chat_message("assistant", avatar=school_logo):
        with st.spinner("सारथी टाइप कर रहा है... ✨"):
            try:
                # Setting up the model session with runtime system instructions
                chat = client.chats.create(
                    model="gemini-2.5-flash",
                    history=chat_history,
                    config=types.GenerateContentConfig(
                        system_instruction=SCHOOL_DATA,
                        temperature=0.7
                    )
                )
                
                # Fetching response from Gemini 2.5
                response = chat.send_message(user_input)
                
                # Display and store output safely
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "text": response.text})
                
            except Exception as e:
                err_message = str(e).upper()
                if "503" in err_message or "UNAVAILABLE" in err_message:
                    st.info("🏫 **सारथी संदेश:** सर्वर पर थोड़ा ट्रैफिक है। कृपया 5-10 सेकंड रुक कर दोबारा पूछें! 😊")
                elif "429" in err_message or "RESOURCE_EXHAUSTED" in err_message:
                    st.warning("⏳ **सारथी संदेश:** दैनिक निशुल्क सीमा (Free Limit) समाप्त। कृपया थोड़ी देर बाद प्रयास करें। 🙏")
                else:
                    st.error("⚠️ **तकनीकी संदेश:** नेटवर्क में कुछ रुकावट है या API Key अमान्य है। कृपया पुनः प्रयास करें।")
                
