import speech_recognition as sr
import webbrowser
import os
import subprocess

r = sr.Recognizer()

def record_text():
    print("Listening for input...")  # Debugging output
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, timeout=5)  # Added timeout for quicker response
            print("Audio received, processing...")  # Debugging output

            # Recognize the speech using Google
            MyText = r.recognize_google(audio)
            print(f"Recognized Text: {MyText}")  # Show the recognized text
            return MyText.lower()  # Convert to lowercase for easier matching
            
    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
    except Exception as e:
        print(f"An error occurred: {e}")  # General error handling
    
    return None

def execute_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        print("Opening Google...")
        print("What do you want to search for on Google?")
        search_query = record_text()  # Listen for the search query
        if search_query:  # If a search query was recognized
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            print(f"Searching for {search_query} on Google...")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube...")
        print("What do you want to play on YouTube?")
        song_name = record_text()  # Listen for the song name
        if song_name:  # If a song name was recognized
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            print(f"Playing {song_name} on YouTube...")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        print("Opening Instagram...")
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        print("Opening Gmail...")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        print("Opening LinkedIn...")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        print("Opening GitHub...")
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        print("Opening WhatsApp...")
    elif "open spotify" in command:
        subprocess.Popen(['spotify.exe'])
        print("Opening Spotify...")
    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")  # For Windows
        print("Opening camera...")
    elif "open notepad" in command:
        subprocess.Popen(['notepad.exe'])
        print("Opening Notepad...")
    elif "open calculator" in command:
        subprocess.Popen(['calc.exe'])
        print("Opening Calculator...")
    elif "open word" in command:
        subprocess.Popen(['winword.exe'])
        print("Opening Microsoft Word...")
    elif "open excel" in command:
        subprocess.Popen(['excel.exe'])
        print("Opening Microsoft Excel...")
    elif "open powerpoint" in command:
        subprocess.Popen(['powerpnt.exe'])
        print("Opening Microsoft PowerPoint...")
    elif "open paint" in command:
        subprocess.Popen(['mspaint.exe'])
        print("Opening Paint...")
    elif "open browser" in command:
        subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe'])  # Adjust path as needed
        print("Opening Firefox...")
    elif "open edge" in command:
        subprocess.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'])  # Adjust path as needed
        print("Opening Microsoft Edge...")
    elif "open discord" in command:
        subprocess.Popen(['C:\\Users\\YourUsername\\AppData\\Local\\Discord\\Update.exe', '--processStart', 'Discord.exe'])  # Adjust path as needed
        print("Opening Discord...")
    else:
        print("Command not recognized")

while True:
    text = record_text()
    if text:  # Only process if there's recognized text
        execute_command(text)
