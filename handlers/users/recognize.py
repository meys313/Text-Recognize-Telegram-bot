import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from text_recognize.text_recognize import recognize
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands="text_recognize")
async def text_recognize(message: types.Message):
    await message.answer("отправьте изображение с имеющимся текстом.\n\n"
                         "Важно! Текст должен быть отчетливо виден, фон за текстом без явных, грубых помех. \n\n"
                         "Заранее выберите соответствующий язык - /lang\n\n"
                         "Для лучшего качества результата рекомендуется заранее вырезать необходимую область с текстом.")

    @dp.message_handler(content_types=types.ContentTypes.PHOTO)
    async def succes(message: types.Message, state: FSMContext):
        await message.answer("Фото принято на обработку, ждите...")
        await message.photo[-1].download('image.jpg')
        try:
            get_states = await state.get_data()
            lang = get_states.get('lang', 'rus')
            await message.answer(recognize(lang).lower())

        except Exception as ex:
            if ex.args[0] == 'Message must be non-empty':
                await message.answer('Не удалось распознать текст.\n'
                                     'Попробуйте снова или отправьте другое изображение.\n\n'
                                     '/help - Получить справку')

    @dp.message_handler(state=None)
    async def bot_start(message: types.Message):
        await message.answer("Вы отправили не изображение. Пожалуйста, отправьте изображение с текстом.\n"
                             "Список команд:\n"
                             "/text_recognize - получить текст с изображения\n"
                             "/help - справка")
