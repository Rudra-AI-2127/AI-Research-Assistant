import streamlit as st
from agent import ResearchAgent

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align: center;
}

/* Chat Bubble */
.stChatMessage {
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161A23;
}

/* Metric Card */
[data-testid="metric-container"] {
    background-color: #1E2330;
    border: 1px solid #31333F;
    padding: 15px;
    border-radius: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    padding-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------
if "agent" not in st.session_state:
    st.session_state.agent = ResearchAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:

    st.title("⚙️ Controls")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.agent.memory.clear()
        st.rerun()

    st.divider()

    st.subheader("🚀 Features")

    st.markdown("""
    - 🧠 Short-Term Memory
    - 🔢 Calculator Tool
    - 📚 Wikipedia Tool
    - 🌐 Web Search Tool
    - 🔀 Multi-Hop Reasoning
    - ⚡ Parallel Tool Calling
    """)

    st.divider()

    st.metric(
        "Conversation Messages",
        len(st.session_state.messages)
    )

    st.metric(
        "Memory Window",
        "10 Messages"
    )

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("🤖 AI Research Assistant")

st.caption(
    "Powered by Gemini • Tool Calling • Memory • Multi-Hop Reasoning"
)

st.divider()

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
prompt = st.chat_input(
    "Ask me anything..."
)

# ---------------------------------------------------
# User Query
# ---------------------------------------------------
if prompt:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):

            response = (
                st.session_state.agent
                .chat_with_agent(prompt)
            )

        st.markdown(response)

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.divider()

