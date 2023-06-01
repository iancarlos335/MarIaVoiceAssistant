import asyncio
import re

from EdgeGPT import Chatbot, ConversationStyle


async def main():
    while True:
        bot = Chatbot(cookie_path='cookies.json')
        response = await bot.ask(prompt=input("Pergunte pra MarIA uma pergunta... "),
                                 conversation_style=ConversationStyle.creative)
        # Select only bot response from the response dictionary
        for message in response["item"]["messages"]:
            if message["author"] == "bot":
                bot_response = message["text"]
        # Remove citations on response
        bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
        print("Maria's response: ", bot_response)
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
