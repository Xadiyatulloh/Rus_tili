from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import base

menular = base.select_all_menular()

j = 0
index = 0
keys = []
for menu in menular:
    if j % 1 == 0 and j != 0:
        index += 1
    if j % 1 == 0:
        keys.append([KeyboardButton(text=f'{menu[1]}', )])
    else:
        keys[index].append(KeyboardButton(text=f'{menu[1]}' ,))
    j += 1

keys.append([KeyboardButton(text='🧑‍💻 Bot admini')])
keys.append([KeyboardButton(text='✍️ Fikr bildirish')])
menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)