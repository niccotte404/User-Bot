from aiogram.utils import executor
from vars_ex import dp
from bot import admin, client, other
from database import userbot_database

async def beginning(_):
    print("Bot started OK")
    await userbot_database.create_db()
    

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)
    

executor.start_polling(dp, skip_updates=True, on_startup=beginning)