from config import token
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
import logging, asyncio

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:types.Message):
    keybord_main = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Новости')],
            [types.KeyboardButton(text='Курсы валют')],
            [types.KeyboardButton(text='Контактная информация')],
            [types.KeyboardButton(text='Помощь')],
            [types.KeyboardButton(text='О нас')],
            [types.KeyboardButton(text='Меню')],
            [types.KeyboardButton(text='FAQ')],
        ],
        resize_keyboard=True)
    await message.reply("Вас приветсвует Бот в котором самые актуальные новости про экономику и валюту Кыргызстана", reply_markup=keybord_main)
    # await message.answer("Здравствуйте!")

@dp.message(lambda message: message.text in ['Новости', 'Курсы валют', 'Контактная информация', 'FAQ', 'Помощь', 'О нас', 'Меню'])
async def info(message: types.Message):
    if message.text == 'Новости':
        await message.answer("Кыргызстан обладает потенциалом в 4 тысячи тонн золота")
    elif message.text == 'Курсы валют':
        await message.answer("Доллар 86.40сом \nЕвро 90.80сом \nРубль 0.86сом")
    elif message.text == 'Контактная информация':
        await message.answer("Наша почта: news.kg@email.com. \nТелефон: +996123456789.")
    elif message.text == 'FAQ':
        await message.answer("Часто задаваемые вопросы: \nКак часто обновляется курс валют? Ответ: Каждый час \nКак часто меняются новости? Ответ: Как только находим интересную новость :)")
    elif message.text == 'Помощь':
        await message.answer("Задайте ваш вопрос и мы ответим в скором времени")
    elif message.text == 'О нас':
        await message.answer("Мы проект News KG, в котором вы найдете самые актульные новости про экономику Кыргызстана!")
    elif message.text == 'Меню':
        await message.answer("Вы в главном меню")
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())