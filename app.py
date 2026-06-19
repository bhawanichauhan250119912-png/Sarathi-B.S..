import streamlit as st
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
        # जेमिनी मॉडल लोड करना (System Instruction के साथ)
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=SCHOOL_DATA
        )

        # जेमिनी के लिए पुरानी चैट हिस्ट्री सही फॉर्मेट में तैयार करना
        formatted_history = []
        for msg in st.session_state.messages[:-1]:
            role_name = "user" if msg["role"] == "user" else "model"
            formatted_history.append({"role": role_name, "parts": [{"text": msg["text"]}]})

        # पुरानी हिस्ट्री के साथ चैट शुरू करना
        chat = model.start_chat(history=formatted_history)
        response = chat.send_message(user_input)

        # बॉट का जवाब दिखाना और सेव करना
        st.session_state.messages.append({"role": "assistant", "text": response.text})
        with st.chat_message("assistant"):
            st.write(response.text)
            
    except Exception as e:
        st.error(f"एक एरर आया है: {e}")

