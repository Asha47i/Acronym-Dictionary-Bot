import streamlit as st

def load_slang_dict():
    slang_dict = {}
    try:
        with open("slang.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    acronym, meaning = line.strip().split("=", 1)
                    slang_dict[acronym.strip().upper()] = meaning.strip()
    except FileNotFoundError:
        st.error("The slang.txt file was not found.")
    return slang_dict

slang_dict = load_slang_dict()

st.title("💬 Acronym Dictionary Bot")
st.markdown("Type an acronym like **LOL**, **BRB**, or **ILY** to see its full meaning.")

with st.container():
    st.subheader("🔥 Popular Acronyms")
    sample_acronyms = {
        "LMAO": "Laughing My A** Off",
        "ILY": "I Love You",
        "IYKYK": "If You Know You Know",
        "WTF": "What The F***",
        "BRB": "Be Right Back",
        "LOML": "Love Of My Life",
        "AFK": "Away From Keyboard",
    }
    for k, v in sample_acronyms.items():
        st.write(f"**{k}** = {v}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Enter an acronym (e.g., LOL, IC, ILY):"):
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = slang_dict.get(user_input.strip().upper(), "❌ Sorry, I couldn't find the definition for that acronym.")
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
