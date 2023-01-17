from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token
from screenshot import main
import asyncio

bot = Bot(token)
dp = Dispatcher(bot)

def get_name(message: types.Message) -> str:
    if message.from_user.username:
        name: str = message.from_user.username
    else:
        name: str = message.from_user.first_name + ' ' + message.from_user.last_name if message.from_user.last_name \
            else message.from_user.first_name
    return name

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    name = get_name(message)
    await bot.send_message(message.chat.id, text=f"Привет, {name}!\n"
                                        "Я @BLRExchangeBot!\n"
                                        "Высылаю актуальную информацию о торгах на валютном рынке!\n"
                                        "Данные приведены с https://banki24.by \n")


@dp.message_handler(commands=["currency"])
async def currency(message: types.Message):
    print(message.from_user)
    msg1 = await bot.send_message(message.chat.id, text="Обработка запроса...")
    main()
    msg = await bot.send_photo(message.chat.id, types.InputFile('cut.png'))
    await bot.delete_message(message.chat.id, msg1.message_id)
    await asyncio.sleep(60)
    await bot.delete_message(message.chat.id, msg.message_id)

if __name__ == "__main__":
    executor.start_polling(dp)
    