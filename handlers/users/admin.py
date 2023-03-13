from aiogram import types
from keyboards.default.baza_button import menu_buttons
from loader import dp


# Echo bot
@dp.message_handler(text="🧑‍💻 Bot admini")
async def bot_echo(message: types.Message):
    await message.answer(text="""Admin:@Tojaliyev_1817
Telefon:+998906341817
Instagram:oyatillotojaliyev4""",reply_markup=menu_buttons)

@dp.message_handler(text="✍️ Fikr bildirish")
async def bot_echo(message: types.Message):
    await message.answer(text="""Qanday fikringiz bo'lsa botda yozib qoldirishingiz mumkin biz albatta fikringizni inobatga olamiz""",reply_markup=menu_buttons)



