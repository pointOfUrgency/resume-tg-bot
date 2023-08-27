from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Tok import Token


bot = Bot(Token)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton("Обо мне",
                          callback_data='me')
b2 = InlineKeyboardButton("Почему стоит работать со мной?",
                          callback_data='work')
b3 = InlineKeyboardButton("Мой стек технологий",
                          callback_data='stack')
b4 = InlineKeyboardButton("Связаться со мной",
                          callback_data='connect')
ikb.add(b1, b2, b3, b4)

photo1 = types.input_file.InputFile('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_2_2023-08-24_12-34-04.jpg')
# photo2 = types.input_file.InputFile('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_1_2023-08-24_12-34-04.jpg')
# photo3 = types.input_file.InputFile('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_3_2023-08-24_12-34-04.jpg')
# photo4 = types.input_file.InputFile('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_4_2023-08-24_12-34-04.jpg')


ABOUT_ME = '''
Мне очень интересно создавать функциональные, безопасные и интуитивно понятные веб-приложения. Однако моя страсть не ограничивается только программированием. Я также увлекаюсь психологией и медициной. Я считаю, что понимание, как люди мыслят и чувствуют, помогает мне создавать более интуитивные и пользовательские приложения. Комбинируя свои знания об информационной безопасности и психологии, я стремлюсь создавать безопасные приложения, которые не только эффективно решают задачи, но и обеспечивают удовлетворение пользователей.
'''
WHY = '''
У меня есть опыт разработки веб-приложений, где я использовал свои знания Python и Django для создания эффективных и современных решений. Я с удовольствием принимаю участие в проектах, где могу применить свои навыки и вносить свой вклад в развитие технологий. У меня всегда есть желание учиться новому и развиваться профессионально. Я готов работать в команде, обмениваться знаниями
'''
STACK = '''
Мой основной стек технологий включает язык программирования Python, фреймворк Django, Django REST Framework для создания RESTful API, систему контроля версий Git и язык разметки HTML.
'''


@dp.message_handler(commands=['start', 'на_главную'])
async def hello(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, 
                         photo=open('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_2_2023-08-24_12-34-04.jpg', "rb"),
                         caption='Привет! Меня зовут Артур Гунько, и я начинающий разработчик и студент направления информационной безопасности.',
                         reply_markup=ikb)
    await message.delete()


@dp.callback_query_handler(text='back')
async def home(callback: types.CallbackQuery):
    await callback.message.answer('Что вас интересует?', reply_markup=ikb)


@dp.callback_query_handler()
async def pages(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("Назад", callback_data='back')
    )
    links = InlineKeyboardMarkup().add(
        InlineKeyboardButton("GitHub", url='https://github.com/pointOfUrgency'),
        InlineKeyboardButton("Telegram", url='https://t.me/UrgUrgFuckedSociety')
    )
    if callback.data == 'me':
        await callback.message.answer_photo(open('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_1_2023-08-24_12-34-04.jpg', "rb"), caption=ABOUT_ME)
        await callback.message.delete()
        await callback.message.answer('Вернуться назад?', reply_markup=keyboard)
    elif callback.data == 'work':
        await callback.message.answer_photo(open('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_3_2023-08-24_12-34-04.jpg', "rb"), caption=WHY)
        await callback.message.delete()
        await callback.message.answer('Вернуться назад?', reply_markup=keyboard)
    elif callback.data == 'stack':
        await callback.message.answer_photo(open('D:\Python learning\Tg-bot-ArthurGunko\photos\photo_4_2023-08-24_12-34-04.jpg', "rb"), caption=STACK)
        await callback.message.delete()
        await callback.message.answer('Вернуться назад?', reply_markup=keyboard)
    elif callback.data == 'connect':
        await callback.message.answer('Куда отправимся?', reply_markup=links)
        await callback.message.answer('Вернуться назад?', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

