import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration
st.set_page_config(page_title="Sarathi-B.S.", page_icon="🌐", layout="centered")

# 2. 3D Sky-Blue Professional Smile (Custom SVG)
BLUE_SMILE_B64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48ZGVmcz48cmFkaWFsR3JhZGllbnQgaWQ9ImdyYWQxIiBjeD0iMzUlIiBjeT0iMjUlIiByPSI2NSUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNlMGY3ZmEiIC8+PHN0b3Agb2Zmc2V0PSI0MCUiIHN0b3AtY29sb3I9IiM0ZmMzZjciIC8+PHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDI3N2JkIiAvPjwvcmFkaWFsR3JhZGllbnQ+PGZpbHRlciBpZD0ic2hhZG93Ij48ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI0IiBmbG9vZC1jb2xvcj0iIzAwMDAwMCIgZmxvb2Qtb3BhY2l0eT0iMC4zIi8+PC9maWx0ZXI+PC9kZWZzPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQ1IiBmaWxsPSJ1cmwoI2dyYWQxKSIgZmlsdGVyPSJ1cmwoI3NoYWRvdykiIC8+PGNpcmNsZSBjeD0iMzUiIGN5PSI0MCIgcj0iNiIgZmlsbD0iI2ZmZmZmZiIgLz48Y2lyY2xlIGN4PSI2NSIgY3k9IjQwIiByPSI2IiBmaWxsPSIjZmZmZmZmIiAvPjxwYXRoIGQ9Ik0gMzAgNjAgUSA1MCA3NSA3MCA2MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjYiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48L3N2Zz4="
BLUE_SMILE_AVATAR = f"data:image/svg+xml;base64,{BLUE_SMILE_B64}"

# 3. School Information (Hardcoded Data)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल', सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो। 
तुम्हारे पास स्कूल की पूरी जानकारी है, जिसे तुम्हें कभी नहीं भूलना है:
- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम (अनुशासित और बेहतरीन नेतृत्व)।
- डायरेक्टर: मानवेंद्र छोंकर सर (विनम्र और सहयोगी)।
- एग्जामिनर: जगत प्रताप चौहान सर।
- फैकल्टी: कविता यादव मैम (इतिहास/भूगोल), विजय राठौर सर (राजनीति विज्ञान/इंग्लिश), विपिन अग्रवाल सर (गणित)।
- टॉपर्स: 10वीं देव छोंकर (98%), 12वीं प्रिया चौहान (96%)।
- सुविधाएं: स्मार्ट क्लासेस, बायोलॉजी लैब (असली सैंपल्स के साथ), केमिस्ट्री लैब।
- समय: गर्मी (सुबह 7 से 1 बजे), सर्दी (सुबह 8 से 2 बजे)।

निर्देश:
1. हमेशा यूज़र की भाषा (English, Hindi, या Hinglish) में बात करो।
2. जवाब हमेशा विस्तार से और बुलेट पॉइंट्स में दो।
3. बहुत ही दोस्ताना (friendly) रहो और उपयुक्त इमोजीस का इस्तेमाल करो।
4. अगर कोई सवाल स्कूल के बाहर का है, तो विनम्रता से कहें कि आप केवल स्कूल के बारे में ही जानकारी दे सकते हैं।
"""

# 4. Professional CSS
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    [data-testid="stChatMessage"] { background-color: transparent !important; border: none !important; }
    
    /* Assistant Bubbles */
    [data-testid="stChatMessage"]:not(:has(.user-msg-hook)) [data-testid="stMarkdownContainer"] {
        background-color: #f3f4f6 !important; color: #1f2937 !important;
        border-radius: 15px 15px 15px 0px !important; padding: 12px 18px !important;
    }

    /* User Bubbles */
    [data-testid="stChatMessage"]:has(.user-msg-hook) { display: flex !important; flex-direction: row-reverse !important; }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stChatAvatar"] { display: none !important; }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stMarkdownContainer"] {
        background-color: #e0f2fe !important; color: #0369a1 !important;
        border-radius: 15px 15px 0px 15px !important; padding: 12px 18px !important;
    }
    
    .header-logo { width: 55px; animation: hover-smile 3s infinite ease-in-out; }
    @keyframes hover-smile { 0%, 100% { transform: translateY(0px) scale(1); } 50% { transform: translateY(-5px) scale(1.05); } }
    </style>
""", unsafe_allow_html=True)

# 5. Initialize State
if "messages" not in st.session_state: st.session_state.messages = []

# Sidebar Controls
with st.sidebar:
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# 6. Header
st.markdown(f"""<div style='text-align: center;'><img src='{BLUE_SMILE_AVATAR}' class='header-logo'>
    <h1 style='color: #111827; margin: 0;'>Sarathi-B.S.</h1>
    <p style='color: #6b7280;'>Your Intelligent School Companion ✨</p></div><br>""", unsafe_allow_html=True)

# 7. API Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("Enter your Google API Key:", type="password")
if not api_key: 
    st.warning("Please enter your API Key to start chatting.")
    st.stop()
client = genai.Client(api_key=api_key)

# 8. Render Chat History
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant", avatar=None if msg["role"] == "user" else BLUE_SMILE_AVATAR):
        content = f"<span class='user-msg-hook'></span>{msg['text']}" if msg["role"] == "user" else msg["text"]
        st.markdown(content, unsafe_allow_html=True)

# 9. Main Chat Loop
if user_input := st.chat_input("Ask me anything about the school..."):
    # Add to state
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(f"<span class='user-msg-hook'></span>{user_input}", unsafe_allow_html=True)

    # API Request
    api_contents = [types.Content(role="user" if m["role"] == "user" else "model", parts=[types.Part.from_text(text=m["text"])]) for m in st.session_state.messages]

    with st.chat_message("assistant", avatar=BLUE_SMILE_AVATAR):
        typing = st.empty()
        typing.markdown("💬 *Sarathi is thinking...*")
        try:
            response = client.models.generate_content_stream(
                model="gemini-2.5-flash", 
                contents=api_contents,
                config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA, temperature=0.7)
            )
            typing.empty()
            full_response = st.write_stream(response)
            st.session_state.messages.append({"role": "assistant", "text": full_response})
        except Exception as e:
            typing.empty()
            st.error(f"Something went wrong: {e}")
            
