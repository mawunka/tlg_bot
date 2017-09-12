# -*- coding: utf-8 -*-
import telebot, datetime, random
token = '396281526:AAEJe7koxfwuILQcvZpRNdCALlRO5FrfYrg'
GROUP_ID = -226450723 #test
#GROUP_ID = -1001134134257 #real-group
#test
bot = telebot.TeleBot(token)
hello = ['прив', 'хелло', 'здравствуйте', 'добрый вечер', 'добрый день', 'приветь', 'hello', 'hi', 'good morning', 'hey', 'ayo', 'эйо', 'zdorov', 'даров', 'дороу', 'дратути']
hello_answ = ['И тебе привет', 'даров', 'хелоу', 'драсть', 'здарова пидр))000', 'Доброго времени суток!', 'Oi', 'Hi :)', 'hello']
seva = ['сева', 'сево']
seva_answ = ['Я лучше Севы)))', 'Что?', 'мм?', 'а']
#bot_req = []
bot_answ = ['отсоси(', 'сам такой', '=(((9', 'ой всё.']

hour = datetime.datetime.now().hour
a,b,c = [18,19,20,21,22,23,24,0,1,2,3,4], [5,6,7,8,9,10,11], [12,13,14,15,16,17]
if hour in a:
	bot.send_message(GROUP_ID, 'Добрый вечер, господа!')
elif hour in b:
	bot.send_message(GROUP_ID, 'Доброе утро, господа!')
else:
	bot.send_message(GROUP_ID, 'Добрый день, господа!')
@bot.message_handler(commands=['help'])
def hlp(message):
	bot.send_message(message.chat.id, ''' Я еще мал и глуп (( пока могу отвечать только на слова:
	'privet', 'hello', 'hi', 'test', 'тест', 'Сева' ''')

@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def repeat_all_messages(message):
	#prvt = ['privet', 'hello', 'hi']
	#tst = ['test', 'тест']
	if (message.text == 'бот пидр'):
		bot.send_message(message.chat.id, random.choice(bot_answ))
	if (message.text.lower().startswith(seva[1]) or message.text.lower().startswith(seva[0])):
			bot.send_message(message.chat.id, random.choice(seva_answ))
	for answ in hello:
		if message.text.lower().startswith(answ):
			bot.send_message(message.chat.id, random.choice(hello_answ))
	
		
	#elif (message.text in tst):
	#	bot.send_message(message.chat.id, 'pass')
	#elif (message.text == 'Сева'):
	#	bot.send_message(message.chat.id, 'я лучше Севы )))) ')
if __name__ == '__main__':
	bot.polling(none_stop=True)
#	
#for i in y:
#	if m.startswith(i):