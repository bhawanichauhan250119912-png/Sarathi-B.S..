import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration
st.set_page_config(page_title="Sarathi-B.S.", page_icon="🌐", layout="centered")

# 2. 3D Sky-Blue Professional Smile (Custom SVG Base64)
# Yeh ek code-generated 3D sky-bluish smiling ball hai.
BLUE_SMILE_B64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48ZGVmcz48cmFkaWFsR3JhZGllbnQgaWQ9ImdyYWQxIiBjeD0iMzUlIiBjeT0iMjUlIiByPSI2NSUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNlMGY3ZmEiIC8+PHN0b3Agb2Zmc2V0PSI0MCUiIHN0b3AtY29sb3I9IiM0ZmMzZjciIC8+PHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDI3N2JkIiAvPjwvcmFkaWFsR3JhZGllbnQ+PGZpbHRlciBpZD0ic2hhZG93Ij48ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI0IiBmbG9vZC1jb2xvcj0iIzAwMDAwMCIgZmxvb2Qtb3BhY2l0eT0iMC4zIi8+PC9maWx0ZXI+PC9kZWZzPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQ1IiBmaWxsPSJ1cmwoI2dyYWQxKSIgZmlsdGVyPSJ1cmwoI3NoYWRvdykiIC8+PGNpcmNsZSBjeD0iMzUiIGN5PSI0MCIgcj0iNiIgZmlsbD0iI2ZmZmZmZiIgLz48Y2lyY2xlIGN4PSI2NSIgY3k9IjQwIiByPSI2IiBmaWxsPSIjZmZmZmZmIiAvPjxwYXRoIGQ9Ik0gMzAgNjAgUSA1MCA3NSA3MCA2MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjYiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48L3N2Zz4="
BLUE_SMILE_AVATAR = f"data:image/svg+xml;base64,{BLUE_SMILE_B64}"

# 3. Welcome Splash Screen (Runs only once)
if "app_started" not in st.session_state:
    splash = st.empty()
    with splash.container():
        st.markdown(f"""
        <style>
        @keyframes bounce-splash {{
            0%, 100% {{ transform: translateY(0) scale(1); }}
            50% {{ transform: translateY(-20px) scale(1.1); }}
        }}
        .splash-emoji {{
            text-align: center;
            animation: bounce-splash 1.5s infinite ease-in-out;
        }}
        .splash-text {{
            color: #1f2937; text-align: center; font-family: sans-serif;
            margin-top: 20px; font-size: 26px; font-weight: bold;
        }}
        </style>
        <div style="height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div class="splash-emoji"><img src="{BLUE_SMILE_AVATAR}" width="100"></div>
            <div class="splash-text">[Welcome to Pradhan Public School]</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2.5) 
    splash.empty() 
    st.session_state.app_started = True

# 4. Professional CSS & Layout Formatting
st.markdown("""
    <style>
    /* Background */
    .stApp { background-color: #ffffff !important; }
    
    /* Transparent Chat Wrapper */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: none !important;
        padding: 5px !important;
    }
    
    /* ------------------------------------------- */
    /* ASSISTANT MESSAGE STYLING (Left Aligned)    */
    /* ------------------------------------------- */
    [data-testid="stChatMessage"]:not(:has(.user-msg-hook)) [data-testid="stMarkdownContainer"] {
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
        border-radius: 15px 15px 15px 0px !important;
        padding: 12px 18px !important;
        width: fit-content !important;
        max-width: 85% !important;
    }

    /* ------------------------------------------- */
    /* USER MESSAGE STYLING (Right Aligned)        */
    /* ------------------------------------------- */
    [data-testid="stChatMessage"]:has(.user-msg-hook) {
        display: flex !important;
        flex-direction: row-reverse !important;
    }
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stMarkdownContainer"] {
        background-color: #e0f2fe !important; /* Light sky blue bubble */
        color: #0369a1 !important;
        border-radius: 15px 15px 0px 15px !important;
        padding: 12px 18px !important;
        width: fit-content !important;
        max-width: 85% !important;
    }
    
    /* STRICTLY HIDE USER AVATAR */
    [data-testid="stChatMessage"]:has(.user-msg-hook) [data-testid="stChatAvatar"] {
        display: none !important; 
    }
    
    /* Chat Input Box */
    [data-testid="stChatInput"] {
        background-color: #f8f9fa !important;
        border: 1px solid #d1d5db !important;
        border-radius: 12px !important;
    }

    /* 3-Dots Typing Animation CSS */
    .typing-container {
        display: flex; align-items: center; background-color: #f3f4f6;
        padding: 12px 18px; border-radius: 15px 15px 15px 0px; width: fit-content;
    }
    .dot {
        height: 8px; width: 8px; background-color: #0288d1; border-radius: 50%;
        display: inline-block; margin: 0 3px; animation: bounce-dot 1.4s infinite ease-in-out both;
    }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes bounce-dot {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    .typing-text { margin-left: 10px; font-size: 14px; font-style: italic; color: #6b7280; font-family: sans-serif;}

    /* Header Logo Hover Animation */
    @keyframes hover-smile {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-5px) scale(1.05); }
    }
    .header-logo { width: 55px; animation: hover-smile 3s infinite ease-in-out; }
    </style>
""", unsafe_allow_html=True)

# 5. Header with 3D Sky-Blue Smile
st.markdown(f"""
    <div style='text-align: center;'>
        <img src='{BLUE_SMILE_AVATAR}' class='header-logo'>
        <h1 style='color: #111827; margin: 0;'>Sarathi-B.S.</h1>
        <p style='color: #6b7280; margin-top: 5px;'>Your Intelligent School Companion ✨</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# 6. School Instructions Context
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल', सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो। 
तुम्हारे पास स्कूल की पूरी जानकारी है:
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
"""

# 7. API Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key: st.stop()
client = genai.Client(api_key=api_key)

# 8. Memory State (Only store messages, NO chat_session to prevent closing error)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            # The span hook allows CSS to right-align the message
            st.markdown("<span class='user-msg-hook'></span>" + msg["text"], unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar=BLUE_SMILE_AVATAR):
            st.markdown(msg["text"])

# 9. Chat Processing & Generation
if user_input := st.chat_input("Ask me anything..."):
    # Store User Input
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"): 
        st.markdown("<span class='user-msg-hook'></span>" + user_input, unsafe_allow_html=True)

    # Rebuild Message History for API explicitly (Fixes "Client Closed" issue)
    api_contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        api_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["text"])]))

    # Display typing indicator temporarily
    with st.chat_message("assistant", avatar=BLUE_SMILE_AVATAR):
        typing_indicator = st.empty()
        typing_indicator.markdown("""
            <div class="typing-container">
                <div class="dot"></div><div class="dot"></div><div class="dot"></div>
                <span class="typing-text">[Sarathi is responding]</span>
            </div>
        """, unsafe_allow_html=True)
        
        try:
            # Create a FRESH call directly passing the history content
            response_stream = client.models.generate_content_stream(
                model="gemini-2.5-flash", 
                contents=api_contents,
                config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA, temperature=0.7)
            )
            
            # Clear animation and write stream
            typing_indicator.empty()
            
            def stream_generator():
                for chunk in response_stream:
                    yield chunk.text
                    
            full_response = st.write_stream(stream_generator)
            st.session_state.messages.append({"role": "assistant", "text": full_response})
            
        except Exception as e:
            typing_indicator.empty()
            st.error(f"Error fetching response: {e}")
            
