# 🤖 AI Research Assistant

A powerful **Agentic AI Research Assistant** built using **Google Gemini**, **Streamlit**, and **Python**. This assistant can reason, use tools, remember conversations, perform multi-step reasoning, and execute tasks in parallel.

---

## 🚀 Features

* 🧠 **Short-Term Memory** for multi-turn conversations
* 🔢 **Calculator Tool** for mathematical computations
* 📚 **Wikipedia Tool** for factual knowledge retrieval
* 🌐 **Web Search Tool** for current information and news
* 🔀 **Multi-Hop Tool Calling** for sequential reasoning
* ⚡ **Parallel Tool Calling** for simultaneous task execution
* 💬 **Conversational AI** powered by Google Gemini
* 🎨 **Interactive Streamlit UI**
* 🏗️ **Modular and Scalable Architecture**

---

## 🏗️ System Architecture

```text
                    ┌───────────────────┐
                    │   Streamlit UI    │
                    └─────────┬─────────┘
                              │
                              ▼
                 ┌─────────────────────┐
                 │  Research Agent     │
                 └─────────┬───────────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
    ┌────────────┐ ┌────────────┐ ┌────────────┐
    │   Memory   │ │  Planner   │ │ Parallel  │
    │   Module   │ │   Agent    │ │ Executor  │
    └────────────┘ └────────────┘ └────────────┘
                           │
                           ▼
                ┌─────────────────┐
                │  Tool Router    │
                └────────┬────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
┌────────────┐   ┌────────────┐   ┌────────────┐
│ Calculator │   │ Wikipedia  │   │ Web Search│
└────────────┘   └────────────┘   └────────────┘
```

---

## 📂 Project Structure

```text
AI-Research-Assistant/
│
├── .streamlit/
│   └── config.toml
│
├── agents/
│   ├── __init__.py
│   ├── parallel_executor.py
│   └── planner.py
│
├── memory/
│   ├── __init__.py
│   ├── short_term.py
│   └── summary_memory.py
│
├── prompts/
│   └── system_prompt.txt
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── web_search.py
│   └── wikipedia_tool.py
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── agent.py
├── app.py
├── config.py
├── main.py
└── requirements.txt
```

---

## 🧠 Agent Capabilities

### 🔢 Calculator Tool

Performs arithmetic calculations.

**Example:**

```text
User: What is (250 + 100) * 5?
Assistant: 1750
```

---

### 📚 Wikipedia Tool

Retrieves factual information.

**Example:**

```text
User: Who created Java?
Assistant: James Gosling created Java at Sun Microsystems.
```

---

### 🌐 Web Search Tool

Fetches recent information from the web.

**Example:**

```text
User: Latest AI news today
```

---

### 🔀 Multi-Hop Tool Calling

Executes multiple reasoning steps to answer complex questions.

**Example:**

```text
User: What is the age of the creator of Python?

Step 1 → Find creator
Step 2 → Find birth year
Step 3 → Calculate age
```

---

### ⚡ Parallel Tool Calling

Runs multiple tasks simultaneously.

**Example:**

```text
User: Compare latest AI and blockchain news
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Rudra-AI-2127/AI-Research-Assistant.git

cd AI-Research-Assistant
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
MODEL_NAME=gemini-2.5-flash
```

Get your Gemini API key from:

https://aistudio.google.com/

---

## ▶️ Running the Application

### Terminal Version

```bash
python main.py
```

### Streamlit UI

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 💻 Tech Stack

* Python
* Google Gemini API
* Streamlit
* Wikipedia API
* DDGS Search
* Concurrent Futures
* Python Dotenv

---

## 📸 Screenshots

### Streamlit Interface

Add your screenshots inside an `assets/` folder.

```text
assets/
├── home.png
├── chat.png
```

Example:

```markdown
![Home Screen](assets/home.png)

![Chat Interface](assets/chat.png)
```

---

## 🔮 Future Improvements

* Long-Term Memory
* SQLite Chat Storage
* Reflection/Critic Agent
* RAG Integration
* Voice Interaction
* Autonomous Planning

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Rudra Pratap Singh Rathore**

GitHub: https://github.com/Rudra-AI-2127

---

⭐ If you found this project useful, please consider giving it a star!
