from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State

from keyboards.default import langs

from loader import dp

from text_recognize.text_recognize import recognize


@dp.message_handler(commands='lang')
async def select_lang(message: types.Message):
    await message.answer('выберите язык: ', reply_markup=langs)


    state_lang = State()
    await state_lang.set()


@dp.message_handler(Text(equals=["eng", "rus"]))

async def get_language(message: types.Message,  state: FSMContext):
    await state.update_data(lang=message.text)
    lang = await state.get_data()
    await message.answer(f'Язык успешно изменен на {lang.get("lang")}', reply_markup=types.ReplyKeyboardRemove())


