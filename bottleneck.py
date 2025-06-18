import os 
import pyttsx3
import speech_recognition as sr
import openai
import psutil
import cv2
import sys
import shutil
import subprocess
import ctypes

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key securely
openai.api_key = os.getenv("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.env")

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Could not connect to the speech service.")
            return ""

def ask_openai(prompt):
    """Ask OpenAI for a response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        speak("There was an error accessing OpenAI.")
        return str(e)

def open_app(app_name):
    """Open the specified application."""
    os.system(f"start {app_name}")

def shutdown():
    """Shut down the system."""
    os.system("shutdown /s /t 5")

def restart():
    """Restart the system."""
    os.system("shutdown /r /t 5")

def check_battery():
    """Check the battery status."""
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery level is {battery.percent} percent.")
        return f"Battery level: {battery.percent}%"
    else:
        return "Battery information not available."

def open_camera():
    """Access the camera and display the feed."""
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera', frame)
            cv2.waitKey(5000)  # Show for 5 seconds
        cap.release()
    else:
        speak("Unable to access the camera.")
    cv2.destroyAllWindows()

def manage_files(command):
    """Handle file operations like create, delete, and move."""
    if "create file" in command:
        with open("newfile.txt", "w") as file:
            file.write("This is a new file.")
        speak("File created successfully.")
    elif "delete file" in command:
        os.remove("newfile.txt")
        speak("File deleted successfully.")
    elif "move file" in command:
        shutil.move("newfile.txt", "C:\\Users\\Public")
        speak("File moved successfully.")

def get_system_info():
    """Retrieve system information like CPU and RAM usage."""
    info = f"CPU usage: {psutil.cpu_percent()} percent. Memory usage: {psutil.virtual_memory().percent} percent."
    speak(info)
    return info

def open_task_manager():
    """Open Task Manager."""
    subprocess.run("taskmgr")

def lock_screen():
    """Lock the system screen."""
    os.system("rundll32.exe user32.dll,LockWorkStation")

def process_command(command):
    """Process and execute the given command."""
    if "open notepad" in command:
        speak("Opening Notepad")
        open_app("notepad")
    elif "shutdown" in command:
        speak("Shutting down the system")
        shutdown()
    elif "restart" in command:
        speak("Restarting the system")
        restart()
    elif "battery status" in command:
        battery_status = check_battery()
        print(battery_status)
    elif "open camera" in command:
        speak("Opening the camera")
        open_camera()
    elif "system info" in command:
        info = get_system_info()
        print(info)
    elif "task manager" in command:
        speak("Opening Task Manager")
        open_task_manager()
    elif "lock screen" in command:
        speak("Locking the screen")
        lock_screen()
    elif "open Google" in command:
        speak("Opening Google")
        open_app("https://www.google.com")
        open_google()
    elif "what is your name" in command:
        speak("My name is Bottleneck AI. I am here to assist you.")
    elif "talk like a friend" in command:
        speak("Hey buddy! How's your day going? You can talk to me about anything.")
    elif "tell me a joke" in command:
        response = ask_openai("Tell me a joke.")
        speak(response)
        print(f"Bottleneck: {response}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        response = ask_openai(command)
        print(f"Bottleneck : {response}")
        speak(response)
    return True

def bottleneck():
    """Main function to run the AI assistant."""
    speak("Hello Sir , I am Bottle  neck AI. what can i help you today and what is a work for me ?")
    while True:
        query = listen()
        if query:
            if not process_command(query):
                break

if __name__ == "__main__":
    bottleneck()





    