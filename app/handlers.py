from pyexpat.errors import messages

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackQueryFilter
from aiogram.types import Message, callback_query, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.callback_answer import CallbackAnswer
from random import randint, sample
from time import sleep

import app.keyboards as kb
from app.Kazino import kazzzino
from app.db_for_victorina import easy_list, hard_list, very_very_hard_list

router = Router()

class Reg(StatesGroup):
    answer = State()
    question_key = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f'Привет, перед Вами телеграмм бот со следующими командами. Выбери одну из них:',
                        reply_markup=kb.main)

@router.message(F.text == 'Вернуться назад')
async def cmd_start(message: Message):
    await message.reply(
            f'С возвращением, Выбери следующие команды',
            reply_markup=kb.main)

@router.message(F.text == 'Кто автор телеграмм бота?')
async def who_I_am(message: Message):
    await message.reply(text=f'Автор телеграмм бота - Руслан Сайфуллин')
    await message.answer_photo(photo='AgACAgIAAxkBAAIB8WcahjNdRkF8RofHxxLGMZg5a0MYAAIr5TEb85DZSB8mzyu--fjLAQADAgADeAADNgQ')
    sleep(2)
    await message.answer_photo('AgACAgIAAxkBAAICDGcaiOjjcnDCXEo7VKn5myEagXnLAAJI5TEb85DZSI4vMY5FxN3gAQADAgADbQADNgQ')

@router.message(F.text == 'Казино')
async def kazik(message: Message):
    zakkk = str()
    sleep(1)
    await message.answer(kazzzino(zakkk))

@router.message(F.text == 'Погода')
async def choose_weather(message: Message):
    await message.answer(f'Выбери город, в котором хочешь узнать погоду',
                         reply_markup=kb.weather)

@router.message(F.text == 'Викторина')
async def victorinia(message: Message):
    await message.answer(f'Выбери сложность вопроса или вернитесь назад',
                         reply_markup=kb.main_victorina)

@router.message(F.text == 'Легкий вопрос')
async def easy_quest(message: Message, state: FSMContext):
    await message.answer(f'Ответьте на достаточно простой вопрос. '
                         f'Если не справитесь с ним, то можете попробовать еще раз:')
    sleep(2)
    a = randint(0, 9)
    await state.update_data(question_key=easy_list[a][1])
    await state.set_state((Reg.answer))
    await message.answer(easy_list[a][0])

@router.message(F.text == 'Сложный вопрос')
async def easy_quest(message: Message, state: FSMContext):
    await message.answer(f'Ответьте на сложный вопрос. '
                         f'Если не справитесь с ним, то можете попробовать еще раз:')
    sleep(2)
    a = randint(0, 5)
    await state.update_data(question_key=hard_list[a][1])
    await state.set_state((Reg.answer))
    await message.answer(hard_list[a][0])

@router.message(F.text == 'Вопрос со звездочкой')
async def easy_quest(message: Message, state: FSMContext):
    await message.answer(f'Ответьте на очень трудный вопрос. '
                         f'Если не справитесь с ним, то обязательно попробуйте еще раз:')
    sleep(2)
    a = randint(0, 5)
    await state.update_data(question_key=very_very_hard_list[a][1])
    await state.set_state((Reg.answer))
    await message.answer(very_very_hard_list[a][0])

@router.message(F.text == 'Угадай число')
async def chislo(message: Message):
    await message.answer(f'Вам предлагается угадать число из диапазона 1-5. '
                         f'Попробуйте угадать, если ответите неверно, то можете попытаться еще раз',
                         reply_markup=kb.main_chislo)

@router.message(F.text == 'Начать')
async def easy_number(message: Message, state: FSMContext):
    await message.answer(f'Угадайте число!')
    sleep(1)
    a = str(randint(1, 5))
    await state.update_data(question_key=a)
    await state.set_state((Reg.answer))

@router.message(Reg.answer)
async def good_cool(message: Message,  state: FSMContext):
    await state.update_data(answer=message.text)
    data = await state.get_data()
    if data['answer'].lower() == data['question_key'].lower():
        await message.answer(f'Поздравляем! В самую точку)!!!')
        await state.clear()
    else:
        await message.answer(f'lol, твой ответ неправильный. Попробуй еще раз')