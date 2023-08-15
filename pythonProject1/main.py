import telebot
from telebot import types
import json
import random

bot = telebot.TeleBot("6653300108:AAFhPJp_q2eu2iUTj-6c4p757X9k8jHNWpw")

print('--BotWorking--')

# --	-- Reserved_Functions -- 	--
# --	-- Reserved_Functions -- 	--

with open('Films.json', 'r', encoding='utf-8') as file_films:
	Films = json.load(file_films)
with open('Serials.json', 'r', encoding='utf-8') as file_serials:
	Serials = json.load(file_serials)

	# ---- GanresFunc ----
	# ---- GanresFunc ----
def Comedy(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Комедія':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Drama(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Драма':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Action(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Бойовик':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Detectiv(FilmsOrSerials, cid):
	print('test')
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Детектив':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Fiction(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Фантастика':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
def Horror(FilmsOrSerials, cid):
	for film in FilmsOrSerials:
		if film["film_ganre"] == 'Жахи':
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=ganres_reply_menu())
	# ---- Codes&Random ----
	# ---- Codes&Random ----
def Random(FilmsOrSerials, cid):
	randomized = random.randint(1, len(FilmsOrSerials))
	for film in FilmsOrSerials:
		if randomized == film["film_code"]:
			photo = open(film["film_info"]['img'], 'rb')
			bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=first_reply_menu())

#	Фукція за якою користувач вводить число (код до фільму чи серіалу)
#	Після чого відкриється цикл який буде шукати відповідний фільм чи серіал за кодом
#	Після цього виведить фільм чи серіал повідомленням у тг (також має бути try: .. expect..: щоб не дуло помилок)
#	Потібно щоб ця функція виконулался ЯКЩО (продовження на 194 рядку...)
def Codes(msg, cid, FilmsOrSerials):
	print(msg)
	# for film in FilmsOrSerials:
	# 	if film["film_code"] == msg.text:
	# 		photo = open(film["film_info"]['img'], 'rb')
	# 		bot.send_photo(cid, photo, caption=film["film_info"]['text'], reply_markup=films_first_reply_menu())

# --	-- Values -- 	--
# --	-- Values -- 	--

counters = {
    "menu_films": 0,
	"film_serial": 0   # 1 - films 2 - serials
}

# --	-- REPLY_MENUS SECTION --	--
# --	-- REPLY_MENUS SECTION --	--

def main_reply_menu():
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_main.row(types.KeyboardButton('🎞 Фільми'), types.KeyboardButton('🎬 Серіали'))
    return markup_main

def first_reply_menu():
	markup_films1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films1.row(types.KeyboardButton('🔎 Пошук за жанрами'), types.KeyboardButton('🔎 Пошук за кодом'))
	markup_films1.row(types.KeyboardButton('🎲 Випадкове'), types.KeyboardButton('↩ Назад'))
	return markup_films1

def ganres_reply_menu():
	markup_films2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films2.row(types.KeyboardButton('😄 Комедія'), types.KeyboardButton('😿 Драми'))
	markup_films2.row(types.KeyboardButton('💣 Бойовики'), types.KeyboardButton('🕵‍♂️ Детектив'))
	markup_films2.row(types.KeyboardButton('🛸 Фантастика'), types.KeyboardButton('👻 Жахи'))
	markup_films2.row(types.KeyboardButton('↩ Назад'))
	return markup_films2
def codes_reply_menu():
	markup_films3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup_films3.row(types.KeyboardButton('➡ Ввести код'), types.KeyboardButton('↩ Назад'))
	return markup_films3

# --	-- COMMANDS --	--
# --	-- COMMANDS --	--

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Початок!", reply_markup=main_reply_menu())

@bot.message_handler(commands=['test'])
def send_welcome(message):
	bot.reply_to(message, f"a = 1", reply_markup=main_reply_menu())

# --	-- MSGs --	--
# --	-- MSGs --	--

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	cid = msg.chat.id

	if msg.text == '🎞 Фільми':
		bot.send_message(cid, '🍿 Фільми - хороший вибір!', reply_markup=first_reply_menu())
		counters['menu_films'] += 1
		counters['film_serial'] = 1
		print(counters['film_serial'])
	elif msg.text == '🎬 Серіали':
		bot.send_message(cid, '🥤 Серіали, чудовий спосіб провести кілька вечорів!', reply_markup=first_reply_menu())
		counters['menu_films'] += 1
		counters['film_serial'] = 2
		print(counters['film_serial'])
	elif msg.text == '↩ Назад' and counters['menu_films'] == 1:
		bot.send_message(cid, 'Назад 🧭', reply_markup=main_reply_menu())
		counters['menu_films'] -= 1

	# ---- Ganres_Films ----

	elif msg.text == '🔎 Пошук за жанрами' and counters['menu_films'] == 1:
		bot.send_message(cid, '🕹 Оберіть жанр', reply_markup=ganres_reply_menu())
		counters['menu_films'] += 1
	elif msg.text == '↩ Назад' and counters['menu_films'] == 2:
		bot.send_message(cid, 'Назад 🧭', reply_markup=first_reply_menu())
		counters['menu_films'] -= 1
	# ---- Codes_Films ----
	elif msg.text == '🔎 Пошук за кодом' and counters['menu_films'] == 1:
		bot.send_message(cid, 'Пошук за кодом 🔍', reply_markup=codes_reply_menu())
		counters['menu_films'] += 1
	elif msg.text == '↩ Назад' and counters['menu_films'] == 2:
		bot.send_message(cid, 'Назад 🧭', reply_markup=first_reply_menu())
		counters['menu_films'] -= 1

# ---	- GANRES -	---
# ---	- GANRES -	---
	elif msg.text == '😄 Комедія':
		if counters['film_serial'] == 1:
			Comedy(Films, cid)
		elif counters['film_serial'] == 2:
			Comedy(Serials, cid)
	elif msg.text == '😿 Драми':
		if counters['film_serial'] == 1:
			Drama(Films, cid)
		elif counters['film_serial'] == 2:
			Drama(Serials, cid)
	elif msg.text == '💣 Бойовики':
		if counters['film_serial'] == 1:
			Action(Films, cid)
		elif counters['film_serial'] == 2:
			Action(Serials, cid)
	elif msg.text == '🕵‍♂️ Детектив':
		if counters['film_serial'] == 1:
			Detectiv(Films, cid)
		elif counters['film_serial'] == 2:
			Detectiv(Serials, cid)
	elif msg.text == '🛸 Фантастика':
		if counters['film_serial'] == 1:
			Fiction(Films, cid)
		elif counters['film_serial'] == 2:
			Fiction(Serials, cid)
	elif msg.text == '👻 Жахи':
		if counters['film_serial'] == 1:
			Horror(Films, cid)
		elif counters['film_serial'] == 2:
			Horror(Serials, cid)
# ---	- RANDOM -	---
# ---	- RANDOM -	---
	elif msg.text == '🎲 Випадкове':
		if counters['film_serial'] == 1:
			Random(Films, cid)
		elif counters['film_serial'] == 2:
			Random(Serials, cid)
# ---	- CODES -	---
# ---	- CODES -	---
	#	...Користувач нажав кнопку з цим текстом (➡ Ввести код)
	#	Після чого користувач вводить чилсло і так далі
	#	Кнопка знаходиться на 102 рядку
	elif msg.text == '➡ Ввести код':
		bot.send_message(cid, "Введіть код:")
		# bot.register_next_step_handler(cid, Codes(msg, cid, Films))

bot.infinity_polling()