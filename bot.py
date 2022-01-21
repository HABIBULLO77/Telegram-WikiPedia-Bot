import logging
import wikipedia
 
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5020218862:AAGFH0L1SHhZyC820T79aErau3g49V0d1lI'
wikipedia.set_lang('en')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi. Welcome to Wikipedia Bot ")



@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("There is no any data about this topic")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)