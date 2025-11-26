# 🤖 LangGraph Streamlit Chatbot

**LangGraph Streamlit Chatbot** is a stateful conversational application built using Python. It combines **LangGraph** for managing conversation flow and memory with **Streamlit** for a clean, interactive user interface. The bot is powered by Google's **Gemini 2.5 Flash Lite** model to provide intelligent, context-aware responses.

-----

## 🌟 Key Features

  * **Stateful Conversations:** Utilizes `LangGraph`'s checkpointing system (`MemorySaver`) to retain conversation history, allowing the bot to "remember" previous interactions within a session.
  * **Powerful AI Model:** Integrates Google's `gemini-2.5-flash-lite` model via `langchain-google-genai` for fast and accurate language generation.
  * **Interactive UI:** Features a user-friendly chat interface built with **Streamlit**, which handles user input and displays the chat history in real-time.
  * **Modular Architecture:** Cleanly separates the frontend UI logic (`chatbot_frontend.py`) from the backend agent logic (`langgraph_backend.py`) for better code maintainability.
  * **Session Management:** Uses Streamlit's session state to manage the unique `thread_id` for each conversation, ensuring distinct chat sessions.

-----

## 🛠️ Technologies Used

  * **Backend:** Python
  * **Agent Framework:** LangGraph
  * **AI Framework:** LangChain
  * **Web Framework:** Streamlit
  * **AI Model:** Google Gemini (`gemini-2.5-flash-lite`)
  * **Key Libraries:**
      * `langgraph`
      * `langchain`
      * `langchain-google-genai`
      * `streamlit`
      * `pydantic`
      * `python-dotenv`

-----

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

  * Python 3.10 or later
  * A Google API Key with the Gemini API enabled. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/saiteja-puttoju/langgraph-streamlit-chatbot.git
    cd langgraph-streamlit-chatbot
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

      * Create a new file in the root of the project named `.env`.
      * Add your Google API key to this file:
        ```env
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

### Running the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run chatbot_frontend.py
````

Your web browser will automatically open to the application's user interface (usually at `http://localhost:8501`).

-----

## How to Use

1.  Open the application in your browser.
2.  Type your message or question into the input box at the bottom of the screen.
3.  Press **Enter**.
4.  The chatbot will process your input using LangGraph and display the response.
5.  Continue the conversation; the bot will remember the context of your previous messages.