from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from datetime import datetime
import ephem
import os


def get_now():
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def get_current_date():
    return datetime.now().strftime('%Y%m%d_%H%M%S')


log_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir_path, exist_ok=True)
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=f"logs/bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_detector(bot, update):
    try:
        _planet_candidate = update.message.text.split('planet')[1].strip()
        planet_name = getattr(ephem, _planet_candidate)(datetime.today())
        constellation = ephem.constellation(planet_name)
        update.message.reply_text(f'Planet: {planet_name.name} in constellation: {constellation[1]}')
    except Exception as err:
        print(f'{get_now()} Error {err}')
        x = [name for id, type, name in ephem._libastro.builtin_planets() if type == 'Planet' and name not in ('Sun','Moon')]
        all_planet_list = '\n/planet '.join(x)
        update.message.reply_text(f'Choose one of this planet:\n/planet {all_planet_list}')


def main():
    mybot = Updater('API_KEY', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_detector))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
