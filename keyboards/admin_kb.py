from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    addAdminBtn = KeyboardButton("➕Добавить администратора➕")
    delAdminBtn = KeyboardButton("❌Удалить администратора❌")
    addToMenuBtn = KeyboardButton("➕Добавить в меню➕")
    delFromMenuBtn = KeyboardButton("❌Удалить из меню❌")
    backToMainMenuBtn = KeyboardButton("🔙Назад в меню🔙")
    rkm.add(addAdminBtn).add(delAdminBtn).add(addToMenuBtn).add(delFromMenuBtn).add(backToMainMenuBtn)
    return rkm