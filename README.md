# Team Tasks Bot

A Telegram bot for team collaboration that allows adding tasks to a shared list.

## Features

- `/start` - Welcome message with available commands
- `/add <task text>` - Add a new task to the shared list
- `/list` - View all tasks
- `/list_csv` - Export all tasks as a CSV file

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a Telegram Bot Token:**
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` and follow the instructions
   - Copy your bot token

3. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Edit `.env` and paste your bot token:
     ```
     BOT_TOKEN=your_bot_token_here
     ```

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd team_tasks_bot
   ```

2. **Run the bot:**
   ```bash
   python main.py
   ```

3. **Test the bot:**
   - Open Telegram and find your bot
   - Send `/start` to begin
   - Try adding tasks with `/add Buy milk`
   - View tasks with `/list`
   - Export with `/list_csv`

## Project Structure

```
team_tasks_bot/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── bot/
│   ├── handlers/          # Command handlers
│   │   ├── start.py       # /start command
│   │   └── tasks.py       # /add, /list, /list_csv
│   └── keyboards/         # Keyboard layouts
│       └── common.py
├── db/
│   ├── database.py        # DB initialization
│   └── queries.py         # Database queries
└── utils/
    └── csv_export.py      # CSV export utility
```

## Database

The bot uses SQLite (`tasks.db`) with the following schema:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user TEXT NOT NULL,
    created_at TEXT NOT NULL
)
```

The database file (`tasks.db`) will be created automatically on first run.
