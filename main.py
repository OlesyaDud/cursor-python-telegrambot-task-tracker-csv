"""
Main entry point for the Telegram team tasks bot.
Starts the bot polling loop.
"""
import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import start, tasks
from db.database import init_db


async def main():
    """Initialize bot and start polling."""
    # Load environment variables
    load_dotenv()
    
    # Get bot token from environment
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN not found in .env file")
    
    # Initialize database
    await init_db()
    
    # Create bot and dispatcher
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    # Include routers
    dp.include_router(start.router)
    dp.include_router(tasks.router)
    
    # Start polling
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
