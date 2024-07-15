import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""
        return command.lower()

# Function to handle the command
def handle_command(command):
    if 'hello' in command:
        speak("Hello! How can I help you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif 'open linkedin' in command:
        webbrowser.open("https://www.linkedin.com/feed/")
        speak("Opening LinkedIn")
    elif 'open twitter' in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
    elif 'open chrome' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Chrome")
    elif 'play music' in command:
        music_dir = 'path_to_your_music_directory' # replace with the path to your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")
    elif 'who are you' in command:
        speak("I am Jarvis, your personal voice assistant.")
    elif 'hobbies' in command:
        speak("I enjoy helping you with your tasks and learning new things.")
    elif 'weather' in command:
        speak("I currently don't have access to real-time weather data, but you can check your favorite weather website for the latest updates.")
    else:
        speak("Sorry, I didn't get that. Could you please repeat?")

# Main function to run the assistant
def run_jarvis():
    speak("Jarvis at your service. How can I assist you today?")
    while True:
        command = listen()
        if command:
            handle_command(command)
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_jarvis()
