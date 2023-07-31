import asyncio
import pydub
import pyttsx3
import re
import speech_recognition as sr
import whisper
from EdgeGPT import Chatbot, ConversationStyle
from pydub import playback


async def main():
    bot_response = ""
    bot = Chatbot(cookie_path='cookies.json')
    response = await bot.ask(prompt=input("Ask an question..."), conversation_style=ConversationStyle.creative)
    # Select only the bot response from the response dictionary
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    # Remove [^#^] citations in response
    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
    print("Bot's response:", bot_response)
    await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
