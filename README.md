
Voice AI Assistant

🔹 Overview

Voice AI Assistant is a Python-based project that can process speech, detect diseases, and convert text to speech. It integrates both frontend and backend components to provide a seamless user experience.

🔹 Features

✔ Speech Processing – Converts spoken language into text
✔ Disease Detection – Predicts diseases based on symptoms
✔ Text-to-Speech (TTS) – Converts text into natural-sounding speech
✔ User-Friendly Interface – A simple web-based frontend

🔹 Tech Stack

Backend: Python (Flask), SpeechRecognition, Text-to-Speech (gTTS or pyttsx3)
Frontend: HTML, CSS, JavaScript
APIs: Any external APIs you are using

🔹 Installation & Setup

1️⃣ Clone the Repository:

git clone https://github.com/sanyagupta31/voice_ai_assistant.git
cd voice_ai_assistant

2️⃣ Install Dependencies:

pip install -r backend/requirements.txt

3️⃣ Run the Backend:

python backend/app.py

4️⃣ Open index.html in a Browser

🔹 Project Structure

voice_ai_assistant/
│── backend/
│   ├── app.py                  # Main backend application (Flask)
│   ├── speech_processing.py     # Handles speech recognition
│   ├── disease_detection.py     # Predicts diseases based on input
│   ├── text_to_speech.py        # Converts text to speech
│   ├── temp_audio.wav           # Temporary audio storage
│   ├── requirements.txt         # Python dependencies
│
│── frontend/
│   ├── index.html               # Web interface
│   ├── script.js                # Handles frontend logic
│   ├── styles.css               # Styling
│
├── response.mp3                 # Sample generated audio response
├── README.md                    # Project documentation

🔹 Future Improvements

✅ Improve AI model for disease detection
✅ Add voice command customization
✅ Enhance UI/UX

🔹 Contributors

👤 Sanya Gupta
Feel free to contribute by submitting a pull request!


---

✨ Let me know if you need modifications! 🚀
