import asyncio, json
import re

from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle


async def main():
    bot = Chatbot(cookies='cookies.json')  # Passing cookies is "optional", as explained above
    bot_response = ""
    response = await bot.ask(prompt=input("Hello world"), conversation_style=ConversationStyle.creative)

    for message in response["item"]["message"]:
        if message["author"] == "bot":
            bot_response = message["text"]

    print("Responsta da Ia:", bot_response)  # Returns
    await bot.close()
    """
{
    "text": str,
    "author": str,
    "sources": list[dict],
    "sources_text": str,
    "suggestions": list[str],
    "messages_left": int
}
    """


if __name__ == "__main__":
    asyncio.run(main())
