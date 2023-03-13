from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.default.baza_button import menu_buttons
from loader import dp, base, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    telegram_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism, familiya=fam, telegrami=telegram_id)
    except Exception:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_buttons)

@dp.message_handler(commands='reklama', chat_id='1073336812')
async def bot_start(message: types.Message):
     userlar = base.select_all_foydalanuvchilar()
     for user in userlar:
         telegrami = user[3]
         await bot.send_photo(chat_id=telegrami, photo='https://t.me/Python_bepul_darslar/127')


@dp.message_handler(text='⬅️Назад')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Rus tili darsliklar', reply_markup=menu_buttons)

menular = base.select_all_menular()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    maxsulotlar = base.select_rus_tili(turi=text)
    j = 0
    index = 0
    keys = []
    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
        j += 1

    keys.append([KeyboardButton(text='⬅️Назад')])
    maxsulot_button = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Rus tili darsliklar', reply_markup=maxsulot_button)

menular = base.select_all_rus_tili_darsliklar()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(menular)
    maxsulot = base.select_rus_til(nomi=text)
    maxsulot_nomi = maxsulot[1]
    maxsulot_videosi_1 = maxsulot[2]
    maxsulot_videosi_2 = maxsulot[3]
    maxsulot_videosi_3 = maxsulot[4]
    maxsulot_videosi_4 = maxsulot[5]
    user_id = message.from_user.id

    if message.text == "🎥 Video darsliklar 🎥":
        await bot.send_video(chat_id=user_id, video=maxsulot_videosi_1,caption='@Tojaliyev_1817')
        await bot.send_video(chat_id=user_id, video=maxsulot_videosi_2,caption='@Tojaliyev_1817')
        await bot.send_video(chat_id=user_id, video=maxsulot_videosi_3,caption='@Tojaliyev_1817')
        await bot.send_video(chat_id=user_id, video=maxsulot_videosi_4,caption='@Tojaliyev_1817')
    elif message.text == "🖼 Rasm darsliklar🖼":
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_1, caption='@Tojaliyev_1817')
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_2, caption='@Tojaliyev_1817')
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_3, caption='@Tojaliyev_1817')
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_4, caption='@Tojaliyev_1817')
    elif message.text == "📄 Text darsliklar 📄":
        await bot.send_message(chat_id=user_id,text="""Rus tilini o'rganamiz
    
    Вечеринка - кеча, ўтириш
    
    Переживать - ҳавотирланмоқ, ташвишланмоқ
    
    Рыжеволосый - сариқ (малла) сочли
    
    Творческий - ижодий
    
    Высокий - баланд (бўйли)
    
    Строгий - қаттиққўл, талабчан
    
    Справедливый - адолатли
    
    Руководитель - раҳбар
    
    Порядок - тартиб
    
    Детство - болалик
    
    Влюблённый - севишган, ошиқ
    
    Шатенка - қўнғир сочли (аёл)
    
    Блондинка - сарғиш сочли (аёл)
    
    Молодой - ёш
    
    Стройный - келишган, хушбичим
    
    Молодой человек - йигит
    
    Работать - ишламоқ
    
    Значит - демак
    
    Встречать - кутиб олмоқ
    
    Скучать - зерикмоқ, соғинмоқ""")

        await bot.send_message(chat_id=user_id,text="""Rus tilini o'rganamiz
    
    Tarjimasiga qaramasdan mustaqil tarjima qilishga urinib ko'ring.
    
    Моя работа
    
    1.  Слушаем, читаем
    
    — Где вы работаете?
    — Я работаю на стройке.
    — Вы работаете каждый день?
    — Да. Я работаю каждый день: понедельник, вторник, среда, четверг и пятница. Это мои рабочие дни.
    — Когда вы начинаете работать?
    — Я начинаю работать в 8 часов утра.
    — А когда кончается ваш рабочий день?
    — В пять часов вечера.
    — А когда вы обедаете?
    — Обед у нас в час дня.
    — Вы работаете зимой и летом?
    — Да. Я работаю круглый год: зимой, весной, летом и осенью.
    — Вы всегда отдыхаете в выходные дни?
    — Нет. Иногда мы работаем в субботу.
    — Часто?
    — Нет, не часто, редко. Может быть, один раз в месяц.
    -------------------------------------------------------------------------------
    Mening ishim
    
    1.Tinglaymiz, o’qiymiz
    
    — Siz qaerda ishlaysiz?
    — Men qurilishda ishlayman.
    — Siz har kuni ishlaysizmi?
    — Ha. Men har kuni ishlayman: dushanba, seshanba, chorshanba, payshanba, va juma. Bu mening ish kunlarim.
    — Siz ishingizni nechada boshlaysiz?
    — Men ishimni ertalabki soat 8 da boshlayman.
    — Ish kuningiz nechada tugaydi?
    — Kechki soat beshda.
    — Soat nechada tushlik qilasiz?
    — Tushligimiz kunduzgi soat 1da.
    — Siz qish va yozda ishlaysizmi?
    — Ha. Men yil bo’yi ishlayman: qishda, bahorda, yozda va kuzda.
    — Siz doimo dam olish kunlari dam olasiz mi?
    — Yo’q. Ba’zida biz shanba kuni ishlaymiz.
    — Tez-tez mi?
     — Yoq, tez-tez emas, onda-sonda. Oyda bir marta bo’lsa kerak.
     
    Mening ishim
    
    1.Tinglaymiz, o’qiymiz
    
    — Siz qayerda ishlaysiz?
    — Men qurilishda ishlayman.
    — Siz har kuni ishlaysizmi?
    — Ha. Men har kuni ishlayman: Dushanba, Seshanba, Chorshanba, Payshanba, va Juma. Bu mening ish kunlarim.
    — Siz ishingizni nechada boshlaysiz?
    — Men ishimni ertalabki soat 8 da boshlayman.
    — Ish kuningiz nechada tugaydi?
    — Kechki soat beshda.
    — Soat nechada tushlik qilasiz?
    — Tushligimiz kunduzgi soat 1da.
    — Siz qish va yozda ishlaysizmi?
    — Ha. Men yil bo’yi ishlayman: qishda, bahorda, yozda va kuzda.
    — Siz doimo dam olish kunlari dam olasiz mi?
    — Yo’q. Ba’zida biz shanba kuni ishlaymiz.
    — Tez-tez mi?
     — Yoq, tez-tez emas, onda-sonda. Oyda bir marta bo’lsa kerak.  
    """)

        await bot.send_message(chat_id=user_id, text="""Rus tilini o'rganamiz
    
    Настоящее время — действие которое происходит сейчас:
    Hozirgi zamon — Ayni paytda nima sodir bo'layotganini ifodalash uchun ishlatiladi.
    
    Bunda fe'llarning o'zgarishi quyidagicha bo'ladi:
    
    Я читаю
    Ты читаешь
    Он/она читает
    Мы читаем
    Вы читаете
    Они читают
    
    So'roqlari:
    Что делаю?
    Что делаешь?
    Что делает?
    Что делаем?
    Что делаете?
    Что делают?
    
    Настоящее время имеют только глаголы несовершенного вида.
    """)

        await bot.send_message(chat_id=user_id, text="""Rus tilini o'rganamiz
    
    Где тут справочная?
    Маълумот берувчи шӯъба қаерда?
    
    Регистрация билетов началась (закончилась)?
    Чипталар қайди бошланди(тугади)?
    
    Во сколько будет вылет?
    Учиш соат нечида?
    
    Счастливого пути! Храни Вас Бог!
    Оқ йӯл!
    
    Где можно купить сувениры? 
    Совғаларни қаердан олиш мумкин?
    
    Где можно обменять валюту?
    Пулни қаерда алмашиш мумкин?
    
    Где можно заказать такси? 
    Такси қаерда туради?
    
    Как мне дойти в ближайший отель?
    Яқинроқ меҳмонхонага қандай борай?
    
    Скажите, пожалуйста, где туалет?
    Узр! Ҳожатона қаерда?""")


        await bot.send_message(chat_id=user_id, text="""Rus tilini o'rganamiz
        
    дело - ish
    
    зеркало - oyna
    
    лето - yoz fasli
    
    место - joy
    
    слово - so'z
    
    государство - davlat
    
    единство - birlik
    
    искусство - san'at
    
    качество - sifat
    
    производство - ishlab chiqarish
    
    сердце - yurak
    
    счастье - baxt
    
    здоровье - sog'lik
    
    горе - baxtsizlik, qayg'u
    
    училище - bilim yurti
    
    внимание - diqqat
    
    движение -  harakat
    
    занятие - mashq
    
    решение - yechim
    
    собрание - yig'ilish
    """)

        await bot.send_message(chat_id=user_id, text="""Rus tilini o'rganamiz
    
    🔆ЯЗЫК - TIL
    🔆РАЗГОВОР - SUXBAT
    
    ❎Что вы сказали? - Nima dedingiz?
    
    ❎Кто это? - Kim bu?
    
    ❎Что? - Nima?
    
    ❎Вы поняли? - Tushundingizmi?
    
    ❎Вам понятно? - Tushunarlimi?
    
    ❎Мне понятно - Tushundim
    
    ❎Чего вы хотите? - Nima istaysiz?
    
    ❎Как? - Qanday?
    
    ❎Каким образом? - Qanday qilib?
    
    ❎Какой? - Qanaqa?
    
    ❎Где? - Qayerda?
    
    ❎Куда? - Qayerga?
    
    ❎Почему? - Nimaga?
    
    ❎Зачем? - Nega?
    
    ❎Сколько? - Qancha, nechta?
    
    ❎Кто здесь знает русский язык? - Bu yerda kim rustilini biladi?
    
    ❎Вы говорите по-русски? - Siz ruscha gaplasha olasizmi?
    
    ❎Вы знаете русский язык? - Siz rus tilini bilasizmi?
    
    ❎Я изучаю узбекский язык - Men O'zbek tilini o'rganyapman
    
    ❎Я xочу научиться говорит по-узбекски - O'zbek tilida gaplashishni o'rganmoqchiman
    
    ❎Вы меня понимаете? - Gapimga tushunyapsizmi?
    
    ❎Говорите медленнее - Sekinroq gapiring
    
    ❎Скажите пожалуйста - Marxamat qilib aytingchi
    
    ❎Напишите на этом листке - Manavi qog'ozga yozing
    
    ❎Что вы сказали? - Nima dedingiz?
    
    🙄☺️
    
    📚Biz Bilan Rustilini O'rganing📚
    """)

        await bot.send_message(chat_id=user_id, text="""Rus tilini o'rganamiz
    
    Sozlashuv❗️👇
    
    ЗДОРОВЬЕ -sog'liq
    Я чувствую себя плохо-O'zimni yomon his qilyapman
    
    У меня болит спина-Mening orqam og'riyapti
    
    Меня знобит-Eti'm uvushib ketyapti
    
    У меня кружится голова-Boshim aylanyapti
    
    У меня сильное головокружение-Boshim qattiq aylanyapti
    
    Я болен-Men betobman
    
    У меня болит голова-Boshim og'riyapti
    
    у меня аллергия на пенициллин-Penitsillinga allergiyam bor
    
    У меня высокое (низкое) давление-Qon bosimim baland (past)
    
    У меня болит здесь-Mening mana bu yerim og'riyapti
    
    У меня температура-Mening isitmam bor
    
    Я простыл (у меня насморк)-Men shamollab qoldim (men tumovman)
    
    У меня сильно болит зуб-Tishim qattiq og'riyapti
    
    Что-то попало в глаз-Ko'zimga nimadir kirdi
    
    Меня тошнит-Ko'nglim ayniyapti
    
    У меня проблемы с сердцем-Yuragim og'riyapti
    
    Я растянул связки на ноге-Oyoq pay la rim cho'zildi
    
    У меня болит горло-Tomog'im og'riyapti
    
    Я страдаю от бессонницы-Uyqusizlikdan qiynalyapman
    
    У меня заложен нос-Burnim bitib qoldi
    
    Я чувствую себя немного лучше-O'zimni biroz yaxshiroq his qilyapman
    
    У меня насморк-Men tumovman
    
    Diqqat Bilan Yod Oling❗️☝️
    """)

    elif message.text == "📓 Grammatika 📓":
        await bot.send_message(chat_id=user_id, text="""Rus tili grammatikasi
        
    Gap tuzishni o'rganamiz oz oz asta asta davomiy. (Что-што o'qiladi)
    
    Кто это? 
    
    1. Это мальчик 
    2. Это девушка
    3. Это доктор
    4. Это саййид
    
    Что это?
    
    1. Это стол
    2. Это ручка
    3. Это книга
    4. Это окнo
    
    -здравствуйте -  Salom
    -что это?   -  Bu nima?
    -это подарок  -  Bu sovg'a
    -а что это?   -  Bunisi nima?
    -это яйцо  -   Bunisi tuxum 
    -это троллейбус?   - -Bu trelleybusmi?-
    - да это троллейбус -   Ha bu trelleybus
    -это автобус?  -  Bu avtobusmi?
    -нет, это не автобус, это трамвай  -  Yo'q bu avtobus emas balki tramvay.
    
    Rustilidagi so'zlarga ma'no berilayotganda biror so'zni olib tashlab yoki biror so'zni qo'shib ya'ni Uzbek tiliga moslashtirib mano bersak bo'ladi albatta o'zimiz tushungan holda!
    Buning uchun mukammal qoidalar bilan o'rganib quloqni rustiliga o'rgatish rus tilidagi tovushlarni ko'p ko'p eshitish bilan, ko'z va tilni o'rgatish albatta ko'p ko'p ruscha matnlarni o'qishlik bilan bo'ladi ......""")


        await bot.send_message(chat_id=user_id, text="""Rus tili grammatikasi
          
    🔅 Баъзи феълларнинг истисно тариқасида ўзгача тусланиши. Уларни ёд олиш керак.

    Жить
    Я жи-в-у – Мы жи-в-ём
    Ты жи-в-ёшь – Вы жи-в-ёте
    Он/Она жи-в-ёт – Они жи-в-ут
    
    Ходить
    Я  хо-ж-у – Мы ход-им
    Ты ход-ишь – Вы ход-ите
    Он/Она ход-ит – Они ход-ят
    
    Есть
    Я е-м – Мы е-д-им
    Ты е-шь – Вы е-д-ите
    Он/Она е-ст – Они е-д-ят
    
    Писать
    Я пи-ш-у – Мы пи-ш-ем
    Ты пи-ш-ешь – Вы пи-ш-ете
    Он/Она пи-ш-ет – Они пи-ш-ут
    
    Любить
    Я люб-л-ю – Мы люб-им
    Ты люб-ишь – Вы люб-ите
    Он/Она люб-ит – Они люб-ят
    
    Ждать  
    Я жд-у – Мы жд-ём
    Ты жд-ёшь – Вы жд-ёте
    Он\Она жд-ёт – Они жд-ут
    
    Смеяться
    Я сме-ю-сь – Мы сме-ём-ся
    Ты сме-ёшь-ся – Вы сме-ёте-сь
    Он\Она сме-ёт-ся – Они сме-ют-ся""")

        await bot.send_message(chat_id=user_id, text="""Rus tili grammatikasi

    📌 Олмошлар
    
    Меники – Мой (Муж.род) Моя (жен.род) Моё (Ср.род)
    Сеники – Твой (Муж.род) Твоя (жен.род) Твоё (Ср.род)
    Уники - Его(Муж.род) Её (жен.род)
     Бизники - Наш
    Сизники - Ваш
    Уларники - Их
    Ўзимники - Свой (Муж.род) Своя (жен.род) Своё (Ср.род)
    Ўзимизники – Наш (Муж.род) Наша (жен.род) Наше (Ср.род)
    Ўзлариники - Их
     Ўзим - Я сам 
    Ўзинг - Ты сам 
    Ўзимиз - Мы сами 
    Ўзингиз - Вы сами 
    Ўзлари – Они сами 
    У (ўша) - Тот 
    Бу(ни), шу(ни) - Этот 
    Ўша (айнан) - Тот самый
     Улар (анавилар) - Они (те) 
    Булар – Эти 
    Ўшалар - Те самые 
    Ана бу (анави), ана шу, ана ўша - Вон тот (этот)
    """)

        await bot.send_message(chat_id=user_id, text="""Rus tili grammatikasi
    
    ✅Где?✅
    Предлог «В» ишлатиладигон
    вазият:
    1) Мамлакатлар, шахарлар, жойлар:
    в Евро́пе, в Аме́рике, в Москве́, 
    в го́роде, в дере́вне, в це́нтре
    2) Муассасалар, ташкилотлар:
    в институ́те, в университе́те, в рестора́не, 
    в кафе́, в шко́ле, в о́фисе, в кинотеа́тре,
    в магази́не, в оте́ле, в клу́бе, в музе́е
    3) Ижтимоий гурухлар:
    в семье́, в кла́ссе, в гру́ппе
    4) Нимадурри ичида булса:
    в до́ме, в самолёте, в кварти́ре, в столе́
    
    Предлог «На» ишлатиладигон
    вазият:
    1) Юналишлар:
    на се́вере, на ю́ге, на за́паде, на восто́ке
    2) Орол, дарёлар, Коллар, денгизлар, киргоклар, тоглар:
    на Ку́бе, на Во́лге, на Байка́ле, на мо́ре, на Ура́ле
    3) Агар объект нимадурни устида булса:
    на этаже́, на земле́, на у́лице, на проспе́кте, 
    на столе́, на пля́же
    4) Жараёнлар:
    на уро́ке, на рабо́те, на обе́де, 
    на прогу́лке, на о́пере, на вы́ставке
    """)
    elif message.text == "💰 Bepul darsliklar💰":
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_1, caption="""Rus tilini tushunasiz-u, yaxshi gaplasha olmaysizmi? Gap tuzishda qiynalasizmi? \nSo'z boyligingiz yaxshi emasmi? \nBuni to'g'irlash kerak!\n\n👇Kanalimizga a'zo bo'lishni unutmang\n\nhttps://t.me/rustili_tilini_organamiz""")
        await bot.send_photo(chat_id=user_id, photo=maxsulot_videosi_2, caption="""Rus tilini tushunasiz-u, yaxshi gaplasha olmaysizmi? Gap tuzishda qiynalasizmi? \nSo'z boyligingiz yaxshi emasmi? \nBuni to'g'irlash kerak!n\n\n👇Kanalimizga a'zo bo'lishni unutmang\n\nhttps://t.me/rus_tilini_organamz""")

