import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration
st.set_page_config(page_title="Sarathi-B.S.", page_icon="🤖", layout="centered")

# 2. PROFESSIONAL & CLEAN CSS (Matches 74598.jpg style)
st.markdown("""
    <style>
    /* Background and Layout */
    .stApp { background-color: #ffffff !important; }
    
    /* Input Box Styling */
    [data-testid="stChatInput"] {
        background-color: #f8f9fa !important;
        border: 1px solid #d1d5db !important;
        border-radius: 12px !important;
        padding: 5px !important;
    }
    
    /* Remove Avatars */
    [data-testid="chatAvatarIcon-user"], [data-testid="chatAvatarIcon-assistant"] {
        display: none !important;
    }

    /* Message Alignment */
    [data-testid="stChatMessage"] { padding: 10px !important; }
    
    /* Assistant Message (Left) */
    [data-testid="stChatMessage"]:not(:has([data-testid="chatAvatarIcon-user"])) [data-testid="stMarkdownContainer"] {
        background-color: #f3f4f6 !important;
        padding: 15px !important;
        border-radius: 15px !important;
        color: #1f2937 !important;
    }
    
    /* User Message (Right) */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        flex-direction: row-reverse;
    }
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] {
        background-color: #3b82f6 !important;
        padding: 15px !important;
        border-radius: 15px !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 style='text-align: center; color: #111827;'>Sarathi-B.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Your Intelligent School Companion ✨</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. RESTORED SCHOOL DATA (Master Data)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' (Pradhan Public Senior Secondary School), सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो। 
तुम्हारे पास स्कूल की पूरी जानकारी है, जो तुम्हें विस्तार से बतानी है:

- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम (अनुशासित और बेहतरीन नेतृत्व)।
- डायरेक्टर: मानवेंद्र छोंकर सर (विनम्र और सहयोगी)।
- एग्जामिनर: जगत प्रताप चौहान सर।
- फैकल्टी: 
   - कविता यादव मैम (इतिहास/भूगोल), 
   - विजय राठौर सर (राजनीति विज्ञान/इंग्लिश), 
   - विपिन अग्रवाल सर (गणित)।
- टॉपर्स: 10वीं देव छोंकर (98%), 12वीं प्रिया चौहान (96%)।
- सुविधाएं: स्मार्ट क्लासेस, बायोलॉजी लैब (असली सैंपल्स के साथ), केमिस्ट्री लैब।
- समय: गर्मी (सुबह 7 से 1 बजे), सर्दी (सुबह 8 से 2 बजे)।

नियम: हमेशा यूज़र की भाषा (Hindi/English/Hinglish) में विस्तार से जवाब दो और बहुत सम्मानजनक रहो।
"""

# 5. API Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key: st.stop()
client = genai.Client(api_key=api_key)

# 6. Session Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# 7. Chat Input & Processing
if user_input := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"): st.write(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.write("Sarathi is responding...")
        try:
            chat = client.chats.create(
                model="gemini-2.5-flash", 
                config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA, temperature=0.7)
            )
            response = chat.send_message(user_input)
            placeholder.write(response.text)
            st.session_state.messages.append({"role": "assistant", "text": response.text})
        except:
            placeholder.write("Error occurred. Please try again.")
            
