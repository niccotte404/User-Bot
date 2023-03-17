from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def client_main_menu():
    
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    menuBtn = KeyboardButton("🍱Меню🍱")
    adminBtn = KeyboardButton("👑Администрация👑")
    helpBtn = KeyboardButton("❓Помощь❓")
    rkm.add(helpBtn, menuBtn).add(adminBtn)
    return rkm


def client_help_menu():
    
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    contactsBtn = KeyboardButton("☎️Контакты☎️")
    timetableBtn = KeyboardButton("📆Расписание📆")
    locationBtn = KeyboardButton("🌇Расположение🌇")
    backBtn = KeyboardButton("🔙Назад в меню🔙")
    rkm.add(contactsBtn, timetableBtn).add(locationBtn).add(backBtn)
    return rkm
    
    
def client_menu_menu():
    
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    nextBtn = KeyboardButton("➡️Далее➡️")
    backBtn = KeyboardButton("🔙Назад в меню🔙")
    rkm.add(nextBtn, backBtn)
    return rkm