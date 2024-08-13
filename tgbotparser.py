import asyncio
import random_parser

from aiogram import Bot, types, Dispatcher, F, html
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = ''



bot = Bot(token=TOKEN)
dp = Dispatcher()

#Обработчик старта с выбором что посмотреть
@dp.message(CommandStart())
async def command_start_handler(message: types.message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Сериалы',
        callback_data = 'Serials')
    )
    builder.add(types.InlineKeyboardButton(
        text='Фильмы',
        callback_data = 'Films')
    )
    await message.answer(
        "Привет! Выбери, что хочешь посмотреть!",
        reply_markup=builder.as_markup()
        )

#Кнопка выбора сериалов
@dp.callback_query(F.data == 'Serials')
async def Serials(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text = 'Ужасы',
        callback_data = 'Horror_serial')
        )
    builder.add(types.InlineKeyboardButton(
        text = 'Фантастика',
        callback_data = 'Fantasy_serial')
        )
    builder.add(types.InlineKeyboardButton(
        text = 'Комедия',
        callback_data = 'Comedy_serial')
    )
    await callback.message.answer('Какой жанр сериала?',
    reply_markup=builder.as_markup()
    )
    await callback.answer()

#Кнопка выбора фильмов
@dp.callback_query(F.data == 'Films')
async def Films(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text = 'Ужасы',
        callback_data = 'Horror_films')
        )
    builder.add(types.InlineKeyboardButton(
        text = 'Фантастика',
        callback_data = 'Fantasy_film')
        )
    builder.add(types.InlineKeyboardButton(
        text = 'Комедия',
        callback_data = 'Comedy_film')
        )
    await callback.message.answer('Какой жанр фильмов?',
    reply_markup=builder.as_markup()
    )
    await callback.answer()


@dp.callback_query(F.data == 'Horror_films')

async def Horror_films(callback: types.CallbackQuery):
    link = random_parser.links_parcer('https://movielib.ru/genre/Ужасы/top/~', 'https://movielib.ru/genre/Ужасы/top/~')
    photo = random_parser.movie_photo(link)
    await callback.message.answer_photo(photo=photo, caption=str(random_parser.film_info(link)))
    # await callback.message.answer(str(random_parser.film_info(link)))


async def main():
    bot = Bot(TOKEN)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
