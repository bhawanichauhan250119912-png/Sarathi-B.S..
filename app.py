import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration
st.set_page_config(page_title="Sarathi-B.S.", page_icon="😊", layout="centered")

# 2. WELCOME SPLASH SCREEN (Req 5)
if "app_started" not in st.session_state:
    splash = st.empty()
    with splash.container():
        st.markdown("""
        <style>
        @keyframes bounce-splash {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-20px) scale(1.1); }
        }
        .splash-emoji {
            font-size: 100px;
            text-align: center;
            animation: bounce-splash 1.5s infinite ease-in-out;
            color: #ff6b6b; /* Light reddish */
        }
        .splash-text {
            color: #1f2937;
            text-align: center;
            font-family: sans-serif;
            margin-top: 20px;
            font-size: 26px;
            font-weight: bold;
        }
        </style>
        <div style="height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div class="splash-emoji">😊</div>
            <div class="splash-text">[Welcome to Pradhan Public School]</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(3) # Wait for 3 seconds
    splash.empty() # Remove splash screen after 3 seconds
    st.session_state.app_started = True

# 3. PROFESSIONAL & CLEAN CSS (Req 2, 3, 4)
st.markdown("""
    <style>
    /* Background */
    .stApp { background-color: #ffffff !important; }
    
    /* Input Box Styling */
    [data-testid="stChatInput"] {
        background-color: #f8f9fa !important;
        border: 1px solid #d1d5db !important;
        border-radius: 12px !important;
    }
    
    /* Continuous Animation for Header Logo */
    @keyframes pulse-smile {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); text-shadow: 0 0 10px rgba(255,107,107,0.5); }
        100% { transform: scale(1); }
    }
    .header-logo {
        display: inline-block;
        animation: pulse-smile 2s infinite ease-in-out;
        font-size: 42px;
        color: #ff6b6b;
    }

    /* Message Bubbles layout (Not full width) */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        padding: 5px 0px !important;
    }
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        width: fit-content !important;
        max-width: 80% !important;
        padding: 12px 18px !important;
        border-radius: 20px !important;
        display: inline-block !important;
        word-wrap: break-word !important;
    }

    /* HIDE USER AVATAR entirely */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stChatAvatar"] {
        display: none !important;
    }

    /* USER MESSAGE (Right Alignment & Blue Bubble) */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        flex-direction: row-reverse !important;
    }
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] {
        background-color: #3b82f6 !important;
        color: white !important;
        border-bottom-right-radius: 4px !important;
    }

    /* ASSISTANT MESSAGE (Left Alignment & Gray Bubble) */
    [data-testid="stChatMessage"]:not(:has([data-testid="chatAvatarIcon-user"])) [data-testid="stMarkdownContainer"] {
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
        border-bottom-left-radius: 4px !important;
    }

    /* Typing Animation CSS */
    .typing-container {
        display: flex;
        align-items: center;
        background-color: #f3f4f6;
        padding: 12px 18px;
        border-radius: 20px;
        border-bottom-left-radius: 4px;
        width: fit-content;
        color: #6b7280;
        font-family: sans-serif;
    }
    .dot {
        height: 8px; width: 8px;
        background-color: #ff6b6b;
        border-radius: 50%;
        display: inline-block;
        margin: 0 3px;
        animation: bounce-dot 1.4s infinite ease-in-out both;
    }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes bounce-dot {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    .typing-text { margin-left: 10px; font-size: 14px; font-weight: 500; font-style: italic;}
    </style>
""", unsafe_allow_html=True)

# 4. Header with Animated Logo
st.markdown("<h1 style='text-align: center; color: #111827;'><span class='header-logo'>😊</span> Sarathi-B.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Your Intelligent School Companion ✨</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 5. REFINED SCHOOL DATA (Req 1 & Req 6)
SCHOOL_DATA = """
तुम 'प्रधान पब्लिक सीनियर सेकेंडरी स्कूल' (Pradhan Public Senior Secondary School), सीगना, आगरा के आधिकारिक AI गाइड 'Sarathi-B.S.' हो। 

तुम्हारे पास स्कूल की पूरी जानकारी है:
- प्रिंसिपल: श्रीमती मोनिका छोंकर मैम (अनुशासित और बेहतरीन नेतृत्व)।
- डायरेक्टर: मानवेंद्र छोंकर सर (विनम्र और सहयोगी)।
- एग्जामिनर: जगत प्रताप चौहान सर।
- फैकल्टी: कविता यादव मैम (इतिहास/भूगोल), विजय राठौर सर (राजनीति विज्ञान/इंग्लिश), विपिन अग्रवाल सर (गणित)।
- टॉपर्स: 10वीं देव छोंकर (98%), 12वीं प्रिया चौहान (96%)।
- सुविधाएं: स्मार्ट क्लासेस, बायोलॉजी लैब (असली सैंपल्स के साथ), केमिस्ट्री लैब।
- समय: गर्मी (सुबह 7 से 1 बजे), सर्दी (सुबह 8 से 2 बजे)।

**तुम्हारे लिए सख्त निर्देश (Strict Instructions):**
1. **भाषा:** यूज़र जिस भाषा में पूछे उसी में जवाब दो (English, Hindi, या Hinglish)। प्राकृतिक और फ्लोइंग भाषा का उपयोग करो।
2. **प्रारूप (Formatting):** जवाब हमेशा विस्तार से (detailed) और बुलेट पॉइंट्स (point-wise) में दो ताकि पढ़ने में आसानी हो।
3. **व्यवहार:** बहुत ही दोस्ताना (friendly), विनम्र और सम्मानजनक रहो। 
4. **इमोजी (Emojis):** हर वाक्य और पॉइंट के साथ उपयुक्त और खुशमिज़ाज इमोजी (😊, 🎓, ✨, 📚, 🔬) का भरपूर इस्तेमाल करो।
"""

# 6. API Setup
api_key = st.secrets.get("GOOGLE_API_KEY") or st.sidebar.text_input("API Key:", type="password")
if not api_key: st.stop()
client = genai.Client(api_key=api_key)

# 7. Session Logic & Memory
if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash", 
        config=types.GenerateContentConfig(system_instruction=SCHOOL_DATA, temperature=0.7)
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages
for msg in st.session_state.messages:
    # Use standard user avatar (hidden by CSS) and custom reddish emoji for assistant
    avatar_icon = "😊" if msg["role"] == "assistant" else "user"
    with st.chat_message(msg["role"], avatar=avatar_icon):
        st.markdown(msg["text"])

# 8. Chat Input & Processing
if user_input := st.chat_input("Ask me anything..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user", avatar="user"): 
        st.markdown(user_input)

    # Add Assistant Message with Typing Animation
    with st.chat_message("assistant", avatar="😊"):
        # Temporary placeholder for 3-dots typing animation
        typing_indicator = st.empty()
        typing_indicator.markdown("""
            <div class="typing-container">
                <div class="dot"></div><div class="dot"></div><div class="dot"></div>
                <span class="typing-text">[Sarathi is responding]</span>
            </div>
        """, unsafe_allow_html=True)
        
        try:
            # Get streaming response
            response_stream = st.session_state.chat_session.send_message_stream(user_input)
            
            def stream_generator():
                for chunk in response_stream:
                    yield chunk.text
                    
            # Clear the typing animation just before writing the real text
            typing_indicator.empty() 
            
            # Write stream output
            full_response = st.write_stream(stream_generator)
            
            # Save to memory
            st.session_state.messages.append({"role": "assistant", "text": full_response})
            
        except Exception as e:
            typing_indicator.empty()
            st.error(f"Error: {e}")
            
