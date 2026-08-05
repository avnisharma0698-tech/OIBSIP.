import asyncio
import edge_tts
import webbrowser
import datetime

VOICE = "en-IN-NeerjaNeural"

async def speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

    try:
        import os
        os.startfile("voice.mp3")   # Windows
    except:
        pass


print("========== AI Voice Assistant ==========")
print("Type 'exit' to close.\n")

while True:

    command = input("You : ").lower()

    if command == "hello":
        print("Assistant : Hello Avni! How are you?")
        asyncio.run(speak("Hello Avni! How are you?"))

    elif command == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        print("Assistant :", now)
        asyncio.run(speak(f"The time is {now}"))

    elif command == "google":
        webbrowser.open("https://www.google.com")
        asyncio.run(speak("Opening Google"))

    elif command == "youtube":
        webbrowser.open("https://www.youtube.com")
        asyncio.run(speak("Opening YouTube"))

    elif command == "github":
        webbrowser.open("https://github.com")
        asyncio.run(speak("Opening GitHub"))

    elif command == "exit":
        asyncio.run(speak("Goodbye. Have a nice day."))
        break

    else:
        print("Assistant : Sorry, I don't know that command.")
        asyncio.run(speak("Sorry, I don't know that command."))