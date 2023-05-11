import asyncio
from EdgeGPT import Chatbot, ConversationStyle

async def main():
    bot = await Chatbot.create(cookie_path='cookies.json')
    print(await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative, wss_link="wss://sydney.bing.com/sydney/ChatHub"))
    await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
