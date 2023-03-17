from vars_ex import bot
from aiogram import types, Dispatcher

async def chatting_only_with_keyboard(message: types.Message):
    await bot.send_message(message.from_user.id, 'Общение с ботом только при помощи клавиатуры')
    
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(chatting_only_with_keyboard)