"""
command: pip install pyTelegramBotAPI
"""
import telebot

TOKEN = "<YOUR_BOT_TOKEN>"  # Bot token obtained from BotFather
STICKER = "path/to/sticker"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def welcome(message):
    raw_message = message.text
    user_name = message.from_user.first_name
    """
    The main function acts as a message handler for text messages.
    When a text message is received, this function will be automatically called by the telebot library.
    The received message is sent back as a response to the same chat.
    """
    if raw_message == '/start':

        sticker = open(STICKER, 'rb')
        bot.send_sticker(chat_id=message.chat.id, sticker=sticker)
        # answer
        bot.send_message(chat_id=message.chat.id, text=f"Welcome {user_name}")

    elif message.text.startswith("/"):
        pass
    else:
        bot.send_message(chat_id=message.chat.id, text=raw_message)


bot.polling(none_stop=True)

