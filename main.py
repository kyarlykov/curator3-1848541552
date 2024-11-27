from telebot import TeleBot

bot = TeleBot('7538483547:AAExMY6fWnnYfXOF8nGngUU7q-rjdR_pPQ8')


@bot.message_handler(commends=['Привет'])
def botic(message):
    bot.send_message(message.chat.id, 'Барев')

@bot.message_handler(commends=['Как дела?'])
def botic(message):
    bot.send_message(message.chat.id, 'Горцерт вонц ен?')

@bot.message_handler(commends=['Хорошо,спасибо'])
def botic(message):
    bot.send_message(message.chat.id, 'Лав,апрес')

@bot.message_handler(commends=['Отлично,тогда до встречи,привет передай маме и папе'])
def botic(message):
    bot.send_message(message.chat.id, 'Де лава,уремн минч андипум,мамаин папаин кбаревес')




bot.infinity_polling()