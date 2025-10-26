Local Command-Line Chatbot

This project is a fully functional local chatbot interface that runs in your terminal. It uses a Hugging Face text generation model (Qwen/Qwen3-4B-Instruct-2507) via an API and maintains a conversational context using a sliding window memory.

This project was built to demonstrate a modular and maintainable Python structure.

Features

Modular Code: The project is split into three distinct modules:

inference.py: The main command-line interface (CLI) for user interaction.

agent_model.py: Handles loading the Hugging Face model and processing messages.

memory.py: Manages the chat history with a sliding window.

Sliding Window Memory: The chatbot remembers the last 5 turns of conversation to provide coherent, multi-turn replies.

Simple CLI: A robust command-line interface that accepts continuous input and terminates gracefully with the /exit command.

Code Structure

inference.py: This is the main entry point for the application. It runs a while loop to capture user input, sends it to the agent_model, prints the AI's response, and saves both messages to the memory.

agent_model.py: This file connects to the Hugging Face API using HuggingFaceEndpoint and loads the model into a ChatHuggingFace wrapper. Its agent_msg function takes a list of messages, gets a response from the AI, and returns it as an AIMessage object.

memory.py: This file contains the chat_history class. It is initialized with a window size (e.g., 5 turns) and stores messages in a list. When the list is full, it removes the oldest message before adding the newest one (FIFO).

Setup Instructions

Clone the Repository:

git clone [https://github.com/InfernoAlpha/ATG-task.git](https://github.com/InfernoAlpha/ATG-task)
cd your-project-directory


Create and Activate a Virtual Environment:

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate


Install Dependencies:
Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt


Create Your Environment File:
Create a file named .env in the main project directory. This file will securely store your API key.

Add Your API Key:
Open the .env file and add your Hugging Face API token. You can get one from the Hugging Face website.

HUGGINGFACE_API_TOKEN="hf_YOUR_API_TOKEN_GOES_HERE"


How to Run

Ensure your virtual environment is activated.

Run the inference.py script from your terminal:

python inference.py


The chatbot will start. You can begin typing your messages.

To stop the chatbot, type /exit and press Enter.

Sample Interaction

Here is a sample of what a conversation with the chatbot looks like:

Human: What is the capital of France?
AI: The capital of France is Paris.
Human: And what about Italy?
AI: The capital of Italy is Rome.
Human: What's a famous landmark in the first city you mentioned?
AI: A famous landmark in Paris is the Eiffel Tower.
Human: /exit