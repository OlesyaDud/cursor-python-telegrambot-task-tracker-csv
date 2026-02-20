import aiosqlite

DB_PATH = "tasks.db"


async def init_db() -> None:
    """Create table if it doesn't exist."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                user TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        await db.commit()


async def get_db() -> aiosqlite.Connection:
    """
    Return an OPEN connection.
    IMPORTANT: Do NOT use 'async with' here, because that would close it immediately.
    """
    return await aiosqlite.connect(DB_PATH)

