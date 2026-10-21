&#x20;Gemma Study Buddy \& Code Assistant



An offline, privacy-first AI study and coding companion powered by Google Gemma 2 (2B), Ollama, and Streamlit.



Built for Road to Devfest: Opensource Edition (Bengaluru).



🌟 Key Features



Adaptive Personas:



Code Explainer \& Reviewer: Analyzes code snippets, pinpoints bugs, explains algorithmic logic, and recommends clean solutions.



Exam Study Buddy: Breaks down complex computer science and engineering topics into easy-to-digest real-world analogies.



General Q\&A: Fast, lightweight knowledge retrieval.



100% Offline \& Private: Zero external API dependencies, zero cloud subscriptions, zero data leaving your machine.



Fast Local Streaming: Real-time token streaming using Gemma 2 (2B)'s compact footprint via Ollama.



🛠️ Architecture \& Tech Stack



Model: Google Gemma 2 (2B parameters)



Local Inference Engine: Ollama



User Interface: Streamlit (Python)



Runtime Environment: Python 3.10+



🚀 Quickstart Guide



Prerequisites



Install Ollama.



Pull Google's Gemma 2B model:



ollama run gemma2:2b





(Type /bye once the download reaches 100%)



Installation \& Run



Clone or download this repository:



git clone https://github.com/<your-username>/gemma-study-assistant.git

cd gemma-study-assistant





Install the required Python dependencies:



pip install -r requirements.txt





Start the application:



streamlit run app.py





The app will open automatically in your browser at http://localhost:8501.



📄 License



This project is licensed under the MIT License - see the LICENSE file for details.

