"""
Common keyboard layouts for the bot.
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard() -> ReplyKeyboardMarkup:
    """
    Create main reply keyboard with common commands.
    Returns a keyboard with buttons for /list, /list_csv, and an example /add.
    """
    builder = ReplyKeyboardBuilder()
    
    # Add buttons
    builder.add(KeyboardButton(text="/list"))
    builder.add(KeyboardButton(text="/list_csv"))
    builder.row(KeyboardButton(text="/add Buy milk"))
    
    # Configure keyboard
    return builder.as_markup(resize_keyboard=True)
