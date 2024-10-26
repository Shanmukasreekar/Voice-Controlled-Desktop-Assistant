Voice-Controlled Desktop Assistant
Overview
The Voice-Controlled Desktop Assistant is a Python-based project that uses voice commands to automate tasks on your computer. With this assistant, you can open applications, browse websites, and even play specific songs on platforms like YouTube and Spotify, all through spoken commands. This assistant leverages Natural Language Processing (NLP) for speech recognition to interpret and execute commands.

Features
Open Applications: Launch desktop applications like Chrome, Notepad, Spotify, Camera, and others using voice commands.
Navigate Websites: Open websites such as Google, YouTube, Instagram, and LinkedIn directly through spoken requests.
Play Media: On YouTube or Spotify, specify a song to play by saying “Play [song name]” after opening the platform.
Command Updates: The program captures and processes voice inputs every three seconds, ensuring a balance between responsiveness and performance.
Technology Stack
Programming Language: Python
Libraries:
speech_recognition for capturing and converting voice commands to text.
webbrowser and subprocess for opening websites and applications.
spotipy for interacting with Spotify’s API and playing specific songs.
Requirements
Python 3.6 or higher
Install required libraries using pip:         pip install speechrecognition spotipy pyttsx3
Project Structure
speech.py: Main script that handles speech recognition, command execution, and platform-specific functions.
README.md: Documentation and instructions for using the assistant.
Usage
Run the script:        python speech.py
Give voice commands as per the following examples:
Opening Applications: "Open Google," "Open Spotify," "Open Calculator."
Navigating Websites: "Open LinkedIn," "Open Gmail," "Open YouTube."
Playing Songs on YouTube: "Play song name on YouTube" after YouTube is opened.
Playing Songs on Spotify: "Play song name" after Spotify is opened.
Example Commands
General Commands:
"Open Chrome"
"Open YouTube"
"Open Gmail"
YouTube Commands:
"Play Rolling in the Deep on YouTube" (after YouTube is opened)