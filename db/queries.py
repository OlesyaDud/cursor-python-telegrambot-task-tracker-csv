"""
Database query functions for task operations.
All functions are async and use aiosqlite.
"""
from datetime import datetime, timezone
from db.database import get_db


def utc_now_iso() -> str:
    """
    Get current UTC time as ISO format string.
    Returns: ISO format datetime string (e.g., "2026-02-20T10:30:45.123456")
    """
    return datetime.now(timezone.utc).isoformat()

async def add_task(text: str, user: str) -> int:
    created_at = utc_now_iso()

    db = await get_db()
    try:
        cursor = await db.execute(
            "INSERT INTO tasks (text, user, created_at) VALUES (?, ?, ?)",
            (text, user, created_at)
        )
        await db.commit()
        return cursor.lastrowid
    finally:
        await db.close()



async def list_tasks() -> list[dict]:
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, text, user, created_at FROM tasks ORDER BY id DESC"
        )
        rows = await cursor.fetchall()

        tasks = []
        for row in rows:
            tasks.append({
                "id": row[0],
                "text": row[1],
                "user": row[2],
                "created_at": row[3]
            })

        return tasks
    finally:
        await db.close()

