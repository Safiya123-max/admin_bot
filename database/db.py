import asyncpg
from config import HOST, PORT, NAME, USER, PASSWORD


def get_db_connection():
    return asyncpg.connect(
        host=HOST,
        port=PORT,
        database=NAME,
        user=USER,
        password=PASSWORD
    )


async def create_table_warnings():
    try:
        conn = await get_db_connection()

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS warnings (
        warning_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        user_id BIGINT NOT NULL,
        moderator_id BIGINT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        reason TEXT
        )
        """)

        await conn.close()

    except Exception as e:
        print(f"ERROR failed to create table 'warnings': {e}")


async def get_warning(chat_id, user_id, moderator_id, reason):
    try:
        conn = await get_db_connection()
        await conn.execute(
            "INSERT INTO warnings (chat_id, user_id, moderator_id, reason) VALUES ($1, $2, $3, $4)",
            chat_id, user_id, moderator_id, reason
        )
        await conn.close()

    except Exception as e:
        print(f"ERROR failed to add waring to table 'warnings': {e}")  


async def get_warnings_count(user_id: int):
    try:
        conn = await get_db_connection()

        count = await conn.fetchval(
            """
            SELECT COUNT(*)
            FROM warnings
            WHERE user_id = $1
            """,
            user_id
        )

        await conn.close()
        return count
    
    except Exception as e:
        print(f"ERROR failed to count warnings to table 'warnings': {e}")   


async def get_warnings_for_user(user_id: int, chat_id: int):
    try:
        conn = await get_db_connection()

        rows = await conn.fetch("""
            SELECT * FROM warnings
            WHERE user_id = $1
            AND chat_id = $2
            """, 
        user_id, chat_id)

        await conn.close()
        return rows 
    except Exception as e:
        print(f"ERROR failed to get warning to table 'warnings': {e}")  


async def delete_warning(warning_id: int) -> bool:
    try:
        conn = await get_db_connection()
        
        deleted = await conn.fetchval("""
        DELETE FROM warnings 
        WHERE warning_id = $1
        """, warning_id)
        return deleted is not None

    except Exception as e:
        print(f"ERROR failed to delete waring to table 'warnings': {e}") 
        return False  

    finally:
        await conn.close()              


