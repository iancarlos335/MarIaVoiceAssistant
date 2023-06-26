import asyncio
import re

import pydub
import pyttsx3
import speech_recognition as sr
import whisper
from EdgeGPT import Chatbot, ConversationStyle
from pydub import playback

# Create a recognizer object and wake word variables
recognizer = sr.Recognizer()
MARIA_WAKE_WORD = "maria"


def get_wake_word(phrase):
    if MARIA_WAKE_WORD in phrase.lower():
        return MARIA_WAKE_WORD
    else:
        return None


def synthesize_speech(text, output_filename):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')
    engine.save_to_file(text, output_filename)
    engine.runAndWait()


def play_audio(file):
    sound = pydub.AudioSegment.from_file(file, format="wav")
    playback.play(sound)


async def main():
    while True:

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print(f"\n\nDiga MARIA quando precisar me chamar. ;)")
            while True:
                audio = recognizer.listen(source)
                try:
                    with open("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                        f.close()
                    # Use the preloaded tiny_model
                    model = whisper.load_model("base")

                    audio_1 = whisper.load_audio('audio.wav')
                    result = model.transcribe("audio.wav")
                    phrase = result["text"]
                    print(f"\n\n\nVocê disse: {phrase}")

                    wake_word = get_wake_word(phrase)
                    if wake_word is not None:
                        break
                    else:
                        print("Não é a palavra chave. Tente novamente.")
                except Exception as e:
                    print("Error transcribing audio: {0}".format(e))
                    continue

            print("Diga algo... ")
            synthesize_speech('Como posso te ajudar?', 'response.mp3')
            play_audio('response.mp3')
            audio = recognizer.listen(source)

            try:
                with open("audio_prompt.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                model = whisper.load_model("base")
                result = model.transcribe("audio_prompt.wav")
                user_input = result["text"]
                print(f"\n\n\nVocê disse: {user_input}")
            except Exception as e:
                print("Error transcribing audio: {0}".format(e))
                continue

            # bot = Chatbot(cookie_path='cookies.json')
            # response = await bot.ask(prompt=user_input, conversation_style=ConversationStyle.precise)
            #
            # for message in response["item"]["messages"]:
            #     if message["author"] == "bot":
            #         bot_response = message["text"]
            #
            # bot_response = re.sub(r'\[\^\d+\^\]', '', bot_response)

            bot = Chatbot(cookie_path='cookies.json')
            response = await bot.ask(prompt=user_input, conversation_style=ConversationStyle.creative)
            # Select only the bot response from the response dictionary
            for message in response["item"]["messages"]:
                if message["author"] == "bot":
                    bot_response = message["text"]
            # Remove [^#^] citations in response
            bot_response = re.sub(r'\[\^\d+\^\]', '', bot_response)

        print("\nResposta da MarIA:", bot_response)
        synthesize_speech(bot_response, 'response.mp3')
        play_audio('response.mp3')
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
