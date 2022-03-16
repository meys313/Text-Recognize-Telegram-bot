from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("text_recognize", "Текст с изображения"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )
