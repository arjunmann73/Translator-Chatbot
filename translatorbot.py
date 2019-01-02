import urllib
import time, telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import random
from telepot import DelegatorBot
from telepot.delegate import pave_event_space, per_chat_id, create_open

TOKEN = '692167822:AAFd3ebAn8_Fik24QKAoz2_BE7sunzXUptU'


trans_rest = 0
trans_text = 1
trans_lang = 2

class translatorbot(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(translatorbot, self).__init__(include_callback_query=True, *args, **kwargs)
        self.state = trans_rest
        self.initial = ''

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if(msg_text == '/start'):
                response = "Hello! I am a translator bot! To use me, say '/translate'. To find out all the languages you can translate to and from, say '/list'."
                bot.sendMessage(chat_id, response)
            elif(msg_text == '/list'):
                all_langs = { 'azerbaijan': 'az' ,	'malayalam'	: 'ml',
                'albanian':	'sq',	'maltese' :	'mt',
                'amharic' :	'am',  	'macedonian' :	'mk',
                'english' :	'en',	'maori' :	'mi',
                'arabic' :	'ar',	'marathi' :	'mr',
                'armenian' :	'hy',	'mari' :	'mhr',
                'afrikaans'	: 'af',  'mongolian' :	'mn',
                'basque' :	'eu',	'german' :	'de',
                'bashkir' :	'ba',	'nepali' :	'ne',
                'belarusian' :	'be',	'norwegian' :	'no',
                'bengali' :	'bn',	'punjabi' :	'pa',
                'burmese' :	'my',	'papiamento' :	'pap',
                'bulgarian' :	'bg', 'persian' :	'fa',
                'bosnian' :	'bs'	,'polish' :	'pl',
                'welsh' :	'cy',	'portuguese' :	'pt',
                'hungarian' :	'hu',	'romanian' :	'ro',
                'vietnamese' :	'vi',  	'russian' :	'ru',
                'haitian' :	'ht',	'cebuano' :	'ceb',
                'galician'	: 'gl',	'serbian' :	'sr',
                'dutch':	'nl',	'sinhala':	'si',
                'hillmari':	'mrj',	'slovakian':	'sk',
                'greek':	'el',	'slovenian':	'sl',
                'georgian':	'ka',	'swahili':	'sw',
                'gujarati':	'gu',	'sundanese':	'su',
                'danish':	'da',	'tajik'	:'tg',
                'hebrew':	'he',	'thai'	:'th',
                'yiddish':	'yi',	'tagalog'	:'tl',
                'indonesian':	'id',	'tamil'	:'ta',
                'irish':	'ga',	'tatar'	:'tt',
                'italian'	:'it',	'telugu':	'te',
                'icelandic':	'is',	'turkish'	:'tr',
                'spanish':	'es',	'udmurt':	'udm',
                'kazakh':	'kk',	'uzbek'	:'uz',
                'kannada':	'kn',	'ukrainian':	'uk',
                'catalan':	'ca',	'urdu':	'ur',
                'kyrgyz':	'ky',	'finnish'	:'fi',
                'chinese':	'zh',	'french':	'fr',
                'korean':	'ko',	'hindi'	:'hi',
                'xhosa'	:'xh',	'croatian':	'hr',
                'khmer'	:'km',	'czech'	:'cs',
                'laotian':	'lo',	'swedish'	:'sv',
                'latin'	:'la',	'scottish':	'gd',
                'latvian':	'lv',	'estonian':	'et',
                'lithuanian':	'lt',	'esperanto':	'eo',
                'luxembourgish':'lb',	'javanese':	'jv',
                'malagasy':	'mg',	'japanese'	:'ja',
                'malay':	'ms'	}
                response = ''
                i = 1
                for key in all_langs:
                    response += str(i) + "." + " " + str(key) + "\n"
                    i += 1
                bot.sendMessage(chat_id, response)
            elif(msg_text == '/translate' and self.state == trans_rest):
                response = 'Let me give you an example of how to use me: \nBot : Send me the text you wanna translate!\nUser : Hello world\nBot: Which language do you wanna translate it to?\nUser : spanish\nBot: hola mundo'
                bot.sendMessage(chat_id, response)
                response = 'Send me the text you wanna translate!'
                bot.sendMessage(chat_id, response)
                self.state = trans_text
            else:
                if(self.state > trans_rest):
                    if(self.state == trans_text):
                        self.initial = msg_text
                        response = 'Which language do you wanna translate it to (say /list to check all languages)?'
                        bot.sendMessage(chat_id, response)
                        self.state = trans_lang
                    if(self.state == trans_lang and msg_text != self.initial):
                        lang = msg_text.lower()
                        all_lang = { 'azerbaijan': 'az' ,	'malayalam'	: 'ml',
                        'albanian':	'sq',	'maltese' :	'mt',
                        'amharic' :	'am',  	'macedonian' :	'mk',
                        'english' :	'en',	'maori' :	'mi',
                        'arabic' :	'ar',	'marathi' :	'mr',
                        'armenian' :	'hy',	'mari' :	'mhr',
                        'afrikaans'	: 'af',  'mongolian' :	'mn',
                        'basque' :	'eu',	'german' :	'de',
                        'bashkir' :	'ba',	'nepali' :	'ne',
                        'belarusian' :	'be',	'norwegian' :	'no',
                        'bengali' :	'bn',	'punjabi' :	'pa',
                        'burmese' :	'my',	'papiamento' :	'pap',
                        'bulgarian' :	'bg', 'persian' :	'fa',
                        'bosnian' :	'bs'	,'polish' :	'pl',
                        'welsh' :	'cy',	'portuguese' :	'pt',
                        'hungarian' :	'hu',	'romanian' :	'ro',
                        'vietnamese' :	'vi',  	'russian' :	'ru',
                        'haitian' :	'ht',	'cebuano' :	'ceb',
                        'galician'	: 'gl',	'serbian' :	'sr',
                        'dutch':	'nl',	'sinhala':	'si',
                        'hillmari':	'mrj',	'slovakian':	'sk',
                        'greek':	'el',	'slovenian':	'sl',
                        'georgian':	'ka',	'swahili':	'sw',
                        'gujarati':	'gu',	'sundanese':	'su',
                        'danish':	'da',	'tajik'	:'tg',
                        'hebrew':	'he',	'thai'	:'th',
                        'yiddish':	'yi',	'tagalog'	:'tl',
                        'indonesian':	'id',	'tamil'	:'ta',
                        'irish':	'ga',	'tatar'	:'tt',
                        'italian'	:'it',	'telugu':	'te',
                        'icelandic':	'is',	'turkish'	:'tr',
                        'spanish':	'es',	'udmurt':	'udm',
                        'kazakh':	'kk',	'uzbek'	:'uz',
                        'kannada':	'kn',	'ukrainian':	'uk',
                        'catalan':	'ca',	'urdu':	'ur',
                        'kyrgyz':	'ky',	'finnish'	:'fi',
                        'chinese':	'zh',	'french':	'fr',
                        'korean':	'ko',	'hindi'	:'hi',
                        'xhosa'	:'xh',	'croatian':	'hr',
                        'khmer'	:'km',	'czech'	:'cs',
                        'laotian':	'lo',	'swedish'	:'sv',
                        'latin'	:'la',	'scottish':	'gd',
                        'latvian':	'lv',	'estonian':	'et',
                        'lithuanian':	'lt',	'esperanto':	'eo',
                        'luxembourgish':'lb',	'javanese':	'jv',
                        'malagasy':	'mg',	'japanese'	:'ja',
                        'malay':	'ms'	}
                        lang = all_lang[lang]

                        love = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20181229T150801Z.b288233d362575d8.97dbbd3485c8219a97e9eb09cd73168419be48b2&text=' + self.initial + '&lang=' + lang + '&[format=%3Cplain%3E]&[options=1]'
                        textstring = requests.get(love).json()
                        response = textstring['text'][0]
                        self.state = trans_rest
                        bot.sendMessage(chat_id, response)



    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

        #inline_message_id = msg['message']['chat']['id'], msg['message']['message_id']
        #bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)

        #bot.answerCallbackQuery(query_id)


bot = DelegatorBot(TOKEN, [
    pave_event_space()
    (per_chat_id(), create_open, translatorbot, timeout=100)
])
MessageLoop(bot).run_as_thread()

bot_name = bot.getMe()['first_name']
print(bot_name + ' at your service...')

# keep the program running and simulate cat life
cat_last_update = time.time()
while True:
    time.sleep(10)

# https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20181229T150801Z.b288233d362575d8.97dbbd3485c8219a97e9eb09cd73168419be48b2&text=hello&lang=ru&[format=%3Cplain%3E]&[options=1]
