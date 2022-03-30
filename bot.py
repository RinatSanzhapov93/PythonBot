from turtle import update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO, filename='bot.log')

print("Бот запущен. Нажмите Ctrl+C для завершения")

def greet_user(update, bot):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)

def talk_to_me(update, bot):
	user_text = "Привет {}! ты написал {}".format(update.message.chat.first_name, update.message.text)
	logging.info("User %s, Chat id %s, Message %s", update.message.chat.username, update.message.chat.id, update.message.text)
	print(update.message)
	update.message.reply_text(user_text)

def main():
	token = settings.api_key
	mybot = Updater(token, use_context=True)
	logging.info('Бот запускается')
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()

main()