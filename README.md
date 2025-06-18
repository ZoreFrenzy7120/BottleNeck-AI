# BottleNeck-AI
it is command Assistant Ai

💡 Project Title: Bottleneck AI – Voice Assistant for Windows
📋 Description:
Bottleneck AI is a desktop-based Python voice assistant designed to interact with users via voice commands. It uses various Python libraries to perform a wide range of system-related tasks, access web services like OpenAI, and interact with the operating system.

🛠️ Key Features:
🎙️ Speech Recognition: Uses the microphone to listen and convert voice to text via Google Speech Recognition.

🔊 Text-to-Speech (TTS): Converts responses into spoken words using pyttsx3.

🤖 OpenAI Integration: Utilizes OpenAI's GPT model to answer general questions and respond conversationally.

🖥️ System Control:

Open applications like Notepad or Task Manager.

Lock the screen, shut down, or restart the system.

Check battery status and system resource usage (CPU, RAM).

📷 Camera Access: Opens the webcam and displays the video feed.

📂 File Management: Create, delete, or move files based on commands.

💬 Conversational Mode: Responds to casual prompts like telling jokes or talking like a friend.

🧩 Technologies & Libraries Used:
os, shutil, subprocess, ctypes: For system operations

pyttsx3: For text-to-speech

speech_recognition: For voice input

openai: To fetch responses from ChatGPT

psutil: For battery and system information

cv2 (OpenCV): For accessing the webcam

dotenv: For secure handling of the OpenAI API key
