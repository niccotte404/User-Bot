from vars_ex import bot
from aiogram import types, Dispatcher
from keyboards import client_kb, admin_kb
from database import userbot_database

states = ("help_menu", "book_menu")
state = None


async def answer_for_start_command(message: types.Message):
    await userbot_database.add_user(message)
    await bot.send_message(message.from_user.id, "Добро пожаловать в UserBot. Чего желаете?", reply_markup=client_kb.client_main_menu())



# Обработчик меню "Помощь"

async def load_help_menu(message: types.Message):
    global state
    state = states[0]
    await bot.send_message(message.from_user.id, "Что вы хотите узнать?", reply_markup=client_kb.client_help_menu())

async def contacts(message):
    if state == states[0]:
        await bot.send_message(message.from_user.id, "Вот наши контакты")

async def back(message: types.Message):
    global state
    if state == states[0]:
        state = None
        await bot.send_message(message.from_user.id, "Главное меню", reply_markup=client_kb.client_main_menu())

# Обработчик меню "Меню"




# Обработчик меню "Администрация"




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(answer_for_start_command, commands=["start"])
    dp.register_message_handler(load_help_menu, lambda x: x.text.startswith("❓Помощь❓"))
    dp.register_message_handler(contacts, lambda x: x.text.startswith("контакты"))
    dp.register_message_handler(back, lambda x: x.text.startswith("назад"))