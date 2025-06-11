# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx
# pip install openai
# pip install gTTS
# pip install pygame

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1c6aedb91fc544a49951a7a093f539d9"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

opnAIapi = ""


def speak(text):
    tts = gTTS(text)
    tempfile = "temp.mp3"
    tts.save(tempfile)

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(tempfile)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def ai_process(command):
    client = OpenAI(api_key=f"{opnAIapi}")

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please",
            },
            {"role": "user", "content": command},
        ],
    )

    return completion["choices"][1]["message"]["content"]


def process_command(c):
    c = c.lower()

    command_map = {
        "open google": "https://google.com",
        "open facebook": "https://facebook.com",
        "open youtube": "https://youtube.com",
        "open linkedin": "https://linkedin.com",
    }
    for key, link in command_map.items():
        if key in c.lower():
            webbrowser.open(link)
            return False  # Don't exit

    if c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            try:
                link = musicLibrary.music[song]
                webbrowser.open(link)
            except KeyError:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please specify a song to play.")
        return False  # Don't exit

    if "news" in c:
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:  # Limit to 5 headlines
                speak(article["title"])
        else:
            speak("Sorry, I couldn't fetch the news.")
        return False  # Don't exit

    if "exit" in c or "stop" in c:
        speak("Goodbye!")
        exit(0)  # or set a flag in main loop to break
        return True  # Signal to exit

    # If no other command matched, use AI
    output = ai_process(c)
    speak(output)
    return False


if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    while True:
        try:
            # Listen for the wake word "Jarvis"
            # obtain audio from the microphone
            r = sr.Recognizer()

            print("Recognizing...")
            # recognize speech using Google Speech Recognition

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=5)
                word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=4, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    should_exit = process_command(command)
                    if should_exit:
                        break  # clean exit from while loop

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}"
            )
