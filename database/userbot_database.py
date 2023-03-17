import sqlite3
import random

async def create_db():
    global connect, cursor
    connect = sqlite3.connect("userbot_database.db")
    cursor = connect.cursor()
    if connect:
        print("Database connected OK")
    cursor.execute("""CREATE TABLE IF NOT EXISTS usertypes(
        user_id INTEGER PRIMARY KEY,
        user_name TEXT,
        user_type TEXT
        )""")
    connect.commit()
    

async def add_user(message):
    user_id = message.from_user.id
    data = cursor.execute(f"SELECT user_id FROM usertypes WHERE user_id = {user_id}").fetchone()
    
    if data is None:
        if message.from_user.id == 1468286116:
            values = (message.from_user.id, message.from_user.username, "админ")
            cursor.execute("INSERT INTO usertypes VALUES (?, ?, ?)", values)
        else:
            values = (message.from_user.id, message.from_user.username, "юзверь")
            cursor.execute("INSERT INTO usertypes VALUES (?, ?, ?)", values)
        connect.commit()
        
    
async def admin_check(message):
    ids = cursor.execute("SELECT user_id FROM usertypes WHERE user_type = 'админ'").fetchall()
    for item in ids:
        item = item[0]
        if item == message.from_user.id:
            isAdmin = True
        else:
            isAdmin = False
    return isAdmin


async def admin_add(bot, message, user):
    if message:
        finding = cursor.execute(f"SELECT user_name FROM usertypes WHERE user_name = '{user}'").fetchone()
        if finding == None:
            await bot.send_message(message.from_user.id, "Этот пользователь не использует бот. Если ва хотите добавить пользователя в качестве администратора, попросите пользователя написать боту")
        else:
            user_id = cursor.execute(f"SELECT user_id FROM usertypes WHERE user_name = '{user}'").fetchone()[0]
            cursor.execute(f"DELETE FROM usertypes WHERE user_name = '{user}'")
            cursor.execute(f"INSERT INTO usertypes VALUES (?, ?, ?)", (user_id, user, "админ",))
        connect.commit()