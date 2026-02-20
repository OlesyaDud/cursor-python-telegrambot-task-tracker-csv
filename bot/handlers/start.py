"""
Start command handler.
Greets users and shows available commands.
"""
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.common import main_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """
    Handle /start command.
    Greets the user and shows available commands with examples.
    """
    welcome_text = (
        "👋 <b>Welcome to Team Tasks Bot!</b>\n\n"
        "This bot helps your team manage shared tasks.\n\n"
        "<b>Available commands:</b>\n"
        "• /add &lt;task text&gt; - Add a new task\n"
        "  Example: /add Buy milk\n\n"
        "• /list - Show all tasks\n\n"
        "• /list_csv - Export all tasks as CSV file\n\n"
        "Use the keyboard below or type commands directly!"
    )
    
    # Send welcome message with keyboard
    await message.answer(
        welcome_text,
        reply_markup=main_keyboard()
    )
