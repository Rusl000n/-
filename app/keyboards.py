
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Погода'), KeyboardButton(text='Казино')],
    [KeyboardButton(text='Викторина'), KeyboardButton(text='Угадай число')],
    [KeyboardButton(text='Кто автор телеграмм бота?')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню')

weather = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Москва', url='https://yandex.ru/pogoda/moscow')],
    [InlineKeyboardButton(text='Санкт-Петербург', url='https://yandex.ru/pogoda/saint-petersburg')],
     [InlineKeyboardButton(text='Великий-Новгород', url='https://yandex.ru/pogoda/veliky-novgorod')],
    [InlineKeyboardButton(text='Екатеринбург', url='https://yandex.ru/pogoda/yekaterinburg')],
    [InlineKeyboardButton(text='Краснодар', url='https://yandex.ru/pogoda/krasnodar')]
])

main_victorina = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Легкий вопрос'), KeyboardButton(text='Сложный вопрос')],
    [KeyboardButton(text='Вопрос со звездочкой'), KeyboardButton(text='Вернуться назад')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню')

main_chislo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать'), KeyboardButton(text='Вернуться назад')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню')