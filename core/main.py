import telebot
import os
from dotenv import load_dotenv
import logging
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
#log
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

#load .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("API_TOKEN is missing!")
bot = telebot.TeleBot(API_TOKEN)

#Bot 
@bot.callback_query_handler(func=lambda call:call.data == 'start')
@bot.message_handler(commands=['start'])
def send_wellcome(message):
    logger.info('wellcome')
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton('محصولات', callback_data='products'),
        InlineKeyboardButton('کمک!',callback_data='help'),
        InlineKeyboardButton("صفحات مجازی", callback_data='websites'),
        InlineKeyboardButton('درباره ما', callback_data='aboutus'),

    ]
    markup.add(*buttons)
    wellcome_text ='''
به ربات راین خوش آمدی
چه کاری میتونم برات انحام بدم؟
'''
    bot.send_message(
        message.chat.id,
        wellcome_text,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call:call.data == 'websites')
def handle_websites(call):
    logger.info('websites')
    markup = InlineKeyboardMarkup(row_width=2)
    buttons =[
        InlineKeyboardButton('سایت',url='https://www.benistore.com'),
        InlineKeyboardButton('اینستگرام',url='https://www.instagram.com/beni/'),
        InlineKeyboardButton(' کانال تلگرام',url='https://www.telegram.org/beni_storeeee'),
    ]
    markup.add(*buttons)
    bot.edit_message_text('صفحات ما:', call.message.chat.id, call.message.message_id, reply_markup=markup)
    
# Products ID 
file_ids = {
    'abchekan': list(range(25,42)),
}

@bot.callback_query_handler(func=lambda call:call.data == 'products')
def handle_product(call):
    logger.info('products')
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton('لولا و چفت', callback_data='lola'),
        InlineKeyboardButton('جک کابینت و تخت', callback_data='jack'),
        InlineKeyboardButton('روشنایی', callback_data='lightning'),
        InlineKeyboardButton('تجهیزات کابینت', callback_data='cabinet'),
        InlineKeyboardButton('ریل کشو', callback_data='kesho'),
        InlineKeyboardButton('ابزار نجاری', callback_data='lamber'),
        InlineKeyboardButton('اتاق خواب', callback_data='bedroom'),
        InlineKeyboardButton('یراق و اتصالات', callback_data='yve'),
        InlineKeyboardButton('درب ریلی و کرکره ای', callback_data='drk'),
        InlineKeyboardButton('یراق درب ساختمان', callback_data='ydb'),
        InlineKeyboardButton('دستگیره کابینت', callback_data='dsk'),
        InlineKeyboardButton('جالباسی', callback_data='jalebasi'),

    ]
    markup.add(*buttons)
    bot.edit_message_text('محصولات ما', call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data == 'cabinet')
def cabinet_handler(call):
    logger.info('cabinet')
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton('سوبرها',callback_data='supers'),
        InlineKeyboardButton('جالیوان و بطری سقفی',callback_data='glassholder'),
        InlineKeyboardButton('لوازم نظم دهنده کابینت',callback_data='ordering_cabinet')
    ]
    markup.add(*buttons)
    bot.edit_message_text('انواع تجهیزات کابینت', call.message.chat.id, call.message.message_id,reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data == 'ordering_cabinet')
def ordering_cabinet_handler(call):
    logger.info('ordering cabinet')
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton('سطل زباله',callback_data='supers'),
        InlineKeyboardButton('آبچکان کابینت',callback_data='abchekan'),
        InlineKeyboardButton('جای قاشق چنگال',callback_data='ordering_cabinet'),
        InlineKeyboardButton('بازگشت',callback_data='cabinet')
    ]
    markup.add(*buttons)
    bot.edit_message_text('انواع تجهیزات کابینت', call.message.chat.id, call.message.message_id,reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: call.data == 'abchekan')
# def abchekan_handler(call):
#     logger.info('abchekan')
    
#     for msg_id in file_ids['abchekan']:
#         bot.forward_message(
#             chat_id= call.message.chat.id,
#             from_chat_id='-1002917339199',
#             message_id=msg_id
#         )

@bot.callback_query_handler(func=lambda call: call.data == 'abchekan')
def abchekan_handler(call):
    logger.info('abchekan')
    for msg_id in file_ids['abchekan']:
        # دکمه اینلاین برای پشتیبانی با کد کالا
        markup = InlineKeyboardMarkup()
        support_button = InlineKeyboardButton(
            text='🛎️ ارسال کد به پشتیبانی',
            url='https://t.me/i4lijalali'
        )
        markup.add(support_button)
        caption = f'کد کالا: {msg_id}\nبرای ارتباط با پشتیبانی روی دکمه زیر کلیک کنید.'
        # کپی پیام از کانال و اضافه کردن دکمه
        bot.copy_message(
            chat_id=call.message.chat.id,
            from_chat_id='-1002917339199',
            message_id=msg_id,
            reply_markup=markup
        )

# log channel post
@bot.channel_post_handler(func=lambda m:True)
def log_channel_handler(message):
    print(f'Message ID: {message.message_id}')

bot.infinity_polling()


