import asyncio
import logging
import sys
from os import getenv
from datetime import datetime
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from background import keep_alive

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        log = open('log.txt', 'a')
        log.write(message.from_user.id + " <> " + message.from_user.full_name)
        await message.reply("Я просто болванка! " + str(datetime.now()))
    except TypeError:
        with open('errors.log', 'a') as f:
            print(f"Ошибка! {str(datetime.now())}")
            f.write(f"Ошибка! {str(datetime.now())}")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

keep_alive()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())