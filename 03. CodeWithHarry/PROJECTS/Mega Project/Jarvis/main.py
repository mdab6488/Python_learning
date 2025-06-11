# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx
# pip install openai
# pip install gTTS
# pip install pygame
# pip install python-dotenv

import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import tempfile
import logging
from typing import Dict, Optional, Tuple
from dotenv import load_dotenv
import threading
import time

# Load environment variables
load_dotenv()

# Configure logging with better formatting and colors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant with configuration and setup."""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.running = True

        # Get API Keys from environment variables
        self.newsapi_key = os.getenv("NEWS_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Validate API Keys
        if not self.newsapi_key or not self.openai_api_key:
            logger.error("Missing API key. Please set NEWS_API_KEY AND OPENAI_API_KEY in your .env file")
            raise ValueError("Missing required API keys")

        # Initialize OpenAI Client
        self.openai_client = OpenAI(api_key=self.openai_api_key)

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Configure speech recognition
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

        # Command mappings
        self.website_commands = {
            "open google": "https://google.com",
            "open facebook": "https://facebook.com",
            "open youtube": "https://youtube.com",
            "open linkedin": "https://linkedin.com",
        }

        # Music Library - you'll need to create this or load from file
        self.music_library = self._load_music_library()

        print("✅ Voice Assistant initialized successfully!\n")

    def _load_music_library(self) -> Dict[str, str]:
        """Load music library from file or return default."""
        try:
            # Try to import existing musicLibrary module
            import musicLibrary
            return musicLibrary.music
        except ImportError:
            logger.warning("musicLibrary module not found, using default music library")
            return {
                "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
                "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
                "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ"
            }

    def speak(self, text: str) -> None:
        """Main speak method - uses only gTTS for consistency."""
        if not text:
            return

        print(f"🗣️ Speaking: {text}\n")
        self._speak_with_gtts(text)

    def _speak_with_gtts(self, text: str) -> None:
        """Use Google Text-to-Speech for consistent voice."""
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang='en', slow=False)

            # Use temporary file that gets cleaned up automatically
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                temp_filename = temp_file.name
                tts.save(temp_filename)

            # Stop any currently playing audio
            pygame.mixer.music.stop()

            # Load and play the audio file
            pygame.mixer.music.load(temp_filename)
            pygame.mixer.music.play()

            # Wait for playback to complete
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Clean up temporary file
            try:
                os.unlink(temp_filename)
            except OSError:
                pass  # File might already be deleted

        except Exception as e:
            logger.error(f"Error with gTTS: {e}")
            print(f"❌ Speech synthesis failed: {e}\n")
            # Fallback to simple print if TTS fails
            print(f"💬 Assistant would say: {text}\n")

    def listen_for_wake_word(self, wake_word: str = "jarvis", timeout: int = 1) -> bool:
        """Listen for the wake word."""
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                print("👂 Listening for wake word...\n")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=3)

                word = self.recognizer.recognize_google(audio).lower()
                print(f"🎤 Heard: {word}\n")

                return wake_word.lower() in word

        except sr.WaitTimeoutError:
            return False
        except sr.UnknownValueError:
            return False
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {e}")
            return False

    def listen_for_command(self, timeout: int = 5) -> Optional[str]:
        """Listen for a command after wake word is detected."""
        try:
            with sr.Microphone() as source:
                print("🟢 Jarvis Active... Listening for command...\n")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=8)

                command = self.recognizer.recognize_google(audio)
                print(f"📝 Command received: {command}\n")
                return command
        except sr.WaitTimeoutError:
            self.speak("I didn't hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            self.speak("I couldn't understand that. Please try again.")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {e}")
            self.speak("Sorry, I'm having trouble with speech recognition.")
            return None

    def open_website(self, command: str) -> bool:
        """Handle website opening commands."""
        for trigger, url in self.website_commands.items():
            if trigger in command.lower():
                print(f"🌐 Opening {url}\n")
                webbrowser.open(url)
                self.speak(f"Opening {trigger.replace('open ', '')}")
                return True
        return False

    def play_music(self, command: str) -> bool:
        """Handle music playing commands."""
        if not command.lower().startswith("play"):
            return False

        parts = command.split(" ", 1)
        if len(parts) < 2:
            self.speak("Please specify a song to play")
            return True

        song_name = parts[1].lower()

        # Try exact match first
        if song_name in self.music_library:
            url = self.music_library[song_name]
            webbrowser.open(url)
            self.speak(f"Playing {song_name}")
            return True

        # Try partial match
        for song, url in self.music_library.items():
            if song_name in song.lower():
                webbrowser.open(url)
                self.speak(f"Playing {song}")
                return True

        self.speak(f"Sorry, I couldn't find {song_name} in your music library")
        return True

    def get_news(self) -> bool:
        """Fetch and read news headlines."""
        try:
            print("📰 Fetching news...\n")
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.newsapi_key}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            articles = data.get("articles", [])

            if not articles:
                self.speak("No news articles found.")
                return True

            self.speak("Here are the top news headlines:")

            for i, article in enumerate(articles[:5], 1):
                title = article.get("title", "")
                if title:
                    self.speak(f"Headline {i}: {title}")
                    time.sleep(1)  # Brief pause between headlines
            return True

        except requests.RequestException as e:
            logger.error(f"Error fetching news: {e}")
            self.speak("Sorry, I couldn't fetch the news right now.")
            return True
        except Exception as e:
            logger.error(f"Unexpected error in get_news: {e}")
            self.speak("Sorry, there was an error getting the news.")
            return True

    def ai_process(self, command: str) -> str:
        """Process command using OpenAI API."""
        try:
            print("🤖 Processing with AI...\n")
            completion = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a virtual assistant named Jarvis. You are helpful, concise, and friendly. Keep responses under 50 words unless more detail is specifically requested."
                    },
                    {"role": "user", "content": command}
                ],
                max_tokens=150,
                temperature=0.7
            )

            return completion.choices[0].message.content

        except Exception as e:
            logger.error(f"Error with OpenAI API: {e}")
            return "Sorry, I'm having trouble processing that request right now."

    def process_command(self, command: str) -> bool:
        """Process voice command and return whether to continue running."""
        if not command:
            return True

        command_lower = command.lower()

        # Exit Commands
        if any(word in command_lower for word in ["exit", "stop", "quit", "goodbye"]):
            self.speak("Goodbye! Have a great day!")
            return False

        # Website commands
        if self.open_website(command):
            return True

        # Music Commands
        if self.play_music(command):
            return True

        # News commands
        if "news" in command_lower:
            self.get_news()
            return True

        # Time command
        if "time" in command_lower:
            current_time = time.strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            return True

        # Date command
        if "date" in command_lower:
            current_date = time.strftime("%A, %B %d, %Y")
            self.speak(f"Today's date is {current_date}")
            return True

        # Default to AI processing
        response = self.ai_process(command)
        self.speak(response)
        return True

    def run(self):
        """Main loop for the voice assistant."""
        self.speak("Initializing Jarvis... Ready to assist you!")

        while self.running:
            try:
                # Listen for wake word
                if self.listen_for_wake_word():
                    self.speak("Yes, how can I help?")

                    # Listen for command
                    command = self.listen_for_command()

                    if command:
                        should_continue = self.process_command(command)
                        if not should_continue:
                            self.running = False
                            break

            except KeyboardInterrupt:
                print("\n⏹️ Keyboard interrupt received")
                self.speak("Shutting down...")
                self.running = False
                break
            except Exception as e:
                logger.error(f"Unexpected error in main loop: {e}")
                continue

        print("👋 Jarvis has been shut down.\n")


def main():
    """Main function to run the voice assistant."""
    try:
        print("🚀 Starting Jarvis Voice Assistant...\n")
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as e:
        logger.error(f"Failed to start voice assistant: {e}")
        print(f"❌ Error: {e} \n")


if __name__ == "__main__":
    main()