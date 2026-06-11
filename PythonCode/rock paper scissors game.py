from google import genai
import pyttsx3

# Gemini API Key
client = genai.Client(api_key="YOUR_API_KEY")

engine = pyttsx3.init()

def speak(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello Shweta. I am Alexa powered by Gemini.")

while True:
    user = input("You: ")

    if user.lower() in ["bye", "exit", "stop"]:
        speak("Goodbye")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user
        )

        answer = response.text
        speak(answer)

    except Exception as e:
        print("Error:", e)
        
