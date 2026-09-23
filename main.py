import asyncio 
from aiogram import Bot, Dispatcher
from handlers import (
    welcome, role, 
    command, start,
    play_command)
from config import TOKEN
from database.db import create_table_warnings


dp = Dispatcher()
dp.include_router(welcome.router)
dp.include_router(role.router)
dp.include_router(command.router)
dp.include_router(start.router)
dp.include_router(play_command.router)


async def main():
    bot = Bot(token=TOKEN)
    await create_table_warnings()

    print("Start bot")
    await dp.start_polling(bot) 

if __name__ == "__main__":
    asyncio.run(main())