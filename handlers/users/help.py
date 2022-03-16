from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("отправьте изображение с имеющимся текстом.",
            "Важно! Текст должен быть отчетливо виден, фон за текстом без явных, грубых помех.",
            "Для лучшего качества результата рекомендуется заранее вырезать необходимую область с текстом. \n\n")

    await message.answer("\n".join(text))
