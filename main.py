import asyncio
import re
import pydub
import pyttsx3
import speech_recognition as sr
import whisper
from EdgeGPT import Chatbot, ConversationStyle
from pydub import playback

recognizer = sr.Recognizer()
BING_WAKE_WORD = "maria"


def get_wake_word(phrase):
    if BING_WAKE_WORD in phrase.lower():
        return BING_WAKE_WORD
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
            print(f"Esperando para contruir palavras, diga 'Olá Maria'...")
            while True:
                audio = recognizer.listen(source)
                try:
                    with open("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                    # Use the preloaded tiny_model
                    model = whisper.load_model("tiny")
                    result = model.transcribe("audio.wav")
                    phrase = result["text"]
                    print(f"Você disse: {phrase}")

                    wake_word = get_wake_word(phrase)
                    if wake_word is not None:
                        break
                    else:
                        print("Não é uma frase. Tente novamente.")
                except Exception as e:
                    print("Erro transcrevendo o audio: {0}".format(e))
                    continue

            print("Diga algo...")
            synthesize_speech('Como eu posso ajudar?', 'response.mp3')
            play_audio('response.mp3')
            audio = recognizer.listen(source)

            try:
                with open("audio_prompt.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                model = whisper.load_model("base")
                result = model.transcribe("audio_prompt.wav")
                user_input = result["text"]
                print(f"Você disse: {user_input}")
            except Exception as e:
                print("Erro transcrevendo o audio: {0}".format(e))
                continue

            bot = Chatbot(cookie_path='cookies.json')
            response = await bot.ask(prompt=user_input,
                                     conversation_style=ConversationStyle.precise)
            # Select only bot response from the response dictionary
            for message in response["item"]["messages"]:
                if message["author"] == "bot":
                    bot_response = message["text"]
            # Remove citations on response
            bot_response = re.sub('\[\^\d+\^\]', '', bot_response)

        print("Bot's response", bot_response)
        synthesize_speech(bot_response, 'response.mp3')
        play_audio('response.mp3')
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
