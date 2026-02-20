"""
Task management handlers: add, list, and export tasks.
"""
from datetime import datetime
from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command

from db.queries import add_task, list_tasks
from utils.csv_export import tasks_to_csv_bytes

router = Router()


@router.message(Command("add"))
async def cmd_add(message: Message):
    """
    Handle /add command.
    Adds a new task to the database.
    Usage: /add <task text>
    """
    # Extract task text from command
    command_parts = message.text.split(maxsplit=1)
    
    if len(command_parts) < 2:
        # No task text provided
        await message.answer(
            "❌ Please provide a task description.\n\n"
            "Usage: /add &lt;task text&gt;\n"
            "Example: /add Buy milk"
        )
        return
    
    task_text = command_parts[1].strip()
    
    if not task_text:
        await message.answer(
            "❌ Task text cannot be empty.\n\n"
            "Usage: /add &lt;task text&gt;\n"
            "Example: /add Buy milk"
        )
        return
    
    # Get user identifier (username if available, otherwise user ID)
    user = message.from_user.username
    if not user:
        user = str(message.from_user.id)
    
    try:
        # Add task to database
        task_id = await add_task(task_text, user)
        
        # Send confirmation
        await message.answer(
            f"✅ Task added successfully!\n\n"
            f"<b>Task ID:</b> {task_id}\n"
            f"<b>Task:</b> {task_text}\n"
            f"<b>Added by:</b> {user}"
        )
    except Exception as e:
        # Handle errors
        await message.answer(
            f"❌ Error adding task: {str(e)}\n"
            "Please try again later."
        )


@router.message(Command("list"))
async def cmd_list(message: Message):
    """
    Handle /list command.
    Shows all tasks ordered by ID (newest first).
    """
    try:
        # Fetch all tasks from database
        tasks = await list_tasks()
        
        if not tasks:
            await message.answer("📝 No tasks yet. Add one with /add!")
            return
        
        # Format tasks for display
        task_lines = []
        for task in tasks:
            task_id = task["id"]
            task_text = task["text"]
            task_user = task["user"]
            created_at = task["created_at"]
            
            # Parse ISO datetime and format as date only
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                formatted_date = dt.strftime("%Y-%m-%d")
            except (ValueError, AttributeError):
                # Fallback to original if parsing fails
                formatted_date = created_at.split('T')[0] if 'T' in created_at else created_at
            
            task_lines.append(
                f"#{task_id} — {task_text}\n"
                f"   👤 by {task_user} • 📅 {formatted_date}"
            )
        
        # Send formatted list
        response = "📋 <b>All Tasks:</b>\n\n" + "\n\n".join(task_lines)
        
        # Telegram message limit is 4096 characters, split if needed
        if len(response) > 4000:
            # Send in chunks
            chunk_size = 4000
            chunks = [response[i:i+chunk_size] for i in range(0, len(response), chunk_size)]
            for chunk in chunks:
                await message.answer(chunk)
        else:
            await message.answer(response)
            
    except Exception as e:
        await message.answer(
            f"❌ Error fetching tasks: {str(e)}\n"
            "Please try again later."
        )


@router.message(Command("list_csv"))
async def cmd_list_csv(message: Message):
    """
    Handle /list_csv command.
    Exports all tasks as CSV file and sends it as a Telegram document.
    """
    try:
        # Fetch all tasks from database
        tasks = await list_tasks()
        
        if not tasks:
            await message.answer("📝 No tasks to export. Add one with /add!")
            return
        
        # Convert tasks to CSV bytes
        csv_bytes = tasks_to_csv_bytes(tasks)
        
        # Create file object for Telegram
        csv_file = BufferedInputFile(
            file=csv_bytes,
            filename="tasks.csv"
        )
        
        # Send file as document
        await message.answer_document(
            document=csv_file,
            caption=f"📊 Exported {len(tasks)} task(s)"
        )
        
    except Exception as e:
        await message.answer(
            f"❌ Error exporting tasks: {str(e)}\n"
            "Please try again later."
        )
