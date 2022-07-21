from random import randint
import time
import telebot



bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "it's a wheel of fortune bot\npress /wheel_of_fortune\nwrite a list of words separated by commas with spaces\nand find out the result")


@bot.message_handler(commands=['wheel_of_fortune'])
def wheel_of_fortune(message):
    bot.send_message(message.from_user.id, 'write a list of words separated by commas with spaces')
    bot.register_next_step_handler(message, result)

def result(message):
    list_ = list(message.text.split(', '))
    sec = 0.01
    list_val = 1
    res = bot.send_message(message.from_user.id, list_[0])
    for word in range(randint(5, 10)):
        bot.edit_message_text(chat_id = message.from_user.id, message_id = res.message_id, text = list_[list_val])

        if list_val < len(list_):
            list_val += 1
        if list_val == len(list_):
            list_val = 0

        sec += 0.01
        time.sleep(sec)
    
        
bot.polling(non_stop=True)