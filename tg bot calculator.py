import telebot
import math

TOKEN = '6502691676:AAFOL6TitnKHMwrFrPrNj4VOloJng'
bot = telebot.TeleBot(TOKEN)                                                                     

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('c', callback_data='c'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),                                                                    
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data=','),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start'])                                                                      
def say_hello(message):
    bot.send_message(message.from_user.id, 'Привет, я очень неудобный и кривой калькулятор. Но если хочешь мной пользоваться я постараюсь сделать все возможное. Набери /calc и вылезет калькулятор!')   


@bot.message_handler(commands=['calc'])
def getmessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)                                                      
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

     

@bot.callback_query_handler(func=lambda call: True)
def do_callback(query):
    global value, old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'c':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:-1]
    elif data == '=':                                                      
        try:
            value = str(eval(value))
        except:
            value = 'Ты дурак? Так делать нельзя!'
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
    old_value = value   
    if value == 'Ты дурак? Так делать нельзя!':
        value = ''     

bot.polling(3)                                                       
